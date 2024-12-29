import os
import torch
import pymysql
import openai
from googleapiclient.discovery import build
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import UnstructuredURLLoader
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI as LangchainOpenAI
from transformers import pipeline
import streamlit as st

# .env 파일 로드
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GOOGLE_CSE_ID = os.getenv("GOOGLE_CSE_ID")

embedding_cache_file = "C:\\FINAL\\nejot\\DB_embedding\\1212_2차_embedding.pt"
device = "cpu"

def get_openai_embedding(text):
    try:
        response = openai.Embedding.create(
            model="text-embedding-ada-002",
            input=[text]
        )
        embedding = response["data"][0]["embedding"]
        return torch.tensor(embedding, device="cpu")
    except Exception as e:
        print(f"임베딩 생성 오류: {e}")
        return None

def calculate_similarity(vec1, vec2):
    if vec1.device != vec2.device:
        vec2 = vec2.to(vec1.device)
    vec1 = vec1 / torch.norm(vec1)
    vec2 = vec2 / torch.norm(vec2)
    similarity = torch.dot(vec1, vec2)
    return similarity.item()

def load_cached_embeddings():
    if os.path.exists(embedding_cache_file):
        data = torch.load(embedding_cache_file, map_location=device)
        return data
    else:
        return {}

def fetch_all_from_db(db_config):
    connection = pymysql.connect(**db_config)
    try:
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute("SELECT * FROM UserBenchmarks")
            rows = cursor.fetchall()
        return rows
    except Exception as e:
        print(f"DB 데이터 가져오기 오류: {e}")
        return None
    finally:
        connection.close()

def update_embedding_cache(embedding_cache_file, model_name, information):
    text_for_embedding = model_name
    if information and information.strip():
        text_for_embedding += " " + information.strip()
    new_embedding = get_openai_embedding(text_for_embedding)
    if new_embedding is not None:
        if os.path.exists(embedding_cache_file):
            embedding_cache = torch.load(embedding_cache_file, map_location="cpu")
        else:
            embedding_cache = {}
        embedding_cache[model_name] = new_embedding
        torch.save(embedding_cache, embedding_cache_file)

def insert_web_info_into_db(db_config, product_name, spec, web_info):
    connection = pymysql.connect(**db_config)
    try:
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            check_sql = "SELECT COUNT(*) as cnt FROM UserBenchmarks WHERE Model = %s"
            cursor.execute(check_sql, (spec,))
            result = cursor.fetchone()
            count = result['cnt']

            if count > 0:
                update_sql = "UPDATE UserBenchmarks SET information = %s WHERE Model = %s"
                cursor.execute(update_sql, (web_info, spec))
            else:
                insert_sql = """
                    INSERT INTO `UserBenchmarks` (`Type`, `Brand`, `Model`, `Rank`, `Benchmark`, `URL`, `information`)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                """
                cursor.execute(insert_sql, (None, None, spec, None, None, None, web_info))

        connection.commit()
        update_embedding_cache(embedding_cache_file, spec, web_info)
    except Exception as e:
        print(f"웹 정보 DB 저장 오류: {e}")
    finally:
        connection.close()

def search_with_cached_embeddings(embedding_cache, spec, all_data, similarity_threshold=0.9):
    if not embedding_cache:
        return {"details":"DB 관련 상세정보를 찾지 못했습니다."}

    user_embedding = get_openai_embedding(spec)
    if user_embedding is None:
        return {"details":"DB 관련 상세정보를 찾지 못했습니다."}

    best_match = {"model": None, "similarity": 0}
    for model_name, embedding in embedding_cache.items():
        sim = calculate_similarity(user_embedding, embedding)
        if sim > best_match["similarity"]:
            best_match = {"model": model_name, "similarity": sim}

    if best_match["similarity"] > similarity_threshold:
        for row in all_data:
            if row['Model'] == best_match['model']:
                rank = row.get('Rank', 'N/A')
                benchmark = row.get('Benchmark', 'N/A')
                url = row.get('URL', 'N/A')
                type_ = row.get('Type', 'N/A')
                brand = row.get('Brand', 'N/A')
                information = row.get('information', 'N/A')

                detailed_info = (
                    f"Type: {type_}\n"
                    f"Brand: {brand}\n"
                    f"Model: {best_match['model']}\n"
                    f"Rank: {rank}\n"
                    f"Benchmark: {benchmark}\n"
                    f"URL: {url}\n"
                    f"Information: {information}\n"
                )
                return {
                    "model": best_match['model'],
                    "rank": rank,
                    "benchmark": benchmark,
                    "url": url,
                    "similarity": best_match["similarity"],
                    "details": detailed_info
                }
        return {"details":"DB 관련 상세정보를 찾지 못했습니다."}
    else:
        return {"details":"DB 관련 상세정보를 찾지 못했습니다."}

def google_search(query, num=3):
    service = build("customsearch", "v1", developerKey=GOOGLE_API_KEY)
    res = service.cse().list(q=query, cx=GOOGLE_CSE_ID, num=num).execute()
    items = res.get("items", [])
    return items

def create_outline_with_additional_info(product_name, specs_info_list, blog_title, keywords):
    combined_info = ""
    for spec, db_info, web_info in specs_info_list:
        combined_info += f"스펙: {spec}\nDB정보:\n{db_info}\n웹 검색 정보:\n{web_info}\n\n"

    prompt = f"""
    다음은 제품 정보다.
    제품명: {product_name}
    스펙들에 대한 상세정보:
    {combined_info}

    키워드: {keywords}
    블로그 제목: {blog_title}

    위 정보들을 반영해서(스펙들에 대한 상세정보) 블로그 글의 목차를 만들어줘.
    각 목차 항목에 간단한 설명을 추가하는데, 스펙 상세정보에 나온 내용도
    적절히 녹여내서 목차 항목을 풍부하게 구성해줘.
    본론은 최대 3개까지만 만들어줘.
    """

    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role":"system","content":"너는 프로페셔널 광고 블로그 글 기획자다."},
            {"role":"user","content": prompt}
        ],
        temperature=0.7,
        max_tokens=2000
    )
    outline = response.choices[0].message.content
    return outline, combined_info

def generate_blog_content(outline, blog_title, keywords, product_name):
    content_prompt = PromptTemplate(
        input_variables=["outline"],
        template=f"""
        다음은 블로그 글 작성 가이드라인이다.

        목차:
        {{outline}}

        블로그 제목: {blog_title}
        키워드: {keywords}
        제품명: {product_name}

        목차를 읽고 목차를 그대로 복사하지 말고, 목차를 기반으로 목차의 각 항목에 대한 풍부한 설명을 포함한 새로운 광고성 블로그 글을 작성해주세요.
        그리고 애니메이션 캐릭터같이 귀여운 말투로 작성해주세요.
        최대한 전문적이고 설득력 있게 작성해줘.
        """
    )

    llm_gpt = ChatOpenAI(
        openai_api_key=openai.api_key,
        model_name="gpt-4o",
        temperature=0.7
    )

    content_chain = LLMChain(llm=llm_gpt, prompt=content_prompt)
    generated_content = content_chain.run({"outline": outline})
    return generated_content

def detect_hate_speech(text, pipe, chunk_size=512):
    results = []
    for start in range(0, len(text), chunk_size):
        chunk = text[start:start+chunk_size]
        chunk_result = pipe(chunk, truncation=True, max_length=chunk_size)
        results.extend(chunk_result)
    for res in results:
        label = res["label"].lower()
        if label in ["hate", "offensive"]:
            return label
    return "none"

############# Streamlit UI 부분 #############
st.title("블로그 글 자동 생성기")

product_name = st.text_input("제품명을 입력하세요:")
product_specs_input = st.text_input("제품 스펙을 쉼표로 구분해서 입력하세요:")
blog_title = st.text_input("블로그 제목을 입력하세요:")
keywords = st.text_input("키워드를 입력하세요(쉼표로 구분):")

if st.button("실행"):
    product_specs_list = [s.strip() for s in product_specs_input.split(",") if s.strip()]

    db_config = {
        "host": "influencerdb.c18uiyu26mws.ap-northeast-2.rds.amazonaws.com",
        "user": "admin",
        "password": "root12#$",
        "db": "finaldatabase",
        "charset": "utf8"
    }

    all_data = fetch_all_from_db(db_config)
    if all_data is None:
        st.error("DB 데이터를 가져오는 데 실패했습니다.")
    else:
        embedding_cache = load_cached_embeddings()
        specs_info_list = []
        for spec in product_specs_list:
            db_result = search_with_cached_embeddings(embedding_cache, spec, all_data)
            product_details_db = db_result.get("details", "DB 관련 상세정보를 찾지 못했습니다.")
            info_in_db = product_details_db != "DB 관련 상세정보를 찾지 못했습니다."

            if info_in_db:
                product_details_web = "웹 검색 스킵 (DB 정보 사용)"
            else:
                query = f"{spec} 설명"
                search_results = google_search(query, num=3)
                if not search_results:
                    product_details_web = "웹 검색 결과를 찾지 못했습니다."
                else:
                    urls = [item.get("link") for item in search_results[:5]]
                    loader = UnstructuredURLLoader(urls=urls)
                    docs = loader.load()

                    if not docs:
                        product_details_web = "웹 검색에서 추가 상세정보를 찾지 못했습니다."
                    else:
                        text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
                        split_docs = text_splitter.split_documents(docs)
                        embeddings = OpenAIEmbeddings(openai_api_key=openai.api_key)
                        vectorstore = FAISS.from_documents(split_docs, embeddings)
                        retriever = vectorstore.as_retriever(search_type="similarity", search_k=3)
                        qa_chain = RetrievalQA.from_chain_type(
                            llm=LangchainOpenAI(openai_api_key=openai.api_key),
                            chain_type="stuff",
                            retriever=retriever
                        )
                        question = f"한국어로 {query} 상세 스펙에 대한 설명을 해줘"
                        answer = qa_chain({"query": question})
                        product_details_web = answer["result"]
                    insert_web_info_into_db(db_config, product_name, spec, product_details_web)

            specs_info_list.append((spec, product_details_db, product_details_web))

        outline, combined_info = create_outline_with_additional_info(product_name, specs_info_list, blog_title, keywords)

        hate_speech_pipe = pipeline("text-classification", model="monologg/koelectra-base-v3-hate-speech")

        max_retries = 2
        final_content = None
        for attempt in range(max_retries):
            generated_content = generate_blog_content(outline, blog_title, keywords, product_name)
            predicted_label = detect_hate_speech(generated_content, hate_speech_pipe, chunk_size=512)
            if predicted_label == "none":
                final_content = generated_content
                break

        if final_content:
            st.subheader("생성된 블로그 글")
            st.write(final_content)
        else:
            st.error("혐오표현 감지로 인해 블로그 글 생성에 실패했습니다.")

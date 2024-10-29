from langchain_common.model import creat_chat_model, create_prompt

def make_chain(model_id):
    # 체인 생성 = 프롬프트 + 모델
    chain = create_prompt() | creat_chat_model(model_id)
    return chain
from PIL import Image
import chromadb
from transformers import ViTFeatureExtractor, ViTModel
import torch
import matplotlib.pyplot as plt
import requests
from glob import glob
from tqdm import tqdm

def get_image_path():
    IMAGE_DATA_PATH = "../../images/vector_db/food_images/"
    return IMAGE_DATA_PATH

def make_collection():
    client = chromadb.Client()
    collection = client.create_collection(name = "foods")
    return collection

def set_feature_extractor(feature_extxtractor_model='facebook/dino-vits16'):
    return ViTFeatureExtractor.from_pretrained(feature_extxtractor_model)

def set_vectordb_model(vectordb_model='facebook/dino-vits16'):
    device = "cuda" if torch.cuda.is_available() else "cpu"
    return ViTModel.from_pretrained(vectordb_model).to(device)

def set_image_data_path(IMAGE_DATA_PATH):
    return sorted(glob(IMAGE_DATA_PATH+"*/*.jpg"))

def save_vectordb(IMAGE_DATA_PATH, model, feature_extractor):
    embeddings = []
    metadatas = []
    ids = []
    for i, img_path in enumerate(tqdm(set_image_data_path(IMAGE_DATA_PATH))):
        img = Image.open(img_path)
        cls = img_path.split("/")[1]
        img_tensor = feature_extractor(images=img, return_tensors="pt").to("cuda")
        outputs = model(**img_tensor)
        embedding = outputs.pooler_output.detach().cpu().numpy().squeeze().tolist()
        embeddings.append(embedding)
        metadatas.append({
            "uri": img_path,
            "name": cls
        })
        ids.append(str(i))
    collection = make_collection()
    print(embeddings.size)
    collection.add(
        embeddings=embeddings,
        metadatas=metadatas,
        ids=ids,
    )
    print("Done!")
    return collection


def query(img_url, model, feature_extractor, collection, n_results=3):
    test_img = Image.open(requests.get(str(img_url), stream=True).raw).convert("RGB")

    test_img_tensor = feature_extractor(images=test_img, return_tensors="pt").to("cuda")
    test_outputs = model(**test_img_tensor)

    test_embedding = test_outputs.pooler_output.detach().cpu().numpy().squeeze()

    query_result = collection.query(
        query_embeddings=test_embedding.tolist(),
        n_results=n_results,
    )

    _, axes = plt.subplots(1, 4, figsize=(16, 10))

    axes[0].imshow(test_img)
    axes[0].set_title("Query")
    axes[0].axis("off")

    for i, metadata in enumerate(query_result["metadatas"][0]):
        distance = query_result["distances"][0][i]

        axes[i+1].imshow(Image.open(metadata["uri"]))
        axes[i+1].set_title(f"{metadata['name']}: {distance:.2f}")
        axes[i+1].axis("off")

    return query_result
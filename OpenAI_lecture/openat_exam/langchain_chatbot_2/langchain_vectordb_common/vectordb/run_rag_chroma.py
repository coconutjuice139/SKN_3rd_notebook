from .rag_chroma import get_image_path, make_collection, set_feature_extractor, set_vectordb_model, save_vectordb, query



def make_img_query(prompt):
    PATH = get_image_path()
    print(PATH)
    feature_extractor = set_feature_extractor()
    print(feature_extractor)
    model = set_vectordb_model()
    print(model)
    collection = save_vectordb(PATH, model, feature_extractor)
    print(collection)
    query_result = query(prompt, model, feature_extractor, collection=collection)
    return query_result
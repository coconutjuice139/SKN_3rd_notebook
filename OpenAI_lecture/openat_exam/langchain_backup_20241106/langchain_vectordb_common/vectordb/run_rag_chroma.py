from .rag_chroma import get_image_path, make_collection, set_feature_extractor, set_vectordb_model, save_vectordb, query



class FunctionTracker:
    def __init__(self):
        self.executed = False  # 초기 값 설정
    def run_collection(self):
        collection = make_collection()
        PATH = get_image_path()
        feature_extractor = set_feature_extractor()
        model = set_vectordb_model()
        collection = save_vectordb(PATH, model, collection, feature_extractor)
        self.executed = True
        return model, feature_extractor, collection

create_models = FunctionTracker()

def make_img_query(prompt, message_history=[]):
    prompt = str(prompt)
    if not create_models.executed:
        model, feature_extractor, collection = create_models.run_collection()
    query_result = query(prompt, model, feature_extractor, collection)
    message_history.append(query_result)
    return query_result
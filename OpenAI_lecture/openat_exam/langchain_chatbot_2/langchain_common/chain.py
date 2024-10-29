from langchain_common.model import creat_chat_model, create_prompt

def make_chain(model_id):
    return create_prompt() | creat_chat_model(model_id)
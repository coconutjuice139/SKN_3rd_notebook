import enum
class CHATBOT_ROLE(enum.Enum):
    user = (enum.auto, "user")
    assistant = (enum.auto, "assistant")
    
# message
class CHATBOT_MESSAGE(enum.Enum):
    role = (enum.auto, "role")
    content = (enum.auto, "content")
    
class CHATBOT_IMG(enum.Enum):
    type = (enum.auto, "image")
    url = (enum.auto, "url")
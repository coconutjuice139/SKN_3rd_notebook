import enum

class ERROR_MSG(enum.Enum):
    NO_MSG = (enum.auto(), "입력된 값이 없소...")
    EXIST_MSG = (enum.auto(), "이미 있는 값이오...")
    pass
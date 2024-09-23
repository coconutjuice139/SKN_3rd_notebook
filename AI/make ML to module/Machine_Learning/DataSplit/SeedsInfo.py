import os
import numpy as np
import random
import torch

def reset_seeds(seed = 50):
    random.seed(seed)
    # 파이썬 환경변수 고정
    os.environ['PYTHONHASHSEED'] = str(seed)
    np.random.seed(seed)
    # cpu 연산 무작위 고정
    torch.manual_seed(seed)
    # gpu 연산 무작위 고정
    torch.cuba.munual_seed(seed)
    # cuba 라이브러리에서 Deterministic(결정론적)으로 예측하기
    # 예측에 대한 불확실성 제거
    torch.backends.cudnn.deterministic = True
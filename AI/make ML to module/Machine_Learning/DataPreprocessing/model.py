from lightgbm import LGBMClassifier
from 

def define_model():
    # 모델 정의
    modelV0 = LGBMClassifier(random_state=args.random_state)
    from sklearn.model_selection import KFold 
    # 교차검증
    kf = KFold(n_splits=5, shuffle=True, random_state=args.random_state)

    n_iter = 0
    for train_index, valid_index in kf.split(enc_tr):
        print(f'train_index: {train_index} / valid_index: {valid_index}')
        if n_iter == 3:
            break
    # print(f'{enc_tr.shape} / {y_tr.shape}')
    # modelV0.fit(enc_tr, y_tr)

def ㅁ():
    return 
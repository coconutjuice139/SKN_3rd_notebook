import easydict
from datetime import datetime

def make_easydict():
    args = easydict.EasyDict()

    # path 정보
    args.default_path = 'c:/dev/ML&DL/make ML to module/data/'
    args.train_csv = args.default_path + 'train.csv'
    args.test_csv = args.default_path + 'test.csv'
    args.default_submission_csv = args.default_path + 'submission.csv'

    args.submission_csv = 'submission_' + str(datetime.today())
    return args

if __name__ == '__main__':
    make_easydict()
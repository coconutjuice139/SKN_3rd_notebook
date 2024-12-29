import torch
import os

embedding_cache_file = "C:\\dev\\nejot\\DB_embedding\\1212_2차_embedding.pt"
specs_to_check = ["아틀라스 시더 향", "패출리 노트"]

if os.path.exists(embedding_cache_file):
    embedding_cache = torch.load(embedding_cache_file, map_location="cpu")
    for spec in specs_to_check:
        if spec in embedding_cache:
            print(f"'{spec}' 임베딩이 캐시에 존재합니다!")
        else:
            print(f"'{spec}' 임베딩을 캐시에서 찾을 수 없습니다.")
else:
    print(f"임베딩 캐시 파일 '{embedding_cache_file}'이 존재하지 않습니다.")
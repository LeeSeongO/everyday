
N = int(input())
movie = 666

while N:
    if "666" in str(movie):  # 영화 제목에 666이 있는지 체크, 있으면 N -= 1해서 다음 영화제목을 서치
        N -= 1

    movie += 1

print(movie - 1)

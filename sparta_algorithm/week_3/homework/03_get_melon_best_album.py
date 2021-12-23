"""
멜론에서 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시하려 한다.

노래는 인덱스 구분하며, 노래를 수록하는 기준은 다음과 같다.

속한 노래가 많이 재생된 장르를 먼저 수록한다.
장르 내에서 많이 재생된 노래를 먼저 수록한다
장르 내에서 재생 횟수가 같은 노래 중에서 고유 번호가 낮은 노래를 먼저 수록한다.

노래의 장르를 나타내는 문자열 배열 genres 와
노래별 재생 횟수를 나타내는 정수 배열 plays 가 주어질 때,
베스트 앨범에 들어갈 노래의 인덱스를 순서대로 반환하시오.
"""

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
# 결과로 [4, 1, 3, 0] 가 와야 한다.


def get_melon_best_album(genre_array, play_array):
    genre_total_play_dict = {}  # genre 마다 play 를 저장할 딕셔너리
    genre_index_play_array_dict = {}  # genre 마다 index 와 play 를 저장할 딕셔너리

    # range 로 돌리는 이유는 인덱스 값을 사용하기 위해서 range(len()) 형식으로 반복
    # enumerate() <- 인덱스를 포함해서 값을 반환하는 함수
    for i in range(len(genre_array)):

        # genre_total_play_dict 에 genre key 값이 있을때와 없을때의 처리
        # key 값이 없을때는 genre_total_play_dict[장르] = 밸류
        # genre_index_play_array_dict[장르] = [[인덱스, 밸류]]
        # key 값이 있는경우 genre_total_play_dict[key] += 밸류   // 키에 맞는 장르에 밸류값을 더해줌
        # genre_index_play_array_dict[장르].append([인덱스, 밸류])  장르안에 [인덱스, 밸류]값을 넣어줌
        if genre_array[i] not in genre_total_play_dict:
            genre_total_play_dict[genre_array[i]] = play_array[i]
            genre_index_play_array_dict[genre_array[i]] = [[i, play_array[i]]]
        else:
            genre_total_play_dict[genre_array[i]] += play_array[i]
            genre_index_play_array_dict[genre_array[i]].append([i, play_array[i]])

    print(genre_total_play_dict)
    print(genre_index_play_array_dict)

    # sorted(genre_total_play_dict.item() //<-- genre_total_play_dict 에 있는 모든 값들을 꺼냄
    # key=lambda item: item[1]  // <-- key 값 즉, key 를 기준으로 정렬하겠다는 의미
    # lambda item: item[1]  // 함수를 만들지 않고 함수처럼 사용가능한 람다, genre_total_play_dict 에서
    # 배열에 첫번째 리스트 ('classic', 1450)[1] 를 키 값으로 정렬하며 정렬 후 reverse=True 정렬한 값을 거꾸로 하겠다. 즉, 내림차순으로 만들겠다라는 뜻
    sorted_genre_total_play_array = sorted(genre_total_play_dict.items(), key=lambda item: item[1], reverse=True)
    print(sorted_genre_total_play_array)

    # index 와 play 값을 사용하기 위해 genre_index_play_array_dict 를 이용
    result = []

    # 정렬된 값중 토탈 값은 필요없고 정리된 장르 순서대로 호출
    for genre, _ in sorted_genre_total_play_array:
        # index 와 play 값을 사용하기 위해 genre_index_play_array_dict 를 이용 해서 index_play_array 변수에 리스트로 저장
        # 따로 저장하는 이유는 sorted 로 가공하기 위해서 이다.
        index_play_array = genre_index_play_array_dict[genre]
        # dict 에서 밸류 값만 저장했기 때문에 index_play_array = [1, 600], [4, 2500] < --
        # 위의 값에서 key 값은 play 을 기준으로 정렬할 것이기 때문에 item[1] <--
        sorted_by_play_and_index_play_index_array = sorted(index_play_array, key=lambda item: item[1], reverse=True)
        # 결과는 장르별 1, 2위 인덱스만 추출하는 것이기때문에 i > 1: 즉, 0, 1 두번 루프
        for i in range(len(sorted_by_play_and_index_play_index_array)):
            if i > 1:
                break
            result.append(sorted_by_play_and_index_play_index_array[i][0])
    return result


print(get_melon_best_album(genres, plays))
# print(get_melon_best_album(genres, plays))  # 결과로 [4, 1, 3, 0] 가 와야 합니다!
""" 다른 사람의 풀이
def solution(lottos, win_nums):

    rank=[6,6,5,4,3,2,1]

    cnt_0 = lottos.count(0)
    ans = 0

    for x in win_nums:
        if x in lottos:
            ans += 1

    return rank[cnt_0 + ans], rank[ans]

느낀점:
정말 간략하게 잘풀어냈다.. 생각도 못했던 count 메소드를 사용했고, 이 메소드를 사용함으로
다음 코드들이 정말 간결하게 잘나온 것 같아서 메소드를 잘 이용해야겠다라는 점

하지만 시간복잡도 면에서는 내 코드가 더 좋게 짜진 부분도 있지 않나 싶다. 예를 들어 lotto.count(0) 이 들어감으로써
정확한 로직은 찾아봐야겠지만 0을 찾기위해 lottos: list 전체를 보게되는 반복문 O(n)만큼의 시간복잡도를 한번 더 쓰기때문이다.
그리고 확장성부분 이 문제의 경우 확장된다는 언급은 없었지만 만약에 정답 길이가 늘어나게되면 순위도 변경될 가능성을 생각해보았다.
"""

"""
    문제의 규칙 
    1. 0의 최고 순위의 영향을 미친다.
    2. 

"""

def check_rank(lt, rk):
    if lt < rk:
        lt += 1
    return lt


def solution(lottos: list, win_nums: list) -> list:
    answer = []
    joker_count = 0
    lotto_matched_count = 0
    rank = len(win_nums)

    for num in lottos:
        if num == 0:
            joker_count += 1
            continue

        if num in win_nums:
            lotto_matched_count += 1

    # 예외 처리 하는 부분
    check = check_rank(rank - (lotto_matched_count + joker_count), rank)
    answer.append(check)

    check = check_rank(rank - lotto_matched_count, rank)
    answer.append(check)

    return answer


lotto_list = [[20, 2, 5, 6, 7, 8, 39], [44, 1, 0, 0, 31, 25], [0, 0, 0, 0, 0, 0], [20, 2, 5, 45, 7, 8, 39]]
win_num_list = [[20, 9, 3, 45, 4, 35, 1], [31, 10, 45, 1, 6, 19], [38, 19, 20, 40, 15, 25], [20, 9, 3, 45, 4, 35, 1]]

print(solution(lotto_list[3], win_num_list[3]))

# [44, 1, 0, 0, 31, 25]	[31, 10, 45, 1, 6, 19]	[3, 5]
# [0, 0, 0, 0, 0, 0]	[38, 19, 20, 40, 15, 25]	[1, 6]
# [45, 4, 35, 20, 3, 9]	[20, 9, 3, 45, 4, 35]	[1, 1]

# 1	6개 번호가 모두 일치
# 2	5개 번호가 일치
# 3	4개 번호가 일치
# 4	3개 번호가 일치
# 5	2개 번호가 일치
# 6(낙첨)	그 외

"""
프로그래머스 // 연습문제 //124 나라의 숫자 // 12899
"""


def solution(n: int) -> int:
    answer = ''
    while n:
        if n % 3:
            answer += str(n % 3)
            n //= 3
        else:
            answer += "4"
            n = n // 3 - 1
    return answer[::-1]


print(solution(4))

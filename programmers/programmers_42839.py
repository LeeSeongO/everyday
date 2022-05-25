"""
프로그래머스 / 완전탐색 / 소수 찾기 / 42839
"""
import itertools


def is_prime_number(num: int) -> bool:
    # 자연수에서 두 개 이상의 소수의 곲으로 이루어져 있는 수, 1과 소수를 제외한 수를 합성수라고 한다.
    # 따라서 num 은 sqrt(N)보다 작은 적어도 하나의 인수를 가지므로 sqrt(N)까지만 나누어보면 된다.
    if num >= 2:
        i = 2
        while i * i <= num:
            if num % i == 0:
                return False
            i += 1
        return True
    else:
        return False


def solution(numbers: str) -> int:
    answer = 0
    # 수열을 담은 공간
    numbers_case = []

    for i in range(1, len(numbers) + 1):
        # 리스트 합병
        numbers_case.extend(list(map(''.join, itertools.permutations(numbers, i))))

    # 리스트 안에 있는 수열들을 정수형으로 바꾸고 중복 제거한다.
    numbers_case = set(list(map(int, numbers_case)))

    for number in numbers_case:
        # 소수판별하는 함수
        if is_prime_number(number):
            answer += 1

    return answer


print(solution("011"))

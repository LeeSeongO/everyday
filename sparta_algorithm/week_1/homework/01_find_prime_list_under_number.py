"""
입력 값의 소수들을 나열하기

입력값보다 작은 값 전체를 cycle 돌려서 비교하는 것은 시간초과 및 효율성 없고,
그렇기 때문에 반복문을 돌리면 O(N)만큼의 시간이 들기때문에 수학적 지식인 에라토스테네스의 체를 이용한다.

에에라토스테네스의 체를 이용하면 O(N ** (1/2))이라고 할 수 있다.

"""

input = 20


def find_prime_list_under_number(number) -> list:
    # 에라토스테네의 체 초기화: number에서 받은 숫자만큼 배열을 boolean 타입으로 초기화 해준다
    prime_list = [True] * number

    # number의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    # sqrt란 Square Root의 줄임말이며, 예를들어 2라는 수를 제곱하면 4, 2는 4의 제곱근이라고 표현한다.
    # math.sqrt(number) == number ** 0.5 // math.sqrt()를 사용하기 위해선 import math 를 해주어야한다.
    m = int(number ** 0.5)  # int()로 변환하는 이유는 소수점을 버리기 위해서 이다.
    for i in range(2, m + 1):  # + 1하는 이유는 range(2, m)에서 m이 4이면 3까지만 반복하기때문에 + 1에서 4만큼 돌리기 위해서
        if prime_list[i]:  # i가 소수인 경우 prime_list[i] == True
            for j in range(i+i, number, i):  # i 이후 i 의 배수들을 False 판정
                prime_list[j] = False

    # 소수 목록 반환 시키기
    # 2부터 시작하는 이유는 1은 소수 값이 아니기때문에 2부터 반복문을 돌리면 결과를 도출한다.
    return [i for i in range(2, number) if prime_list[i]]


result = find_prime_list_under_number(input)
print(result)
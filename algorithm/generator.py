"""
기존의 함수는 return 구문을 맞닥뜨리면 값을 리턴하고 모든 함수의 동작을 종료하지만
yield는 제너레이터가 여기까지 실행 중이던 값을 내보낸다(사전적 의미 '양보하다')의미로,
중간값을 리턴한 다음 함수는 종료되지 않고 계속해서 맨 끝에 도달할 때까지 실행된다.

값을 추출할때는 next()를 사용하면 된다.
"""

def get_natural_number():
    n = 0
    while True:
        n += 1
        yield n


# 다음과 같이 여러 타입의 값을 하나의 함수에서 추출가능하다.
def generator():
    yield '1'
    yield 'string'
    yield 'True'


g1 = get_natural_number()
g2 = generator()
for _ in range(100):
    print(next(g1), end=' ')

print()
for _ in range(3):
    print(next(g2))
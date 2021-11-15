import sys

# range(레인지)
"""
아래의 코드에서 range()는 range 클래스를 리턴하며, for문에서 사용할 경우 내부적으로는
제너레이터의 next()를 호출하듯 매번 다음 숫자를 생성한다. 이전 버전(2.x버전)까지는
range()함수가 숫자를 미리 생성해서 리스트로 리턴하는 방식이었고 제너레이터를 리턴하는 방식은 xrange()라고 존재했었다.

for i in range(5):
    print(i, end=' ')

두 방식의 차이점은 크기가 큰 숫자를 생성할 때 미리 숫자를 생성하면 메모리를 숫자가 커질수록 많은 메모리를 잡아먹게되는데
제너레이터를 리턴하는 방식은 생성 조건만 정해두고 나중에 필요할 때 생성해서 꺼내 쓸 수 있다.
예를들어,

a = [n for n in range(1000000)]
b = range(1000000)
len(a) == len(b)를 비교하면 True가 나오는데

a는 이미 생성된 리스트값을 가지고있고, b는 생성해야 한다는 조건만 존재하기 때문에

sys.getsizeof(a)
sys.getsizeof(b)

메모리 점유율을 비교하면 제너레이터를 리턴하는 방식이 효율적이라는 것을 알 수 있다.
또한, 미리 생성하지 않은 값을 인덱스에 접근이 안될 거 같지만
인덱스로 접근 시에는 바로 생성하도록 구현되어있어 바로 접근이 가능하다.

ex) b[20]
"""


def range_test():
    a = [n for n in range(1000000)]
    b = range(1000000)

    print("len(a): {} \nlen(b): {}".format(len(a), len(b)))
    print("len(a) == len(b):", len(a) == len(b))
    print("sys.getsizeof(a):",sys.getsizeof(a))
    print("sys.getsizeof(b):",sys.getsizeof(b))
    print(b[20])
"""
코딩을 하다 보면 일단 코드의 전체 골격을 잡아 놓고 내부에서 처리할 내용은 차근차근 생각하며
만들겠다는 의도로 다음과 같이 코딩하는 경우가 있다.

class MyClass(objet):
    def method_a(self):

    def method_b(self):
        print("Method B")

c = MyClass()

위의 코드의 경우 method_a()가 아무런 처리를 하지 않았기 때문에 엉뚱한 method_b()에서 오류가 발생할 수 있는데
이런 경우 다음과 같이 pass를 method_a()함수에 넣어주어 처리할 수 있다.
"""


# 파이썬에서 pass는 널 연산(Null Operation)으로 아무것도 하지 않는 기능이다.
class MyClass(object):
    def method_a(self):
        pass

    def method_b(self):
        print("Method B")


c = MyClass()
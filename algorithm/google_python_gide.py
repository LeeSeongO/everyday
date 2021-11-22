"""
PEP 8에는 인덴트는 공백 4칸으로 한다든지 등의 여러 가지 지침이 포함되어 있다.
특히 가독성을 높이기 위한 지침들이 많고, 이 주제는 '코딩 스타일'과도 잘 부합하는 주제이다

함수의 기본 값으로 가변 객체(Mutable Objet)를 사용하지 않아야 한다. 함수가 객체를 수정하면
(리스트에 아이템을 추가한다든지 등) 기본값이 변경되기 떄문이다. 따라서 다음과 같이 기본값으로
[]나 {}를 사용하는 것은 지양해야 한다.

def foo(a, b=[]):
    pass


def foo(a, b: mapping = {}):
    pass

대신 다음과 같이 불변 객체(immutable Object)를 사용한다. None을 명시적으로 할당하는 것도 좋은 방법이다.

def foo(a, b=None):
    if b is None:
        b = []


def foo(a, b: Optional[sequence] = None):
    if b is None:
        b = []
"""

"""
True, False를 판별할 때는 암시적(implicit)인 방법을 사용하는 편이 간결하고 가독성이 높다.
굳이 False임을 if foo != []: 같은 형태로 판별할 필요가 없다. if foo:로 충분하다.

if len(users) == 0:  # 길이가 없다는 뜻이며 가독성을 높이려면 not users로 충분
    print('no users')
    
if foo is not None and not foo:
    self.handle_zero()
    
    # 정수를 처리할 때는 암시적으로 거짓 여부를 판별하기보다는 정수값을 직접 비교하는 편이 덜 위험하다.
    
if not i % 10:
    self.handle_multiple_of_ten()

위의 코드를 수정해보면

if not users:
    print('no users')
    
if foo == 0:
    self.handle_zero()
    
if i % 10 == 0:
    self.handle_multiple_of_ten()

"""


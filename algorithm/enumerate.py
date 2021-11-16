"""
enumerate()는 '열거하다'라는 뜻의 함수로, 여러 가지 자료형(list, tuple. set 등)을 인덱스를 포함시켜
enumerate객체로 리턴한다.
"""

a = [1, 2, 3, 5, 9, 10]
print(a)
print(enumerate(a))
print(list(enumerate(a)))

# a = ['a1', 'b2', 'c3']가 있을 때 이 리스트의 인덱스와 값을 함께 출력하기
# 방식1
for i in range(len(a)):
    print(i, a[i])

# 위의 코드를 range()를 사용하지 않고, 깔끔하게 구현
i = 0
for v in a:
    print(i, v)
    i += 1

# 위의 코드 또한, 값은 깔끔하게 처리했으나 이 경우 인덱스를 위한 변수를 별도로 관리하는 형태라 이 또한 깔끔하지 않다.
# 까장 깔끔한 방식은 다음과 같이 enumerate()를 활용한 방법이다.
for i, v in enumerate(a):
    print(i, v)
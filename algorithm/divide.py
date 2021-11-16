"""
파이썬 2 이하에서 기본 나눗셈 연산자 /는 타입을 유지하는 특성 때문에 실수하기가 쉬웠다. 다음과 같이 5 / 3을 했을 때 우리가 기대하는
결과는 파이썬 3 이상에서 1.666이지만 파이썬 2 이하 버전에서는 정수형을 유지했었다.
"""

print("# 나눗셈")
divide = 5 / 3
print(divide)
print(type(divide))

divide_int1 = 5 // 3
print(divide_int1)
print(type(divide_int1))

divide_int2 = int(5 / 3)
print(divide_int2)
print(type(divide_int2))
print()

# 나머지
print("# 나머지")
remainder = 5 % 3
print(remainder)
print()

# 몫과 나머지
print("# 몫과 나머지를 한번에 구하기")
a = divmod(5, 3)
print(a)
print(list(a))
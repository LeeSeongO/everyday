"""
딕셔너리의 주요 연산 시간 복잡도
len(a) 요소의 개수를 리턴한다. O(1)
a[key] 키를 조회하여 값을 리턴한다. O(1)
a[key] = value 키/값을 삽입한다. O(1)
key in a a 딕셔너리에 key 값이 있는지 확인한다. O(1)
파이썬 3.7 내부적으로 인덱스를 이용해 입력 순서를 유지하지만.
3.6 이하 버전을 사용하는 곳은 입력 순서가 유지되지 않아 collections.OrderedDict()라는 별도의 자료형을 제공했다.

코테시 주의사항은 인터프리터의 버전이 확실하지 않으므로 이점을 주의해야한다.
"""
import collections

a = dict()  # a = {}

a = {
    "key1": "value1",
    "key2": "value2"
}

a["key3"] = "value3"

print(a["key1"])

try:
    print(a["key4"])

except KeyError:  # 존재하지 않는 키값을 조회하면 KeyError 에러가 발생할때 예외처리 하는 방법
    print("존재하지 않는 키")

print('key' in a)

"""
collections.defaultdict, collections.Counter, collections.OrderedDict 정리

collections.defaultdict(int) 로 딕셔너리를 선언하면 존재하지 않는 키 값 KeyError 를 발생시키지 않고 0으로 생성해준다.
"""

b = collections.defaultdict(int)

print(type(b), type(a))

b['a'] += 1
print(b['a'], b['b'])

if 'key4' in a:
    print('존재하는 키')
else:
    print('존재하지 않는 키 ')

for k, v in a.items():  # items() 메소드를 이용하면 키와 값을 각각 꺼내올 수 있다.
    print(k, v)

"""
Counter 객체
Counter 객체는 아이템에 대한 개수를 계산해 딕셔너리로 리턴하며, 다음과 같이 사용한다.
"""

c = [1, 2, 3, 4, 5, 5, 5, 6, 6]
d = collections.Counter(c)
print(d)  # Counter({5: 3, 6: 2, 1: 1, 2: 1, 3: 1, 4: 1})

"""
위와 같이 해당 아이템의 개수가 들어간 딕셔너리를 생성하고, 실제로는 딕셔너리를 생성한 것을 한 번 더 래핑(Wrapping)한
collections.Counter 클래스를 갖는다.

Counter 객체에서 가장 빈도 수가 높은 요소는 most_common()을 사용하면 된다.
b.most_common(2) <-- 뜻은 b collections.Counter 클래스에서 빈도수가 높은 2개를 가져오라는 뜻이다.
"""

# print(b.most_common(2))  # 일반 dict 클래스는 오류가 생긴다. 오류 내용으로 확인해보니 collections.Counter 에서만 작동하는 속성이다.
# 확인 작업
i = collections.defaultdict(int)
"""
당연하다고 생각될 수 있지만 i를 defaultdict 로 선언후 일반적인 dict 형식으로 넣어주면 i 의 type 은 defaultdict 가 아닌 dict 자료형이 된다.

# i = {
#     '5': 1,
#     '4': 2,
# }

"""
i[3] = 1
# print(i.most_common(1))
i = collections.Counter(i)
print(i.most_common(1))

"""
위에서 언급했지만 dict 는 python 3.6 이하 버전에서는 입력 순서가 유지되지 않는다. 그러므로
OrderedDict 라는 별도의 객체를 제공했었다.

"""

g = collections.OrderedDict({
    'banana': 3,
    'apple': 4
})

print(g)





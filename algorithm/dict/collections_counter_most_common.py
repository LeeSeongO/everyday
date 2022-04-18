import collections

c = [1, 2, 3, 4, 5, 5, 5, 6, 6]

temp = collections.Counter(c)

# Counter({5: 3, 6: 2, 1: 1, 2: 1, 3: 1, 4: 1})
print(temp)

# temp Counter 객체에서 가장 빈도 수가 높은 요소 추출할떈 most_common 을 사용한다.
print(temp.most_common(1)[0][1])


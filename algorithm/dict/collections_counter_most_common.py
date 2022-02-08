import collections

c = [1, 2, 3, 4, 5, 5, 5, 6, 6]

temp = collections.Counter(c)

# Counter({5: 3, 6: 2, 1: 1, 2: 1, 3: 1, 4: 1})
print(temp)


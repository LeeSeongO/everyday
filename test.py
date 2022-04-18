import collections

a = collections.defaultdict(int)

a['A'] = 5
a['B'] = 4

b = {
    'B': 5,
    'A': 4
}

print(a['C'])
print(a)
print(b)
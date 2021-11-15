from algorithm import type_hint as th, \
    list_comprehension, \
    generator, \
    range

# range(레인지)
"""
range.range_test()
"""

# generator(제너레이터)
"""
g1 = generator.get_natural_number()
for _ in range(0, 100):
    print(next(g1))

g2 = generator.generator()
print('\n'.join("{}{}{}".format(next(g2), next(g2), next(g2))))
"""

# list_comprehension(리스트 컴프리헨션)
original_dict = {
    "철1": 80,
    "영1": 70
}
original_list = [(10, 20), (30, 40)]

# original_list = list_comprehension.list_comprehension(original_list)
print(original_list)
print(dict(original_list))

# type_hint(타입 힌트)
"""
print(th.type_hint(3))
"""
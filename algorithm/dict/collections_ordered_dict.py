"""
파이썬 3.6 이하에서는 딕셔너리가 입력 순서가 유지가 되지않아서 collections.OrderedDict 를 사용해야지만 순서를 유지할 수 있다.
그 이후 버전인 3.7부터는 딕셔너리 내부적으로 인덱스를 이용하며 입력 순서가 유지되도록 개선이 되었다.
"""

import collections

a = collections.OrderedDict()

a['A'] = 3
a['B'] = 4

print(a)
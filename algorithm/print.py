"""
print('A1', 'B2')의 출력인 A1 B2에서 스페이스 공백 부분을 sep파라미터로 구분자를 콤마(,)로 지정해줄 수 있다.
"""
print('A1', 'B2', sep=', ')

"""
print()함수는 기본적으로 줄바꿈을 포함하는데 end파라미터로 변경할 수 있다.
"""
print('A1', end=', ')
print('B2')

"""
리스트를 출력할 때는 join()으로 묶어서 처리한다.
"""
a = ['A1', 'B2']
print(', '.join(a))

"""
idx 값에 1을 더해서 fruit와 함께 출력하는 방법은?
"""
idx = 1
fruit = "Apple"

# 인덱스를 지정한 형태
print('{0}: {1}'.format(idx + 1, fruit))

# 인덱스를 생략한 형태
print('{}: {}'.format(idx + 1, fruit))

# 마지막으로 f-string(formated string literal)
"""
변수를 뒤에 별도로 부여할 필요 없이 마치 템플릿을 사용하듯 인라인으로 삽입할 수 있어 편리하고,
무엇보다 .format을 부여하는 방식에 비해 훨씬 갈결하고 직관적이며 속도도 빠르다.
"""
print(f'{idx + 1}: {fruit}')
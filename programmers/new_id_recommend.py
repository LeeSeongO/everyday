import re


def solution(new_id):
    answer = new_id.lower()
    answer = re.sub(r'[^a-z0-9-_.]', '', answer)
    print(answer)
    answer = re.sub('[\.]{2,}', '.', answer)
    print(answer)
    return answer


nick_name = '...!@BaT#*..y.abcdefghijklm.'

print(solution(nick_name))
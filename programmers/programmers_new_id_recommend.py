"""
    문제
    https://programmers.co.kr/learn/courses/30/lessons/72410?language=python3
"""

import re

def solution(new_id):
    answer = ''

    # 1단계 new_id 의 모든 대문자를 대응되는 소문자로 치환합니다.
    new_id = new_id.lower()

    # 2단계 new_id 에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 문자를 제거합니다.
    new_id = re.sub("[^0-9a-zA-Z[-][_][.]]", " ", new_id)

    print(new_id)

    return answer


temp_id = input('신규 아이디 입력:')
recommend_id = solution(temp_id)

print(recommend_id)

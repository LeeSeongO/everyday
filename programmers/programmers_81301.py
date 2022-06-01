"""
프로그래머스 // 카카오 // 숫자 문자열과 영단어 //81301
"""

import re


def solution(s: str) -> int:
    answer = s[:]

    english_word = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    # zero 부터 nine 까지 | 로 묶어서 패턴
    reg_exp = re.compile('|'.join(map(str, english_word)))
    # 문자열에 존재하는 영단어를 list 로 반환
    word_list = reg_exp.findall(answer)

    # list 를 re.sub 를 이용해서 치환한다.
    # 주의할점: 치환할때 숫자는 안된다. 그래서 dict 의 value 값을 문자로 바꾸어줌.
    for word in word_list:
        # 패턴, 바꿀 문자열, 문자열
        answer = re.sub(word, english_word[word], answer)

    return int(answer)


s_string = ['one4seveneight', '1234o']
print(solution(s_string[0]))

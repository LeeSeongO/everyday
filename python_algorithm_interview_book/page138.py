"""
유효한 팰린드롬

문제.
주어진 문자열이 팰린드롬인지 아닌지 확인하라. 대소문자 구분하지 않으며, 영문자와 숫자만 대상으로 한다.

입력
"A man, a plan, a canal: Panama"
출력
True

입력
"race a car"
출력
False

"""


# 영문 대소문자를 구분하지않기때문에 대문자 or 소문자로 모든 문자를 변환시킨다.

temp = "A man, a plan, a canal: Panama"


def is_palindrome1(s: str) -> bool:
    strs = []
    for char in s:
        # 문자가 영문 또는 숫자인지 확인
        if char.isalnum():
            # 만들어 놓은 배열에 소문자로 변환해서 str 배열 끝부분에 추가한다.
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False

    return True


print(is_palindrome1(temp))

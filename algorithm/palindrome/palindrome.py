"""
palindrome(팰린드롬)
앞뒤가 똑같은 단어나 문장으로, 뒤집어도 같은 말이 되는 단어 또는 문장을 팰린드롬이라고 한다. 우리말로는 '회문'이라 부른다.

def isPalindrome - 리스트로 list.pop(0) <-- 시간복잡도 O(n)보다
def isPalindrome2 - 데크 deque.popleft() <-- 시간복잡도 O(1)이 더 빠르다.
def isPalindrome3 - 정규식을 이용한 슬라이싱 사용

속도 순위
1등 정규식을 이용 슬라이싱
2등 데크사용
3등 리스트

"""

import collections, re
from typing import Deque


# 리스트로 변환한 풀이.


class Palindrome:
    def isPalindrome(self, s: str) -> bool:
        strs = []
        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        # 팰린드롬 여부 판별
        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                return False

        return True

    def isPalindrome2(self, s: str) -> bool:
        # 자료형 데크로 선언
        strs: Deque = collections.deque()

        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False

        return True

    def isPalindrome3(self, s: str) -> bool:
        s = s.lower()
        # 정규식으로 불필요한 문자 필터링
        # 첫번째 인자에는 [] 는 정규식을 넣고 {} 추출할 개수
        # 두번째 인자에는 추출할 개수를 어떤식으로 표현할지
        # 세번쨰 인자에는 치환 문자 즉 검열할 문자열을 넣는다
        s = re.sub('[^a-z0-9]', '', s)

        return s == s[::-1]  # 슬라이싱


test_list = []


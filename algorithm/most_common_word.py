"""
가장 흔한 단어

금지어 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라. 대소문자 구분을 하지 않으며, 구두점(마침표, 쉼표 등) 또한 무시한다.

입력:
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

출력:
"ball"
"""
import collections
from typing import List
import re


class MostCommonWord:
    def most_common_word(self, _paragraph: str, _banned: List[str]) -> str:
        # 정규식에서 ' ' 하는 이유는 구두점을 띄우기 위함도 있지만 공백도 공백으로 남기기 위해서 치환 문자열을 ' '으로 처리해야 한다.
        # re.sub(r'[^\w^\s]', '', _paragraph) 도 가능하다!
        words = [word for word in re.sub(r'[^\w]', ' ', _paragraph)
                 .lower().split()
                 if word not in _banned]

        # coleections 모듈에 Counter 을 통해 단어별로 카운터해서 분류 할 수 있다.
        # {'ball': 2, 'bob': 1, 'a': 1, 'the': 1, 'flew': 1, 'far': 1, 'after': 1, 'it': 1, 'was': 1}
        counts = collections.Counter(words)

        # 가장 빈도수가 높은 단어 첫번째를 리턴한다.
        # counts.most_common(1) -> [('ball', 2)] 로 반환 그렇기 때문에 [0][0] 으로 접근해 단어를 뽑아준다.
        print(counts.most_common(1))
        return counts.most_common(1)[0][0]


paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

most_common_word = MostCommonWord()
print(most_common_word.most_common_word(paragraph, banned))


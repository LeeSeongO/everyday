import collections
from typing import List

"""
문자열 배열을 받아 애너그램 단위로 그룹핑하라.
["eat", "tea", "tan", "ate", "nat", "bat"]
"""


class GroupAnagrams:
    def group_anagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)

        # 문자열을 꺼내서 오름 차순으로 정리를 하게 되면 문자열을 문자들의 배열이기때문에 배열로 쪼개지기 때문에
        # join으로 다시 합쳐주는 과정이 필요하다. 그중 같은 단어들로 이루어 져있으면 append(word)를 하고,
        # 새로운 단어가 들어오면 defaultdict(list)로 만들어놓았기 때문에 새로운 단어가 키값에 append(word)가 된다..
        for word in strs:
            # 정렬하여 딕셔너리에 추가.
            anagrams[''.join(sorted(word))].append(word)

        return list(anagrams.values())


list_a = ["eat", "tea", "tan", "ate", "nat", "bat"]
anagrams = GroupAnagrams()
print(anagrams.group_anagrams(list_a))

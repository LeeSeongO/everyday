import collections


def groupAnagrams(strs: list[str]) -> list[list[str]]:
    anagrams = collections.defaultdict(list)

    for word in strs:
        # 정렬하여 딕셔너리에 추가
        anagrams[''.join(sorted(word))].append(word)
    return list(anagrams.values())


group_list = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']

print(groupAnagrams(group_list))
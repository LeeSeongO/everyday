import collections


def solution(participant, completion):
    answer = dict(collections.Counter(participant)) - dict(collections.Counter(completion))
    return list(answer.keys())[0]

participant_list = ["mislav", "stanko", "mislav", "ana"]
completion_list = ["stanko", "ana", "mislav"]

temp = solution(participant_list, completion_list)

print(type(temp))
# 누가 신고를 몇번당했는지

def solution(id_list, report, k):
    answer = [0 for _ in range(len(id_list))]
    count_report_list = [[0, ''] for _ in range(len(id_list))]

    # 중복 제거하는 부분
    report_set = set(report)

    for rp in report_set:
        # rp 에는 어떤값? muzi frodo
        temp_split = rp.split()

        # 신고당한 사람 id_list ['muzi', 'frodo', 'apeach', 'neo']
        reported_user = id_list.index(temp_split[1])

        # 신고당한 사람의 신고 카운트, 신고한 유저 목록
        reported_user_list = count_report_list[reported_user]

        # 신고당한 횟수 저장
        reported_user_list[0] += 1

        # 신고한 유저 목록을 저장
        if reported_user_list[1] == '':
            reported_user_list[1] = temp_split[0]
        else:
            reported_user_list[1] += ' ' + temp_split[0]

    for i in count_report_list:
        if i[0] >= k:
            # [apeach, muzi]
            report_user_list = i[1].split()

            for user in report_user_list:
                answer[id_list.index(user)] += 1

    return answer


a = ['muzi', 'frodo', 'apeach', 'neo']
b = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi", "muzi neo"]
c = 2
print(solution(a, b, c))
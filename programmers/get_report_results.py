# 이용자의 ID가 담긴 id_list, 각이용자가 신고한 이용자의 ID 정보가 담긴 문자열 배열 report, 정지 기준이 되는 신고 횟수 k

# 1. 정답을 만들 공간을 만들어주기.
# 2. 신고당한 유저의 인덱스에 count 값과, 신고한 유저 목록을 저장하는 리스트
# 혹시 중복된 값이 존재할 수 있으므로 중복된 값을 처리 함.
# 3. 2번의 count 값이 k 와 비교해서 크거나 같을때 신고한 유저 목록들의 answer 값을 1씩 증가 시키기.

def solution(id_list, report, k):
    answer = [0 for _ in range(len(id_list))]
    count_report_list = [[0, ''] for _ in range(len(id_list))]

    # 같은 유저를 여러번 했을 경우 1번만 되기 위해 중복 제거
    report_set = set(report)

    for rp in report_set:
        temp_split = rp.split(' ')

        # 신고당한 사람
        reported_user = id_list.index(temp_split[1])

        # 신고당한 사람의 신고횟수, 신고한 유저 목록
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
            report_user_list = i[1].split(' ')

            for user in report_user_list:
                answer[id_list.index(user)] += 1

    return answer


a = ['muzi', 'frodo', 'apeach', 'neo']
b = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi", "muzi neo"]
c = 2

print(solution(a, b, c))
"""
프로그래머스 // 카카오 // 추석 트래픽 // 17676
"""

from typing import List


def solution(lines: List[str]) -> int:
    answer = 0
    log = []  # log의 (시작시간, 끝시간) 저장

    for line in lines:
        date, s, t = line.split()  # 날짜, 응답완료시간, 처리시간 ex) 2016-09-15 20:59:57.421 0.351s
        s = s.split(':')

        end = int((int(s[0]) * 3600 + int(s[1]) * 60 + float(s[2])) * 1000)  # 끝시간을 msec 단위로 저장
        start = int(end - float(t[:-1]) * 1000 + 1)  # 시작 시간을 msec 단위로 저장
        log.append([start, end])

    for x in log:
      # 최대 초당 처리량 구하기
        answer = max(answer, throughput(log, x[0], x[0] + 1000), throughput(log, x[1], x[1] + 1000))

    return answer


# 초당 처리량을 구하는 함수
def throughput(log, start, end):
    cnt = 0
    for x in log:
        if x[0] < end and x[1] >= start:
            cnt += 1
    return cnt

    # def solution(lines: List[str]) -> int:
    #     answer = 0
    #     start_time = []
    #     end_time = []
    #
    #     for t in lines:
    #         time = t.split()
    #         start_time.append(get_start_time(time[1], time[2]))
    #         end_time.append(get_time(time[1]))
    #     for i in range(len(lines)):
    #         cnt = 0
    #         cur_end_time = end_time[i]
    #
    #         # i번째는 현재 자신의 시작시간이고, i 이하는 그 이전의 시작시간이므로 카운트 할 필요가 없다.
    #         for j in range(i, len(lines)):
    #             if cur_end_time > start_time[j] - 1000:
    #                 cnt += 1
    #         answer = max(answer, cnt)
    #     return answer
    #
    #
    # def get_time(time):
    #     time_temp = time.split(':')
    #     hour = int(time_temp[0]) * 3600
    #     minute = int(time_temp[1]) * 60
    #     second = int(time_temp[2][:2])
    #     millisecond = int(time_temp[2][3:])
    #     return (hour + minute + second) * 1000 + millisecond
    #
    #
    # def get_start_time(time, duration_time):
    #     # s 를 제거하기 위해 -1 인덱스까지 복사해서 n_time 에 넣는다.
    #     n_time = duration_time[:-1]
    #     int_duration_time = int(float(n_time) * 1000)
    # return get_time(time) - int_duration_time + 1


lines_temp = ["2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s", "2016-09-15 20:59:58.299 0.8s",
              "2016-09-15 20:59:58.688 1.041s", "2016-09-15 20:59:59.591 1.412s", "2016-09-15 21:00:00.464 1.466s",
              "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s", "2016-09-15 21:00:00.966 0.381s",
              "2016-09-15 21:00:02.066 2.62s"]
lines_temp1 = ["2016-09-15 00:00:00.000 3s"]

print(solution(lines_temp))

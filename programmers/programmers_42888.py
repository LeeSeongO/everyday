"""
프로그래머스 // KAKAO BLIND // 오픈 채팅방 // 42888
"""
from typing import List


def solution(record: List[str]):
    answer = []
    nickname = {}
    command = {
        'Enter': '님이 들어왔습니다.',
        'Leave': '님이 나갔습니다.'
    }

    # Enter, Change - nickname 이 변경되는 커맨드를 먼저 처리해준다
    for r in record:
        r_split = r.split()
        if r_split[0] in ["Enter", "Change"]:
            nickname[r_split[1]] = r_split[2]

    # Change 를 제외하고 answer.append 처리
    for r in record:
        r_split = r.split()
        if r_split[0] != "Change":
            answer.append(nickname[r_split[1]] + command[r_split[0]])

    return answer


record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]
print(solution(record))


"""
from typing import List


def solution(record: List[str]) -> List[str]:
    answer = []
    
    # {user_id: {nickname: str, index_command: []}}
    record_dict = {}
    
    for user_info in record:
        enter = "님이 들어왔습니다."
        leave = "님이 나갔습니다."
        
        # Enter, Change: 0 - command, 1 - user_id, 2 - nickname // Leave: 0 - command, 1 - user_id
        user_info_split = user_info.split()
        
        if user_info_split[0] == "Enter":
            # 처음 입장
            if user_info_split[1] not in record_dict:
                record_dict[user_info_split[1]] = {
                    "nickname": user_info_split[2],
                    "index_command": [[len(answer), enter]]
                }
            # 두번째 입장이기 때문에 아이디 값이 변경되었으면 Change 처리 해야됨.
            else:
                if record_dict[user_info_split[1]]["nickname"] != user_info_split[2]:
                    record_dict[user_info_split[1]]["nickname"] = user_info_split[2]
                    for i, command in record_dict[user_info_split[1]]["index_command"]:
                        answer[i] = record_dict[user_info_split[1]]["nickname"] + command
                    
                record_dict[user_info_split[1]]["index_command"].append([len(answer), enter])
                
            answer.append(user_info_split[2] + enter)
            
        elif user_info_split[0] == "Leave":
            record_dict[user_info_split[1]]["index_command"].append([len(answer), leave])
            answer.append(record_dict[user_info_split[1]]["nickname"] + leave)
            
        else:
            for i, command in record_dict[user_info_split[1]]["index_command"]:
                record_dict[user_info_split[1]]["nickname"] = user_info_split[2]
                answer[i] = record_dict[user_info_split[1]]["nickname"] + command
            
    return answer
"""
"""
다리를 지나는 트럭
문제 설명
트럭 여러 대가 강을 가로지르는 일차선 다리를 정해진 순으로 건너려 합니다. 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 알아내야 합니다. 다리에는 트럭이 최대 bridge_length대 올라갈 수 있으며, 다리는 weight 이하까지의 무게를 견딜 수 있습니다. 단, 다리에 완전히 오르지 않은 트럭의 무게는 무시합니다.

예를 들어, 트럭 2대가 올라갈 수 있고 무게를 10kg까지 견디는 다리가 있습니다. 무게가 [7, 4, 5, 6]kg인 트럭이 순서대로 최단 시간 안에 다리를 건너려면 다음과 같이 건너야 합니다.

경과 시간	다리를 지난 트럭	다리를 건너는 트럭	대기 트럭
0	[]	[]	[7,4,5,6]
1~2	[]	[7]	[4,5,6]
3	[7]	[4]	[5,6]
4	[7]	[4,5]	[6]
5	[7,4]	[5]	[6]
6~7	[7,4,5]	[6]	[]
8	[7,4,5,6]	[]	[]
따라서, 모든 트럭이 다리를 지나려면 최소 8초가 걸립니다.

solution 함수의 매개변수로 다리에 올라갈 수 있는 트럭 수 bridge_length, 다리가 견딜 수 있는 무게 weight, 트럭 별 무게 truck_weights가 주어집니다. 이때 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 return 하도록 solution 함수를 완성하세요.

제한 조건
bridge_length는 1 이상 10,000 이하입니다.
weight는 1 이상 10,000 이하입니다.
truck_weights의 길이는 1 이상 10,000 이하입니다.
모든 트럭의 무게는 1 이상 weight 이하입니다.
입출력 예
bridge_length	weight	truck_weights	return
2	10	[7,4,5,6]	8
100	100	[10]	101
100	100	[10,10,10,10,10,10,10,10,10,10]	110

"""

from typing import List
from collections import deque


def solution(bridge_length: int, weight: int, truck_weights: List[int]) -> int:
    answer = 0
    truck_weights_deque = deque(truck_weights)
    
    # 현재 다리위의 무게 큐
    current_bridge_weight_deque = deque([0] * bridge_length)

    # 현재 다리위의 무게
    current_bridge_weight = 0

    while len(current_bridge_weight_deque):
        answer += 1
        # 1초가 지났기 때문에 현재 다리 위의 무게에서 popleft 한값을 minus 처리
        current_bridge_weight -= current_bridge_weight_deque.popleft()

        # 대기 중인 트럭 큐가 비어있는지 확인
        if truck_weights_deque:
            # 다리위의 무게 + 다음 대기중인 트럭 1대의 값을 더해서 최대 무게랑 비교
            # True 면 대기중인 트럭 1대 append 하고, 현재 다리 위의 무게도 증가시켜준다.
            # False 무게 0을 append 해준다.
            # current_bridge_weight를 sum함수로 처리하려고했는데 시간복잡도 오류로 아래와 같이 처리
            if current_bridge_weight + truck_weights_deque[0] <= weight:
                current_bridge_weight_deque.append(truck_weights_deque.popleft())
                current_bridge_weight += current_bridge_weight_deque[-1]
            else:
                current_bridge_weight_deque.append(0)

    return answer


bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]

print(solution(bridge_length, weight, truck_weights))

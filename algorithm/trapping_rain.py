"""
높이를 입력받아 비 온 후 얼마나 많은 물이 쌓일 수 있는지 계산하라.

입력:
[0,1,0,2,1,0,1,3,2,1,2,1]
출력:
6
"""
from typing import List


# 투 포인터 방식 O(n), 스택 O(n) 실행 시간은 투포인터가 살짝 빠르다..
class TrappingRain:

    # 투 포인터를 활용
    def trappingRainTwoPointer(self, height: List[int]) -> int:
        # height: [] 리스트 값이 없을 경우 0을 반환한다.
        if not height:
            return 0

        volume = 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]

        # while 종료 조건 left 포인터가 right 포인터랑 같아지거나 넘어가면 종료
        while left < right:

            # 변경되는 최대 높이를 갱신
            left_max, right_max = max(height[left], left_max), \
                                  max(height[right], right_max)

            # 더 높은 쪽을 향해 투 포인터 이동
            # 양쪽 중 낮은 높이가 더 높은 쪽을 향해 이동하면서, 높이가 줄어들면 공간이 비는 것이므로,
            # volume 에 + 하도록 left_max - height[left] 릃 해준다.
            if left_max <= right_max:
                volume += left_max - height[left]
                left += 1
            else:
                volume += right_max - height[right]
                right -= 1

            print(volume)

        return volume

    def trappingRainStack(self, height: List[int]) -> int:
        stack = []
        volume = 0


        # 스택을 쌓아가면서 풀어야 하기 때문에 최대 크기만큼 반복
        for i in range(len(height)):

            # 변곡점을 만나는 경우
            # 스택에 값이 들어있으면서 현재 높이가 stack[-1] 인덱스 보다 높으면
            while stack and height[i] > height[stack[-1]]:

                # 스택에서 꺼낸다.
                top = stack.pop()

                # 예외처리
                if not len(stack):
                    break

                # 이전과의 차이만큼 물 높이 처리
                distance = i - stack[-1] - 1
                waters = min(height[i], height[stack[-1]]) - height[top]

                volume += distance * waters

            stack.append(i)

        return volume



height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

TrappingRain = TrappingRain()
TrappingRain.trappingRainTwoPointer(height)

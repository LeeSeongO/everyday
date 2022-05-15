"""
두수의 합
덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라.

입력
nums = [2, 7, 11, 15], target = 9

출력
[0, 1]

"""
from typing import List


class TwoSum:
    # 브루트 포스 방식
    # 정답을 찾기 위해서 0 번째 인덱스부터 마지막 인덱스까지 차례대로 비교하는 비효율적인 방식.
    def twoSumBF(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    # in을 이용한 탐색
    # target - 요소를 뺀 값이 List 안에 있는 지 확인하는 방식
    def twoSumIn(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            complement = target - n

            # return 값에 nums.index(n) 인덱스 번호, nums[i + 1:] <-- 에 찾았기때문에 index 에 i + 1 을 해준다.
            if complement in nums[i + 1:]:
                return [nums.index(n), nums[i + 1:].index(complement) + (i + 1)]

    def twoSumKey(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}

        # 키와 값을 바꿔서 딕셔너리로 저장
        for i, num in enumerate(nums):
            nums_map[num] = i

        # 타겟에서 첫 번째 수를 뺀 결과를 키로 조회
        # target - num(key값) 이 nums_map 에 키값으로 있는지 확인하고,
        # 키값이 있을시에 자기자신을 더한게 아닌지 예외적인 부분을 nums_map[target - num] 조건으로 처리해준다.
        # 조건이 맞다면 i 와 nums_map[target - num] 를 반환시켜준다.
        for i, num in enumerate(nums):
            if target - num in nums_map and i != nums_map[target - num]:
                return [i, nums_map[target - num]]

    # twoSumKey 를 반복문 하나에서 코드를 조금 더 간결하게 처리하는 방식
    # target - num 한 값을 nums_map 에 찾아서 없으면 nums_map[num] 에 값을 입력, 있다면 출력
    def twoSumKey2(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}

        for i, num in enumerate(nums):
            if target - num in nums_map:
                return [nums_map[target - num], i]
            nums_map[num] = i

    # 투 포인터 방식
    # 이 방식을 사용할때 주의 할 점은 List 안에 있는 숫자들이 오름차순으로 정렬이 되어있어야 한다.
    def twoSumTP(self, nums: List[int], target: int) -> List[int]:
        # 양쪽 끝을 포인터로 생성
        left, right = 0, len(nums) - 1

        # 왼쪽 포인터와 오른쪽 포인터가 같은 위치에 있으면 종료
        while not left == right:
            # 합이 타겟보다 작으면 왼쪽 포인터를 오른쪽으로
            if nums[left] + nums[right] < target:
                left += 1
            # 합이 타겟보다 크면 오른쪽 포인터를 왼쪽으로
            elif nums[left] + nums[right] > target:
                right -= 1

            else:
                return [left, right]






nums = [2, 7, 11, 15]
target = 9

TwoSum = TwoSum()
print(TwoSum.twoSumKey2(nums, target))
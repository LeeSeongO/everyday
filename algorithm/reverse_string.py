
from typing import List

class reverse_string:
    """
    투 포인터(two pointer)를 이용한 스왑
    단어 그대로 2개의 포인터를 이용해 범위를 조정해가며 풀이하는 방식

    """
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

    """
    파이썬다운 방식
    
    s = s[::-1] 도 가능하지만 리트코드에서는 오류가 발생한다.
    원래는 정상적으론 처리가 되어야 하지만 공간 복잡도를 O(1)로 제한하다 보니
    처리하는 데 다소 제약이 있다. 이런 경우는
    s[:] = s[::-1]로 해결하면 된다.
    
    속도 순위
    1. 파이썬다운 방식
    2. 투 포인터를 이용한 스왑
    미묘한 차이로 파이썬다운 방식이 빠르다
    """
    def reverseString1(self, s: List[str]) -> None:
        s.reverse()


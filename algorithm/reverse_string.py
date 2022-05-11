from typing import List


class ReverseString:
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

    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters, digits = [], []
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)

        # 1개의 키를 람다 표현식으로 정렬
        # 식별자는 순서에 영향을 끼치지 않지만, 문자가 동일할 경우 식별자 순으로 한다. 라는 조건때문에 2개의 키를 사용해서 정렬해야 한다.
        temp_letters = sorted(letters, key=lambda x: x.split()[1:])
        print(temp_letters)

        # 2개의 키를 람다 표현식으로 정렬
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return letters + digits


logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]


Class_log = ReverseString()

print(Class_log.reorderLogFiles(logs))



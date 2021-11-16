
"""
# 대충 만든 변수명과 주석을 달지 않은 경우

def num_matching_subseq(self, s: str, words: list[str]) -> int:
    a = 0
    for b in words:
        c = 0
        for i in range(len(b)):
            d = s[c:].find(b[i])
            if d < 0:
                a -= 1
                break
            else:
                c += d + 1
        a += 1

    return a

"""


# 위의 코드를 수정한 경우
def num_matching_subseq(self, s: str, words: list[str]) -> int:
    matched_count = 0

    for word in words:
        pos = 0
        for i in range(len(word)):
            # Find Matching position for each character.
            found_pos = s[pos:].find(word[i])
            if found_pos < 0:
                matched_count -= 1
                break
            else:
                # If found, take step position forward.
                pos += found_pos + 1
        matched_count += 1

    return matched_count

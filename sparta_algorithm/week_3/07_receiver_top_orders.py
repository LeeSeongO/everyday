"""
Question
주어진 리스트 맨 오른쪽 숫자부터 왼쪽으로 레이저를 발사할때
receive 하는 인덱스 넘버 구하기
"""


top_heights = [6, 9, 5, 7, 4]

def get_receiver_top_orders(heights):
    answer = [0] * len(heights)
    while heights:
        height = heights.pop()
        for idx in range(len(heights) - 1, 0, -1):
            if heights[idx] > height:
                answer[len(heights)] = idx + 1
                break;

    return answer


test = [0 for _ in range(5)]

print(test)

# get_receiver_top_orders(top_heights)
# print(get_receiver_top_orders(top_heights))
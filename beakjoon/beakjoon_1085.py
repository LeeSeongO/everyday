"""
한수는 지금 (x, y)에 있다. 직사각형은 각 변이 좌표축에 평행하고, 왼쪽 아래 꼭짓점은 (0, 0), 오른쪽 위 꼭짓점은 (w, h)에 있다.
직사각형의 경계선까지 가는 거리의 최솟값을 구하는 프로그램을 작성하시오.

첫째 줄에 x, y, w, h가 주어진다.
"""


# x, y, w, h 값을 입력
x, y, w, h = map(int, input().split())
if x - 0 < w - x:
    min_x = x - 0
else:
    min_x = w - x

if y - 0 < h - y:
    min_y = y - 0
else:
    min_y = h - y

# x로 갔을때 최솟값과 y로 갔을때 최솟값을 비교
print(min(min_x, min_y))

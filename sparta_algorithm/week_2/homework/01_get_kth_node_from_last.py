"""
참고사항으로 k가 링크드 리스트의 길이보다 크지 않은지 확인해야함
에러 처리는 right_node를 넣어주는 반복문에 처리를 해주면 될 것 같다.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def get_kth_node_from_last(self, k):
        left_cur = self.head  # 시작점 부터 탐색할 노드
        right_cur = self.head  # k만큼 떨어진 지점부터 탐색할 노드

        for _ in range(k - 1):  # k만큼 떨어진 노드를 입력해주는 루프
            right_cur = right_cur.next

        while right_cur.next is not None:  # right 노드가 마지막 노드에 닿을때까지 반복
            left_cur = left_cur.next
            right_cur = right_cur.next

        return left_cur


linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)

# [6] -> [7] -> [8]

print(linked_list.get_kth_node_from_last(2).data)  # 7이 나와야 합니다!
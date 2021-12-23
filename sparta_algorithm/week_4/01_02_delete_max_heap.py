class MaxHeap:
    def __init__(self):
        self.items = [None]

    def insert(self, value):
        self.items.append(value)
        cur_index = len(self.items) - 1

        while cur_index > 1:  # cur_index 가 1이 되면 정상을 찍은거라 다른 것과 비교 안하셔도 됩니다!
            parent_index = cur_index // 2
            if self.items[parent_index] < self.items[cur_index]:
                self.items[parent_index], self.items[cur_index] = self.items[cur_index], self.items[parent_index]
                cur_index = parent_index
            else:
                break

    def delete(self):
        """
        아래의 코드에는 전재 조건이 잘못 되었다. 예외처리 할 수 없음.
        while 문에서 지금 입력 값의 인덱스가 1인경우에도 생각을 해야함
        prev_max = self.items[1]
        self.items[1], self.items[-1] = self.items[-1], self.items[1]
        del self.items[-1]

        parent_node = 1
        child_node = parent_node * 2
        while self.items[parent_node] < self.items[child_node] or \
                self.items[parent_node] < self.items[child_node + 1]:
            if self.items[child_node] < self.items[child_node + 1]:
                self.items[parent_node], self.items[child_node + 1] = self.items[child_node + 1], self.items[
                    parent_node]
                parent_node = child_node + 1
                child_node = parent_node * 2
            else:
                self.items[parent_node], self.items[child_node] = self.items[child_node], self.items[parent_node]
                parent_node = child_node
                child_node = parent_node * 2

            if child_node > len(self.items) - 1:
                break

        return prev_max
        """
        # 1. 루트 노드와 맨 끝에 있는 노드를 교체한다.
        # 2. 맨 뒤에 있는 원소를 (원래 루트 노드)를 삭제한다. 이 때, 끝에 반환해줘야 하므로 저장
        # 3. 변경된 노드와 자식 노드들을 비교한다. 두 자식 중 더 큰 자식과 비교해서 자신보다 자식이 더 크다면 자리를 바꿈.
        # 4. 자식 노드들 보다 부모 노드가 더 크거나 가장 바닥에 도달할때 까지 3. 을 반복한다.
        # 5. 2에서 제거한 원래 노드를 반환한다.

        self.items[1], self.items[-1] = self.items[-1], self.items[1]
        prev_max = self.items.pop()

        cur_index = 1

        while cur_index <= len(self.items) - 1:
            left_child_index = cur_index * 2
            right_child_index = cur_index * 2 + 1
            max_index = cur_index

            # left_child_index <= len(self.items) - 1  // 실질적으로 접근하는 인덱스 이므로 -1처리를 하고
            # left_child_index 가 작거나 같아야 존재한다고 할 수 있다.
            if left_child_index <= len(self.items) - 1 and self.items[left_child_index] > self.items[max_index]:
                max_index = left_child_index

            if right_child_index <= len(self.items) -1 and self.items[right_child_index] > self.items[max_index]:
                max_index = right_child_index

            if max_index == cur_index:
                break

            self.item[cur_index], self.items[max_index] = self.items[max_index], self.items[cur_index]
            cur_index = max_index
        return prev_max



max_heap = MaxHeap()
max_heap.insert(8)
max_heap.insert(6)
max_heap.insert(7)
max_heap.insert(2)
max_heap.insert(5)
max_heap.insert(4)
print(max_heap.items)  # [None, 8, 6, 7, 2, 5, 4]
print(max_heap.delete())  # 8 을 반환해야 합니다!
print(max_heap.items)  # [None, 7, 6, 4, 2, 5]

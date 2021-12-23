class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        """
        head   tail
        [4] -> [2]
        self.tail.next = new_node
        self.tail = new_node
        """
        new_node = Node(value)

        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node
        self.tail = new_node

        return

    def dequeue(self):
        """
        head          tail
        [4] -> [2] -> [3]

        head  tail
        [2] -> [3]

        self.head 값이 지워질 값이고,

        while self.head.next == self.tail

        self.head.next 값이 self.tail 의 값이 끝값이기 때문 같을때까지 반복


        """
        if self.is_empty():
            return "Queue is Empty"
        delete_head = self.head
        self.head = self.head.next

        return delete_head.data

    def peek(self):
        if self.is_empty():
            return "Queue is Empty"
        else:
            return self.head.data

    def is_empty(self):
        return self.head is None


que = Queue()
que.enqueue(3)
print(que.peek())
que.enqueue(4)
print(que.peek())
que.enqueue(5)
print(que.peek())
print(que.dequeue())
print(que.peek())
print(que.dequeue())
print(que.dequeue())
print(que.dequeue())
print(que.is_empty())


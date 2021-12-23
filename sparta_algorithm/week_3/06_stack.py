class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        new_head = Node(value)
        new_head.next = self.head
        self.head = new_head
        return

    # pop 기능 구현
    def pop(self):
        if self.is_empty():
            return "Stack Is Empty"
        delete_node = self.head
        self.head = self.head.next
        return delete_node.data

    def peek(self):
        if self.is_empty():
            return "Stack Is Empty"

        return self.head.data

    # is_empty 기능 구현
    def is_empty(self):
        return self.head is None


stack = Stack()
stack.push(3)
print(stack.peek())
stack.push(4)
print(stack.peek())
print(stack.pop())

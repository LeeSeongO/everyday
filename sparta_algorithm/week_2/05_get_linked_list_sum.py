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


def _get_linked_list_sum(linked_list):
    linked_list_sum = 0
    head_1 = linked_list.head

    while head_1 is not None:
        linked_list_sum = linked_list_sum * 10 + head_1.data
        head_1 = head_1.next

    return linked_list_sum


def get_linked_list_sum(linked_list_1, linked_list_2):
    num1 = _get_linked_list_sum(linked_list_1)
    num2 = _get_linked_list_sum(linked_list_2)

    return num1 + num2


linked_list_1 = LinkedList(6)
linked_list_1.append(7)
linked_list_1.append(8)

linked_list_2 = LinkedList(3)
linked_list_2.append(5)
linked_list_2.append(4)

# print(get_linked_list_sum(linked_list_1, linked_list_2))
print(get_linked_list_sum(linked_list_1, linked_list_2))
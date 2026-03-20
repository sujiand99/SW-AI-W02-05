# 링크드리스트 - 에디터 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1406

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

new_node = Node("a")

head = new_node
tail = head

tail.next = Node("b")

tail = head.next

tail.next = Node("c")
tail = tail.next

tail.next = Node("d")
tail = tail.next

def print_list(node):
    while node:
        print(node.value, end=" ")
        node = node.next
    print()

tail.next = Node("x")
tail = tail.next





print_list(head)
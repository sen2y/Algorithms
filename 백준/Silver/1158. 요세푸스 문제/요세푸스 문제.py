import sys
input = sys.stdin.readline
n, k = map(int, input().split())

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

head = Node(1)
prev = head
for i in range(2, n+1):
    node = Node(i)
    prev.next = node
    prev = node
prev.next = head # 원형 리스트


result = []
curr = prev
while n:
    for _ in range(k):
        curr = curr.next
    result.append(curr.value)

    # 삭제
    tmp = curr.next 
    for _ in range(n-1):
        if tmp.next == curr:
            tmp.next = curr.next
            break
        tmp = tmp.next
    n -= 1

print("<" + ", ".join(map(str, result)) + ">")

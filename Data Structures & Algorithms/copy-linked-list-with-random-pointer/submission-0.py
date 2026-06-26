'''
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
'''

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        copyList = {None: None}

        current = head
        while current:
            newNode = Node(current.val)
            copyList[current] = newNode
            current = current.next
        current = head
        while current:
            ref = copyList[current]
            ref.next = copyList[current.next]
            ref.random = copyList[current.random]
            current = current.next

        return copyList[head]
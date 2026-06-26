# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        A,B = list1, list2
        if B is None:
            return A 
        elif A is None:
            return B

        if A.val > B.val:
            A,B = B,A
        
        head,temp = A,A
        A = A.next
        while A and B:
            

            if A.val < B.val:
                temp.next = A
                A = A.next
            else:
                temp.next= B
                B = B.next
            temp = temp.next

        if B:
            temp.next = B
        if A:
            temp.next = A
        
        return head
            

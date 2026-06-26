class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None

        second = self.reverseLL(second)
        first = head

        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2

    def reverseLL(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        temp = head

        if head.next:
            temp = self.reverseLL(head.next)
            head.next.next = head
        head.next = None
        return temp
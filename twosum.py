
class ListNode:

    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


class Solution(object):

    def addTwoNumbers(self, l1: ListNode, l2 ListNode) -> ListNode:

        result = curr = ListNode()

        remainder = 0

        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            total = x + y + remainder

            curr.next = ListNode(total % 10)
            remainder = total // 10

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

            curr = curr.next

        if remainder:
            curr.next = ListNode(remainder)

        return result.next

from ...linkedlist.linkedlist import Sll

# python -m dsa.patterns.05_list_reversal.206

class Solution:
    def reverseList(self, head: Sll | None) -> Sll | None:
        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev

if __name__ == '__main__':
    o = Solution()
    Sll.print(o.reverseList(Sll.from_iterable([1,2,3,4,5])))
    Sll.print(o.reverseList(Sll.from_iterable([1,2])))
    Sll.print(o.reverseList(Sll.from_iterable([])))

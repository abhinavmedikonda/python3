from ...linkedlist.linkedlist import Sll

# python -m dsa.patterns.05_list_reversal.092

class Solution:
    def reverseBetween(self, head: Sll | None, left: int, right: int) -> Sll | None:
        if not head or left >= right:
            return head
        prev = out_ = Sll(0, head)
        for _ in range(left-1):
            prev = prev.next
        curr = prev.next
        for i in range(right-left):
            temp = curr.next
            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp
        return out_.next

if __name__ == '__main__':
    o = Solution()
    Sll.print(o.reverseBetween(Sll.from_iterable([1,2,3,4,5]), 2, 4))
    Sll.print(o.reverseBetween(Sll.from_iterable([5]), 1, 1))

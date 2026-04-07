from ...linkedlist.linkedlist import Sll

# python -m dsa.patterns.05_list_reversal.024

class Solution:
    def swapPairs(self, head: Sll | None) -> Sll | None:
        if not head or not head.next:
            return head
        prev = Sll()
        frst = head
        scnd = out_ = frst.next
        next = scnd.next
        while frst and scnd:
            bufr = scnd.next
            scnd.next = frst
            frst.next = bufr
            prev.next = scnd
            prev = frst
            frst = bufr
            if not frst or not frst.next:
                return out_
            scnd = frst.next
            next = scnd.next
        return out_

if __name__ == '__main__':
    o = Solution()
    Sll.print(o.swapPairs(Sll.from_iterable([1,2,3,4])))
    Sll.print(o.swapPairs(Sll.from_iterable([])))
    Sll.print(o.swapPairs(Sll.from_iterable([1])))
    Sll.print(o.swapPairs(Sll.from_iterable([1,2,3])))

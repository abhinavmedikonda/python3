from ...linkedlist.linkedlist import Sll

# python -m dsa.patterns.04_varying_speeds.141

class Solution:
    def hasCycle(self, head: Sll | None) -> bool:
        if not head:
            return False
        one = head
        two = head.next
        while two and two.next:
            if one == two:
                return True
            one = one.next
            two = two.next.next
        return False

if __name__ == '__main__':
    o = Solution()
    print(o.hasCycle(Sll.from_iterable([3,2,0,-4], 1)))
    print(o.hasCycle(Sll.from_iterable([1,2], 0)))
    print(o.hasCycle(Sll.from_iterable([1], -1)))

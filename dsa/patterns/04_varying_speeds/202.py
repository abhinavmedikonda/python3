class Solution:
    def isHappy(self, n: int) -> bool:
        one = two = n
        while two != 1:
            one = sum(int(c)**2 for c in str(one))
            two = sum(int(c)**2 for c in str(two))
            if two == 1:
                return True
            two = sum(int(c)**2 for c in str(two))
            if one == two:
                return False
        return True

if __name__ == '__main__':
    o = Solution()
    print(o.isHappy(19))
    print(o.isHappy(2))
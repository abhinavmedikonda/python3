def binarySearch(nums, target):
    l, r = 0, len(nums)-1
    while l <= r:
        m = (l + r)//2
        if nums[m] == target:
            return m
        elif nums[m] > target:
            r = m-1
        else:
            l = m+1
    return -1

import bisect

def binarySearchUsingBisect(nums, target):
    l = bisect.bisect_left(nums, target)
    r = bisect.bisect_right(nums, target)
    if l == r:
        print(f'unique index: {l}')
    else:
        print(f'left index: {l}')
        print(f'right index: {r}')
    # bisect.insort

'''
8
1 2 4 6 8 8 9 10 12 14 16
8
'''
if __name__ == '__main__':
    print(binarySearch([1, 2, 4, 6, 8, 8, 9, 10, 12], 8))
    print(binarySearchUsingBisect([1, 2, 4, 6, 8, 8, 9, 10, 12], 8))

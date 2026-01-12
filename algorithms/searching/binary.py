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

'''
8
2 4 6 8 10 12 14 16
16
'''
if __name__ == '__main__':
    nums_count = int(input().strip())
    nums = [int(s) for s in input().strip().split()]
    target = int(input().strip())
    result = binarySearch(nums, target)
    print(result)

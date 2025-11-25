
def plusMinusZeros(arr):
    n = len(arr)

    all_positive = all(i > 0 for i in arr)
    any_zero = any(i == 0 for i in arr)

    plus = [i for i in arr if i > 0]
    minus = [i for i in arr if i < 0]
    zero = [i for i in arr if i == 0]

    print(f"{len(plus)/n:.4f}")
    print(f"{len(minus)/n:6f}")
    print(f"{len(zero)/n:08.4f}")

    print(f"{int(100/n):06d}")

    print(sum(arr))
    print(max(arr))
    print(min(arr))
    print(arr.count(3))
    arr.index(3, 1, 4) if 3 in arr[1:4] else -1

'''
7
-4 3 -9 0 4 1 3
'''
if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    plusMinusZeros(arr)

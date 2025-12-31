import sys

# kadane's algorithm
def mss(_arr):
    ms_ = 0
    low = sys.maxsize
    low_i = 0
    bgn = end = -1
    for i, it in enumerate(_arr):
        if it < low:
            low = it
            low_i = i
        if it-low > ms_:
            ms_ = it-low
            bgn = low_i
            end = i
    
    print(ms_, f'({bgn}, {end})')

if __name__ == '__main__':
    mss([1, 4, 8, 3, 2, -2, 6, -3, 7])

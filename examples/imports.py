aray = [1, 2, 3]

import sys
maxi = sys.maxsize

import copy
newu = copy.deepcopy(aray)

import heapq
heapq.heapify(aray)

from collections import deque
dequ = deque(aray)

from collections import Counter
cntr = Counter(aray)

from collections import defaultdict
hmap = defaultdict(lambda: [1, 2, 3])

import bisect
indx = bisect.bisect_right(aray, 2)



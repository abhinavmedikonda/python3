import heapq

mnhp = [4, 7, 2, 8, 1, 3]
heapq.heapify(mnhp)
print(f"Heap after heapify: {mnhp}")

heapq.heappush(mnhp, 5)
print(f"Heap after push(5): {mnhp}")

mn = heapq.heappop(mnhp)
print(f"Popped element: {mn}")
print(f"Heap after pop: {mnhp}")

data = [10, 4, 8, 2, 12, 5]
mxhp = [-n for n in data]
heapq.heapify(mxhp)
print(f"Heap after heapify: {mnhp}")

num = 2
heapq.heappush(mxhp, -num)

mx = -heapq.heappop(mxhp)


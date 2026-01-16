stack = []
stack.append(1)
stack.append(2)
stack.append(3)
print(stack.pop())

queue = []
queue.append(1)
queue.append(2)
queue.append(3)
print(queue.pop(0))

# list performs well for stack, deque performs well for queue
from collections import deque
my_queue = deque()
my_queue.append('A')
my_queue.append('B')
my_queue.append('C')
first_item = my_queue.popleft()
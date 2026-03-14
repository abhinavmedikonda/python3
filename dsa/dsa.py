stk = []
stk.append(1)
stk.append(2)
stk.append(3)
print(stk.pop())

que = []
que.append(1)
que.append(2)
que.append(3)
print(que.pop(0))

# list performs well for stack, deque performs well for queue
from collections import deque
deq = deque()
deq.append('A')
deq.append('B')
deq.append('C')
first_item = deq.popleft()
deq.appendleft('A')
last_item = deq.pop()
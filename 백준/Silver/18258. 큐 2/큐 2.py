
import sys
from collections import deque

n = int(sys.stdin.readline())
queue = deque()

for _ in range(n):
  order = sys.stdin.readline().split()

  if order[0] == 'push':
    queue.append(int(order[1]))

  if order[0] == 'pop':
    if queue:
      print(queue.popleft())
    else:
      print(-1)

  if order[0] == 'size':
    print(len(queue))

  if order[0] == 'empty':
    if queue :
      print(0)
    else:
      print(1)

  if order[0] == 'front':
    if queue :
      print(queue[0])
    else:
      print(-1)

  if order[0] == 'back':
    if queue :
      print(queue[-1])
    else:
      print(-1)

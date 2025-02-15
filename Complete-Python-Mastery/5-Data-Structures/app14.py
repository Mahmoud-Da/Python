from collections import deque

[1, 2, 3]

[1, 2, 3, 4, 5, 6, 7, 8, 9]

queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()

print(queue)
# deque([2, 3])

if not queue:
    print("'empty")

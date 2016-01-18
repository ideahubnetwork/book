from collections import deque

q = deque([1, 2, 3], maxlen=3)
print(q)

q.append(4)
print(q)
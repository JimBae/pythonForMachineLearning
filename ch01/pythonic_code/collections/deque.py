
from collections import deque

dequeList = deque()

for i in range(5):
	dequeList.append(i)
print(dequeList) #deque([0, 1, 2, 3, 4])

dequeList.appendleft(10)
print(dequeList) #deque([10, 0, 1, 2, 3, 4])

dequeList.rotate(2)
print(dequeList) #deque([3, 4, 10, 0, 1, 2])
dequeList.rotate(2)
print(dequeList) #deque([1, 2, 3, 4, 10, 0])


print(dequeList) #deque([1, 2, 3, 4, 10, 0])
print(deque(reversed(dequeList))) #deque([0, 10, 4, 3, 2, 1])


dequeList.extend([5,6,7])
print(dequeList) #deque([1, 2, 3, 4, 10, 0, 5, 6, 7])

dequeList.extendleft([5,6,7])
print(dequeList) #deque([7, 6, 5, 1, 2, 3, 4, 10, 0, 5, 6, 7])


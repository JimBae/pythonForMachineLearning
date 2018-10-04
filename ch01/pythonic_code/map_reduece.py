# ref
# https://github.com/TEAMLAB-Lecture/AI-python-connect/blob/master/codes/ch_1/pythonic_code/map_reduce.py

#=================================
# Map
#=================================

def f(x,y):
	return x+y
f(1,4)

f = lambda x,y: x+y
f(1,4)


exList = [1,2,3,4,5]
func = lambda x: x**2
print (list(map(func, exList)))


exList = [1,2,3,4,5]
funcName = lambda x,y: x+y
print (list(map(funcName, exList, exList))) 


list( map( lambda x:x**2 if x%2 == 0 else x, exList))

# if python3, you have to use with 'list'
exList = [1,2,3,4,5]
print (list(map(lambda x: x+x, exList)))
#print (map(lambda x: x+x, exList))

funcName = lambda x: x**2
print (map(funcName, exList))
for i in map(funcName, exList):
	print(i)

result = list(map(funcName, exList))
print (result)
#print (next(result))


import sys
sys.getsizeof(exList)
sys.getsizeof( list(map(lambda x: x+x, exList)))

#=================================
# Reduce
#=================================
from functools import reduce
print (reduce(lambda x, y:x+y, [1,2,3,4,5]))

def factorial(n):
	return reduce( lambda x, y:x*y, range(1,n+1))

# 5 * 4 * 3 * 2 * 1 
print (factorial(5))

#================================
# Summary
#================================
# lambda, map, reduce
# In python3, not recommend lambda and reduce because of readabiliry




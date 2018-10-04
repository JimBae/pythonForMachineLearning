# ref
# https://github.com/TEAMLAB-Lecture/AI-python-connect/blob/master/codes/ch_1/pythonic_code/lambda_function.py

def f(x, y):
	return x + y

print (f(1,4))

f = lambda x, y: x + y
print (f(1,4))


f = lambda x: x ** 2
print (f(3))


f = lambda x: x/2
print (f(3))


print ((lambda x: x+1)(5))


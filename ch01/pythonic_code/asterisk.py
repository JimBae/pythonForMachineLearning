# ref
# https://github.com/TEAMLAB-Lecture/AI-python-connect/blob/master/codes/ch_1/pythonic_code/asterisk_ex.py

# https://www.edwith.org/aipython/lecture/22956/

#-------------------------------
# Asterisk : *args and **kargs
#-------------------------------

# Case1 *args 
def asterisk_test(a, *args):
	print(a, args)
	print(type(args))
asterisk_test(1,2,3,4,5,6)

# Case2 *kargs
def asterisk_test(a, **kargs):
	print(a, kargs)
	print(type(kargs))
asterisk_test(1, b=2, c=3, d=4, e=5, f=6)


#-----------------------------------
# Asterisk : unpacking a container
#-----------------------------------
# unpacking the values in tuple, dict, etc. data types
# Can use function's input and zip 

def asterisk_test(a, *args):
	print (a, args)
	print (type(args))
asterisk_test(1, *(2,3,4,5,6))

#def asterisk_test(a, args):
#	print (a, *args) ##
#	print (type(args))
#asterisk_test(1, (2,3,4,5,6))







#-----------------------------------
# Examples
#-----------------------------------

def asterisk_test(a, *args): 
	print (a, args)
	print (type(args)) # tuple

asterisk_test(1,2,3,4,5,6)

def asterisk_test2(a, **args): 
	print (a, args)
	print (type(args)) # dict

asterisk_test2(1, b=2, c=3, d=4, e=5, f=6)


def asterisk_test(a, *args): 
	print (a, args[0])
	print (type(args)) # tuple

asterisk_test(1, (2,3,4,5,6))



#def asterisk_test(a, args): 
#	# error
#	print (a, *args)
#	print (type(args)) # tuple
#
#asterisk_test(1, (2,3,4,5,6))

a, b, c = ([1,2], [3,4], [5,6])
print (a,b,c)


data = ([1,2], [3,4], [5,6])
#print(*data)
print(data)

for data in zip( *([1,2], [3,4], [5,6]) ):
	print (sum(data))


def asterisk_test(a,b,c,d,e=0):
	print(a,b,c,d,e)

data = {"d":1, "c":2, "b":3, "e":56}
#asterisk_test(10, *data)
asterisk_test(10, **data)



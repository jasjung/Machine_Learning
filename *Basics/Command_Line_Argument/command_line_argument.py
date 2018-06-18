import sys

# check if it has any arguments

print()
arg_num = len(sys.argv) 

if arg_num == 1: 
	print('there are no arguments')

elif arg_num > 1: 
	# subtract 1 because one of the arguments is the file name 
	print('there are %d arguments ' % (arg_num-1))
	print(sys.argv)

	print('first argument is:', sys.argv[1])

	# how to combine all arguments without quotations 
	one_string = " ".join(sys.argv[1:])
	print(one_string)
	print(type(one_string))

print('done')
print()



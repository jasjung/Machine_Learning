import sys
import os 

# update my github folder 
# check if it has any arguments

print()
arg_num = len(sys.argv) 

def github_update(msg ='update'):
	print(msg)
	print()
	print('************************************************') 
	print('Pushing jasjung/Python')
	print('************************************************') 
	os.system("cd /Users/ijung/Desktop/Github/Python && git add . && git commit -m '%s' && git push origin master" % msg)

	print()
	print('************************************************') 
	print('Pushing jasjung/Python2')
	print('************************************************')
	os.system("cd /Users/ijung/Desktop/Github/Python2 && git add . && git commit -m '%s' && git push origin master" % msg)

if arg_num == 1: 
	print('there are no arguments')
	github_update()

elif arg_num > 1: 
	# subtract 1 because one of the arguments is the file name 
	print('there are %d arguments ' % (arg_num-1))
	print(sys.argv)
	# combine all arguments 
	one_string = " ".join(sys.argv[1:])
	github_update(msg=one_string)

print('done')
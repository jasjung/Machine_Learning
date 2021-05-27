import sys
print('### Writing to File')
temp = sys.stdout                 # store original stdout object for later
sys.stdout = open('log.txt', 'w') # redirect all prints to this log file
print("testing123")               # nothing appears at interactive prompt
print("another line")             # again nothing appears. it's written to log file instead
sys.stdout.close()                # ordinary file object

sys.stdout = temp                 # restore print commands to interactive prompt
print("back to normal")           # this shows up in the interactive prompt
print(temp)


print('### Writing to Console')

stdout_fileno = sys.stdout
sample_input = ['Hi', 'test', 'test2']
 
for i in sample_input:
    # Prints to stdout
    stdout_fileno.write(i + '\n')

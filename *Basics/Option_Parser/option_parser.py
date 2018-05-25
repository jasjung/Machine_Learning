
'''
Option Parser starter code

'''

from optparse import OptionParser

parser = OptionParser()

parser.add_option('-u', '--user', action='store', type='string', help='ownder of the hive table')

parser.add_option('-d', '--dimensions', action='store', type='string', help='array of dimensions of the table that will be used for formning different dimensions')

parser.add_option('-m', '--metrics', action='store', type='string', help='array of metrics')

(options, args) = parser.parse_args()

if options.user == None or options.metrics == None or options.dimensions == None:
	print('*** You did not provide all necessary arguments. Please try again. I am quitting the script.')
	quit() 

#print(options)
#print(options.metrics)
#print(args)

print(options.user)
print((options.metrics).split(','))
print((options.dimensions).split(','))

#print(eval(options.metrics))

#options.metrics


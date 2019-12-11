
'''
https://www.pyimagesearch.com/2018/03/12/python-argparse-command-line-arguments/
https://stackoverflow.com/questions/15301147/python-argparse-default-value-or-specified-value
'''

import argparse

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-n", "--name", required=True,
	help="name of the user")
args = vars(ap.parse_args())

# display a friendly message to the user
print("Hi there {}, it's nice to meet you!".format(args["name"]))

# python argparse.py --name Adrian

# python ex.py --help
# python ex.py --name Adrian jo


error_exit()
{
	echo "$1" 
	echo "$0"
	exit 1
	# send failure email 
}

success_exit()
{
	exit 0
	# send success email 
}

DATE_no_hyphen=`date +%Y%m%d`

if python test.py
	then 
		echo 'yo'
		touch success_$DATE_no_hyphen
else error_exit "Error"
fi 

exit 0

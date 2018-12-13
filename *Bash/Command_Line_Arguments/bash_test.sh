
#!/bin/bash
for arg in "$@"
do
    if [ "$arg" == "1" ] 
    then
        echo "1"
    fi

    if [ "$arg" == "2" ] 
    then
        echo "2"
    fi

    if [ "$arg" == "3" ] 
    then
        echo "3"
    fi
    
done

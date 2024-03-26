#!/bin/bash
# Lets create an until loop that takes a variable and adds 1 till it reachs 10
# Have the script echo out what are current number is
i=1
until [[ $i -eq 10 ]]
do
    echo "$i"
    ((i++)) 
done
echo "loop done the vaule of i is now $i" 
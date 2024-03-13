#!/bin/bash

# Lets create a function in bash that adds two number together
# Stretch goal can you do subtraction, multipliaction or division
# You will need to declare two variables
num1=5
num2=6
addnum() {
    sum=$((num1 + num2))
    echo "$sum"  
}
addnum
#!/bin/bash
# Given three integers (, , and ) representing the three sides of a triangle, identify whether the triangle is scalene, isosceles, or equilateral.
# If all three sides are equal, output EQUILATERAL.
# Otherwise, if any two sides are equal, output ISOSCELES.
# Otherwise, output SCALENE.
# Input Format
# Three integers, each on a new line.
# Constraints
# The sum of any two sides will be greater than the third.
# Output Format
# One word: either "SCALENE" or "EQUILATERAL" or "ISOSCELES" (quotation marks excluded)

echo " enter 3 sides of a triangle! "
read a
read b
read c

if [ $a == $b ] && [ $b == $c ] && [ $c == $a ]
then
    echo 'this is an equilateral'
elif [ $a == $b ] || [ $b == $c ] || [ $c == $a ]
then
    echo 'this is an isosceles'
else
    echo 'this is scalene'
fi 



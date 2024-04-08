#!/bin/bash
# Today we are going to use a case statment instead of a conditional
# Have the program ask how your day is and echo out a response for good or bad
# Case statment format is a little different so please look up how this would be formated
# https://linuxize.com/post/bash-case-statement/
echo "How is your day going?"
read MOOD
echo "My day is going $MOOD"

case $MOOD in

  "good")
    echo -n "GOOD TO HEAR IT WAS $MOOD"
    ;;

  "bad")
    echo -n "SORRY TO HEAR THAT IT WAS $MOOD"
    ;;

  "terrible")
    echo -n "Wow what happen to make it $MOOD"
    ;;

  *)
    echo -n "idk"
    ;;
esac
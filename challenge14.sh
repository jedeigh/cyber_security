#!/bin/bash
# find all connections on the network
sudo nmap -sn 192.168.1.0/24
# from here select which device on the network you want to ping
echo "please chose a device on the network to ping!"
read ping
echo "you pinged $ping"  # want to show device not ip address
echo "do you want to send a file to $ping y/n"
read response
if $response=n
 then 
 echo "ok have a nice day!"
else
    echo "ok have a great day!" 
fi    
#echo "simple data" > encryptfile.txt # create a file
#encrypt_file =encryptfile.txt # encrypt file
#gpg -c "$encrypt_file"
# send encrypted file to pinged device 


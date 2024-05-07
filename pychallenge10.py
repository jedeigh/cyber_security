from urllib import response
import requests
import time 
# Create a Python script that performs the following:

# Prompt the user to type a string input as the variable for your destination URL.

# Prompt the user to select a HTTP Method of the following options:
# GET - used to retrive info from the given server using a given URL
# POST - request that a web server accepts the data enclosed in the body of the request message, most likely storing it
# PUT - requst that the enclosed entity be stored under the supplied URL. If the URL refers to an already existing resource, it is modified and if the URL does not point to an existing resource, the server can create the resource with that URL
# DELETE - deletes the specified resource
# HEAD - ask for a response identical to that of a GET request, but without the response body
# PATCH - is used for modify capabilites. The Patch request only needs to contain the changes to the resource, not the complete resource
# OPTIONS - request permitted communication options for a given URL or server. A client can specify a URL with this method, or an asterisk * to refer to the entire server
# Print to the screen the entire request your script is about to send. Ask the user to confirm before proceeding.
# Add some comments of what these request are doing to your script
# Using the requests library, perform a GET request to your github.

# For the given header, translate the codes into plain terms that print to the screen; for example, a 404 error should print Site not found to the terminal instead of 404.
#response = requests.get()
# For the given URL, print response header information to the screen.

user_url = input('Hi please enter a vaild url address, \n for example: https://www.espn.com ')

print('Please choose an HTTP Method from the selections below!')
time.sleep(2)
r = input("Get, Post, Put, Delete , Head, Patch, Options: ")

if r == 'get' or 'Get':
    r = requests.get(user_url)
    content = input('Do you want to print the data on screen y/n: ')
    if content == 'y' or 'yes':
        print(r)
        print(r.content)
    if content == 'n' or 'no':
        print('request completed!')
elif r == 'post' or 'Post':
    r = requests.post(user_url,data ={'key':'value'})
    print(r)
    print(r.json())
elif r == 'put' or 'Put':
    r = requests.put(user_url,data ={'key':'value'})
    print(r)
    print(r.content)
elif r == 'delete' or 'Delete':
    r = requests.delete(user_url,data ={'key':'value'})
    print(r)
    print(r.json())
elif r == 'head' or 'Head':
    r = requests.head(user_url,data ={'key':'value'})
    print(r)
    print(r.headers)
    print(r.content)
elif r == 'patch' or 'Patch':
    r = requests.patch(user_url,data ={'key':'value'})
    print(r)
    print(r.content)
elif r == 'post' or 'Post':
    r = requests.post(user_url,data ={'key':'value'})
    print(r)
    print(r.json())
elif r == 'options' or 'Options':
    r = requests.options(user_url)
    print(r.status_code)
    print(r.headers)
else:
    print('Sorry that was a vaild option!')


   



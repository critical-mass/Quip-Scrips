#imports
import json
import requests
import os
from dotenv import load_dotenv
from pathlib import Path

#load in enviroment vars
dotenv_path = Path('/Users/daniel/fun/python_projects/python-http/env/.env')
load_dotenv(dotenv_path=dotenv_path)

#vars
nickName = input('Input the nickname of the user: ')
lastName = input('Input the lastname of the user: ')
email = input('Input the email of the user: ')
name = str(nickName)+str(" ")+str(lastName)
url = "https://scim.quip.com/Users"
token = os.environ['TOKEN']

#construct json body 
data = {
    "name": "%s" % name,
    "email": "%s" % email
}
headers = {
	'Authorization': 'Bearer %s' % token
}

#make the request
response = requests.post(url=url, headers=headers, data=data)
print(response.content)
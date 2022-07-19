#imports
import json
import requests
import os
from dotenv import load_dotenv
from pathlib import Path

def add_user(nickName, lastName, email):
    #load in enviroment vars
    dotenv_path = Path('/Users/daniel/fun/python_projects/python-http/env/.env')
    load_dotenv(dotenv_path=dotenv_path)

    #vars
    name = str(nickName)+str(" ")+str(lastName)
    url = "https://scim.quip.com/Users"
    token = os.environ['TOKEN']

    #construct json body & headers
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
    return(response.content)
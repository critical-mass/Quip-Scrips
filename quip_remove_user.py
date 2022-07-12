#imports
from fileinput import filename
import requests
import json
import os
from dotenv import load_dotenv
from pathlib import Path

#define some vars
dotenv_path = Path('/Users/daniel/fun/python_projects/python-http/env/.env')
filename = "test.json"

#load the enviroment vars
load_dotenv(dotenv_path=dotenv_path)

#take the email of the user being offboarded
email = input('what email do you want offboarded? ')

#define the url, email, token, payload and headers 
url = "https://scim.quip.com/2/Users?filter=emails+eq+{}".format(email)
token = os.environ['TOKEN']
payload={}
headers = {
	'Authorization': 'Bearer %s' % token
}

#define the response and make the request
response = requests.get(url, headers=headers, data=payload)

#write the data to the file
with open(filename, "w") as f:
	f.write(str(response.text))
f.close()

#read the data from the file and caputer the id of the user in question.
#new var defined as ID
with open(filename, "r") as fb:
	data = json.loads(fb.read())
	id = data['Resources'][0]['id']
fb.close()

#construct request to remove user in quip
delete_url = "https://scim.quip.com/2/Users/{}".format(id) 
headers = {
'Authorization': 'Bearer %s' % token
}

#define a new response var and make deletion request
response = requests.delete(delete_url, headers=headers, data=payload)
print(response.content)
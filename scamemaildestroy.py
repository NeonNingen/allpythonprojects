import requests
import os
import random
import string
import json

chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))

url = 'https://applewebsecured9752.theworkpc.com/HijaIyh_App/request/iyh_login.php?locale=en_GB'

names = json.loads(open('names.json').read())

for name in names:
	name_extra = ''.join(random.choice(string.digits))

	username = name.lower() + name_extra + '@yahoo.com'
	password = ''.join(random.choice(chars) for i in range(8))

	requests.post(url, allow_redirects=False, data={
		'xuser': username,
		'xpass': password
		})

print("The username: %s and password: %s") % (username, password)
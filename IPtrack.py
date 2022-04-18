#!/usr/bin/python

import time
import os
import json
from urllib import request

print("--- IP Tracker ---")
print("")
time.sleep(2)
os.system("clear")

url = "http://ip-api.com/json/"
ip = input("IP: ")
request = request.urlopen(url + ip)
data_json = json.loads(request.read())

if data_json['status'] == "success":
	print(f"IP : {data_json['query']}")
	print(f"País : {data_json['country']}")
	print(f"Região : {data_json['regionName']}")
	print(f"Cidade : {data_json['city']}")
	print(f"Latitude : {data_json['lat']}")
	print(f"Longitude : {data_json['lon']}")
	print(f"ISP : {data_json['isp']}")
else:
	print("IP inválido!")

#!/usr/bin/python

import time
import os
import json
from urllib import request
os.system('cls' if os.name == 'nt' else 'clear')
url = "http://ip-api.com/json/"
print("--- Simple IP Tracker ---")

def request_and_input():
    print('<enter> for your own ip, or 0 to leave.')
    ip = input(": ")
    if ip == 0:
	quit()
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
	print("Invalid IP!")
    
while(True):
    request_and_input()

# -*- coding: utf-8 -*-
"""
Created on Sat May  7 18:57:55 2022
https://www.nylas.com/blog/use-python-requests-module-rest-apis/
@author: asbjo
"""
import requests

username = ''
PhilipsHuebridgeIP = ""


response = requests.put("http://"+PhilipsHuebridgeIP+"/api/"+ username +"/lights/2/state", json={"on":True})

print(response.json())


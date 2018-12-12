# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 12:00:06 2018

@author: npapp
"""

import os

from awair import awair

path = "C:/Users/npapp/Dropbox/Python"
os.chdir(path)
os.listdir(path)

username = "npappas@gmail.com"
password = "awa123123"

api = awair(username,password)

devices = api.devices()

for device in devices:
    print(device)
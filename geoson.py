# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 21:46:57 2017

@author: atse
"""

import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'http://py4e-data.dr-chuck.net/json?key=42&'
address = input('Enter location: ')
url = serviceurl + '?' + urllib.parse.urlencode({'sensor':'false', 'address':  address})
data = urllib.request.urlopen(url).read().decode()
info = json.loads(data)
info = info['results']
print('Retrieving', url, '\nRetrieved', len(data), 'characters')
for item in info:
    key = item['place_id']
print('Place id:',key)

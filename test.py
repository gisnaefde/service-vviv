# import requests

# response = requests.get('http://192.168.8.161/api/set-interval')

# data = response.json()
# set_interval = data['data'][0]['set_interval']
# print(set_interval)

import pyodbc
import time
import os
import requests

server = '192.168.8.111'
database = 'REMONDB'
username = 'sa'
password = 'dbadmin123!@'

conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+'; DATABASE='+database+';UID='+username+';PWD='+password)

last_data = None

try :
    while True:
        response = requests.get('http://192.168.8.161/api/set-interval')
        interval = json.loads(response.text).get('interval', 10)
		print(interval)
        time.sleep(interval)




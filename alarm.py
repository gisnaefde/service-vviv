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
        cursor = conn.cursor()
        cursor.execute('SELECT TOP 1 * FROM trg_TBL_ALARM_HIST ORDER BY alarm_hist_idx DESC')
        row = cursor.fetchone()

        response = requests.get('http://192.168.8.161/api/set-interval')
        data = response.json()
        set_interval = data['data'][0]['set_interval']
        print(set_interval)
        if row:
            if row == last_data:
                print("Data Masih Sama")
            else:
                os.system("curl -X POST http://192.168.8.125/api/send-alarm-data")
            last_data = row
        else:
            print ("Tidak Ada Data di Tabel")
        
        time.sleep(set_interval)

except pyodbc.Error as e:
    print("Terjadi kesalahan:", str(e))

finally:
    conn.close()

# import time

# while (True):
# 	print('test')
# 	time.sleep(10)


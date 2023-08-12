import pyodbc
import time
import os
import requests

server = '192.168.8.111'
database = 'REMONDB'
username = 'sa'
password = 'dbadmin123!@'

conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+'; DATABASE='+database+';UID='+username+';PWD='+password)

last_row_count = 0

try:
    while True:
        cursor = conn.cursor()
        cursor.execute('SELECT COUNT(*) FROM TBL_RT_INFO')
        row = cursor.fetchone()
        current_row_count = row[0]

        response = requests.get('http://192.168.8.161/api/set-interval')
        data = response.json()
        set_interval = data['data'][0]['set_interval']
        print(set_interval)

        if current_row_count > 0:
            if current_row_count == last_row_count:
                print("Data Masih Sama")
            else:
                print("Data baru dikirim ke server")
                os.system("curl -X POST http://192.168.8.125/api/send-rt-info")

            last_row_count = current_row_count
        else:
            print("Tidak Ada Data di Tabel")

        time.sleep(set_interval)

except pyodbc.Error as e:
    print("Terjadi kesalahan:", str(e))

finally:
    conn.close()

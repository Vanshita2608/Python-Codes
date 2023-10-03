#dbs_connectivity.py

import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",password="",database="college")
if mydb:
  print("Connection Established Successfully")
else:
  print("Connection Error")
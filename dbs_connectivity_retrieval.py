#dbs_connectivity_retrieval.py

import mysql.connector

try:
  con = mysql.connector.connect(host="localhost",user="root",password="",database="college")
  print("Connection Established Successfully")
  cur = con.cursor()  
  print(cur)
  #id,name,branch,sem,city
  sql="select * from student"
  cur.execute(sql)
  result = cur.fetchall()
  print("ID      Name        Branch      Sem      City")
  for row in result:
    #print(row)
    print("%d      %s     %s           %d      %s"%(row[0],row[1],row[2],row[3],row[4]))  
except:
  print("Connection Error")
finally:
  if con:
    con.close()
    print("Resources Released")
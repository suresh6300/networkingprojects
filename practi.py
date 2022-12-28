
import mysql.connector
db = mysql.connector.connect(host='127.0.0.1', user="root", password="Shreya@9966", database="network")
mycur = db.cursor()
query='use network'
mycur.execute(query)
query1='''create table network_table
          
       
mycur.execute(query1)
query2='select * from network_table'
mycur.execute(query2)
print(mycur)

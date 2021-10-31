#C:\Program Files\MySQL\MySQL Server 8.0\bin
from imbox import Imbox
from datetime import datetime
import re
import traceback
import os
import mysql.connector
import pymongo 
import gridfs


#after creation of database email_components and table-company on mysql workbench
mydb = mysql.connector.connect(
  host="localhost",
  user="user",            #insert your username
  password="yourpassword",#insert your password
  database='email_components'
)


#after creation of database email_attachments on mongodb using command- use email_attachments
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
#print(myclient.list_database_names())
db = myclient["email_attachments"]


#extracting email body and attachments and storing them in respective databases
download_folder = "C:\\Users\\Admin\\OneDrive\\Desktop\\Email_Project\\project"#replace path
if not os.path.isdir(download_folder):
    os.makedirs(download_folder, exist_ok=True)
with Imbox('imap.gmail.com',
        username='email', #insert your email id
        password='password',#insert your password
        ssl=True,
        ssl_context=None,
        starttls=False) as imbox:
        inbox_messages_from = imbox.messages(
            sent_from='vedashreejoshi20@gmail.com',
            sent_to='vedashree.j@somaiya.edu',
            #date__on=datetime.date(2021, 10, 30),
            unread=True)
        all_inbox_messages = imbox.messages()
        for uid, message in inbox_messages_from:
                    inbox_messages_from.mark_seen(uid)
                    message.body
                    me=message.body['plain'][0]
                    me=me.split('\r\n\r\n')
                    #inv = re.findall(r'[0-9]+',message.body['plain'][0])
                    #invoice=inv[3]
                    company=me[0]
                    date=me[1].split(': ')[1]
                    invoice=me[2].split(': ')[1]
                    items=  me[3].split(': ')[1]
                    address=me[4].split(': ')[1]
                    print(company)
                    print(date)
                    print(invoice)
                    print(items)
                    print(address)
                    sql = "INSERT INTO Company VALUES (%s,%s,%s,%s,%s)"
                    val = (company,date,invoice,items,address)
                    mycursor = mydb.cursor()
                    mycursor.execute(sql, val)
                    mydb.commit()
                    print(mycursor.rowcount, "record inserted.")
                    for idx, attachment in enumerate(message.attachments):
                      try:
                         att_fn = attachment.get('filename')
                         download_path = f"{download_folder}/{att_fn}"
                         print(download_path)
                         with open(download_path, "wb") as fp:
                              fp.write(attachment.get('content').read())
                         file_location=download_path
                         file_data=open(file_location,"rb")
                         data=file_data.read()
                         fs=gridfs.GridFS(db)
                         fs.put(data,filename=att_fn)
                         print("upload complete")
                      except:
                         print(traceback.print_exc())
                        

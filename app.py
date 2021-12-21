# coding: utf-8
from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
import os
import psycopg2


app = Flask(__name__)
#BDD1
DB_HOST = "host"
DB_NAME = "name"
DB_USER = "user"
DB_PASS = "password"




@app.route('/')
def index():
    conn = psycopg2.connect(
    host=DB_HOST,
    database=DB_NAME,
    user=DB_USER,
    password=DB_PASS,
    port="5432",
    sslmode='require')
    cursor=conn.cursor()
    cursor.execute("SELECT table_schema,table_name FROM information_schema.tables WHERE table_schema = 'public' ORDER BY table_schema,table_name")
    rows = cursor.fetchall()

    print(rows.__len__())
    if(rows.__len__()==0):
        return render_template("indexvide.html")
    else:
        cursor.execute('''SELECT * from ouvrage00''')
        data00=cursor.fetchall()
        cursor.execute('''SELECT * from ouvrage01''')
        data01=cursor.fetchall()
        cursor.execute('''SELECT * from ouvrage02''')
        data02=cursor.fetchall()
        cursor.execute('''SELECT * from ouvrage03''')
        data03=cursor.fetchall()
        cursor.execute('''SELECT * from ouvrage20''')
        data20=cursor.fetchall()
        cursor.execute('''SELECT * from ouvrage21''')
        data21=cursor.fetchall()
        cursor.execute('''SELECT * from ouvrage22''')
        data22=cursor.fetchall()
        cursor.execute('''SELECT * from ouvrage23''')
        data23=cursor.fetchall()      
        conn.close()                          
        return render_template("index.html",data00=data00,data01=data01,data02=data02,data03=data03,data20=data20,data21=data21,data22=data22,data23=data23)


if __name__ == "__main__":
    
    app.run()
    
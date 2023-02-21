import mysql.connector
import requests
import datetime

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "face_db"  
)
  
mycursor = mydb.cursor()

dd = datetimes.datetime.now()

objects = payload["FaceRec"]["face_array"]
face_count  = payload["FaceRec"]["count"]

if (face_count <=0):
    print("ไม่พบใบหน้า")
    payload["show_message"] = "ไม่พบข้อมูลใบหน้า"
else:
    for objs in objects:
        sql = "select * from tbl_students where std_code = %s"
        val = (objs["name"],)
        mycursor.execute(sql,val)
        records = mycursor.fetchall()
        if(mycursor.rowcount<=0):
            print("ไม่พบข้อมูล",objs["name"],"ในฐานข้อมูล")
        else: 
            std_name = records[0][1]+records[0][2]+" "+records[0][3]
            sql ="select datetime, send_line from tbl_checkin where std_code = %s and DATE(datetime)=%s"
            val = (objs["name"], dd.stftime("%Y-%m-%d"),)
            mycursor.execute(sql,val)
            records = mycursor.fetchall()
            if(mycursor.rowcount<=0):
                sql = "insert into tbl_checkin (check_id, datetime, std_code, send_line) values(NULL, %s, %s, '0')"
                val = (dd.stftime("%Y-%m-%d %H:%M"),objs["name"],)
                mycursor.execute(sql,val)
                mydb.commit()      
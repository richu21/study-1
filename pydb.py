import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="pass123",
  database="pystudy"
)

try : 
    mycursor = mydb.cursor()
    sql = """INSERT INTO students (RollNo,FirstName,LastName,mark1,mark2,mark3) VALUES (%s, %s, %s, %s, %s, %s)"""
    val = (10,"rohit","sharma",35,28,43)
    mycursor.execute(sql,val)
    # mycursor.fetchall()
    mydb.commit()
except Exception as ex :
    print(ex)
    mydb.rollback()
finally :
    mydb.close()

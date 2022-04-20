import pandas as pd
import mysql.connector
from sqlalchemy import create_engine 

def connect_mysql_cursor_execute(x):
    db= mysql.connector.connect(host="localhost", user="root", password="password")
    cursor = db.cursor()
    cursor.execute(x)
def connect_mysql_cursor_execute_tables_motor(x,y,z):
    str_conn='mysql+pymysql://root:password@localhost:3306/lab_5.3'
    motor=create_engine(str_conn)

x.to_sql(name='selenium', con=motor, if_exists='append', index=False)



"""

This file will read records from the database table 

github: https://github.com/yfujieda
twitter: https://twitter.com/yfujieda_
10/13/2019

"""

import pymysql.cursors

SERVER_URL = "localhost"
DB = "test_db"
USER_NAME = "yourusername"
PASSWORD = "yourpassword"

SQL_CONNECTION = pymysql.connect(host=SERVER_URL,
                    user=USER_NAME,
                    passwd=PASSWORD,
                    db=DB,
                    charset='utf8mb4',
                    cursorclass=pymysql.cursors.DictCursor,
                    autocommit=True)

SQL = """SELECT * FROM test_db.cars"""

with SQL_CONNECTION.cursor() as cursor:
    try:
        sql_exec = cursor.execute(SQL)
        if sql_exec:
            print(sql_exec)
            print(cursor.fetchall())
        else:
            print(sql_exec)
            print("No Record")
    except (pymysql.Error, pymysql.Warning) as e:
        print(f'error! {e}')
    
    finally:
        SQL_CONNECTION.close()
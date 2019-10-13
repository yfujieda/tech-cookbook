""" 

This file will update the specified record

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

SQL = """UPDATE test_db.cars SET car_model = 'explorer', car_brand = 'ford' WHERE id = '3'"""

with SQL_CONNECTION.cursor() as cursor:
    try:
        sql_exec = cursor.execute(SQL)
        if sql_exec:
            print(sql_exec)
            print("Record Upadted")
        else:
            print(sql_exec)
            print("Not Upadted")
    except (pymysql.Error, pymysql.Warning) as e:
        print(f'error! {e}')

    finally:
        SQL_CONNECTION.close()

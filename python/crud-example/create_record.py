""" 

This file will create a new record in the database table 

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

SQL = """INSERT INTO test_db.cars(car_model, car_brand) VALUES ('accord', 'honda')"""

with SQL_CONNECTION.cursor() as cursor:
    try:
        sql_exec = cursor.execute(SQL)
        if sql_exec:
            print(sql_exec)
            print("Record Added")
        else:
            print(sql_exec)
            print("Not Added")
    except (pymysql.Error, pymysql.Warning) as e:
        print(f'error! {e}')

    finally:
        SQL_CONNECTION.close()
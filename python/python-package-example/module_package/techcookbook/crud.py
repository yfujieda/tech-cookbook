"""crud module"""

import pymysql.cursors

def connection():
    """
    function to establish connection with the database
    """

    SERVER_URL = "localhost"
    DB = "test_db"
    USER_NAME = "yourusername"
    PASSWORD = "yourpassword"

    DB_CONNECTION = pymysql.connect(host=SERVER_URL,
                    user=USER_NAME,
                    passwd=PASSWORD,
                    db=DB,
                    charset='utf8mb4',
                    cursorclass=pymysql.cursors.DictCursor,
                    autocommit=True)

    return DB_CONNECTION

def close_connection(DB_CONNECTION):
    """
    function to close the connection with DB
    """

    DB_CONNECTION.close()


def create_record():
    """
    function to create a record
    """

    DB_CONNECTION = connection()

    SQL = """INSERT INTO test_db.cars(car_model, car_brand) VALUES ('accord', 'honda')"""

    with DB_CONNECTION.cursor() as cursor:
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
            close_connection(DB_CONNECTION)

def read_record():
    """
    function to read the records
    """  

    DB_CONNECTION = connection()

    SQL = """SELECT * FROM test_db.cars"""

    with DB_CONNECTION.cursor() as cursor:
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
            close_connection(DB_CONNECTION)


def update_record():
    """
    function to update a record
    """

    DB_CONNECTION = connection()

    SQL = """UPDATE test_db.cars SET car_model = 'explorer', car_brand = 'ford' WHERE id = '3'"""

    with DB_CONNECTION.cursor() as cursor:
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
            close_connection(DB_CONNECTION)


def delete_record():
    """
    function to delete a record
    """    

    DB_CONNECTION = connection()

    SQL = """DELETE FROM test_db.cars WHERE id = '4'"""

    with DB_CONNECTION.cursor() as cursor:
        try:
            sql_exec = cursor.execute(SQL)
            if sql_exec:
                print(sql_exec)
                print("Record Deleted")
            else:
                print(sql_exec)
                print("Not Deleted")
        except (pymysql.Error, pymysql.Warning) as e:
            print(f'error! {e}')

        finally:
            close_connection(DB_CONNECTION)
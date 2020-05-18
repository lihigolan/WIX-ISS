import mysql.connector
import constants

mycursor = None
mydb=None

def connect_db():
    try:
        global mydb
        mydb = mysql.connector.connect(
        host="35.195.247.8",
        port="3306",
        database="interview",
        user="interview_user",
        passwd="mysql202098114345!#"
        )

        global mycursor
        mycursor = mydb.cursor()

    except Exception as exc:
        print(exc)
        return False
    return True

def create_orbital_table():
    try:
        mycursor.execute("CREATE TABLE " + constants.TABLE_ORBITAL +
                         " (" + constants.CITY + " VARCHAR(255), "
                         + constants.DATE + " DATETIME, "
                         + constants.DURATION + " INT)")

    except Exception as exc:
        if not constants.ALR_EXIST in exc.msg:
            print(exc)
            return False
    return True


def reset_stats_table(data):
    try:
        mycursor.execute("CREATE TABLE " + constants.TABLE_STATS +
                         " (" + constants.CITY + " VARCHAR(255), "
                         + constants.AVG_APPEARANCE + " double)")
        #insert only once
        insert_to_stats(data)

    except Exception as exc:
        if not "already exists" in exc.msg:
            print(exc)
            return False
    return True

def insert_to_orbital(data):
    sql = "INSERT INTO " + constants.TABLE_ORBITAL \
          + " (" + constants.CITY + ", " \
          + constants.DATE + ", " \
          + constants.DURATION + ")  VALUES (%s, %s, %s)"
    try:
        mycursor.executemany(sql, data)
        mydb.commit()

    except Exception as exc:
        print(exc)
        return False
    return True

def insert_to_stats(data):
    sql = "INSERT INTO " + constants.TABLE_STATS \
          + " (" + constants.CITY + ", " \
          + constants.AVG_APPEARANCE +")  VALUES (%s, %s)"
    try:
        mycursor.executemany(sql, data)
        mydb.commit()

    except Exception as exc:
        print(exc)
        return False
    return True

def create_stat_update_proc():
    return handle_create_proc(constants.PROCEDURE_STAT_NAME, constants.SQL_STAT_PROC)


def create_union_proc():
    return handle_create_proc(constants.PROCEDURE_UNION_NAME, constants.SQL_UNION_PROC)

def handle_create_proc(name, body):
    try:
        mycursor.execute(body)
        return name
    except Exception as exc:
        if constants.ALR_EXIST in exc.msg:
            return name
        print(exc)
        return None

def call_proc(name):
    try:
        mycursor.execute("call "+ name +"();")
        return True
    except Exception as exc:
        print(exc)
        return False

def get_data_from_table(name):
    try:
        mycursor.execute("select * from " + name + ";")
        return mycursor.fetchall()
    except Exception as exc:
        print(exc)
        return None
    
def delete_table(name):
    try:
        mycursor.execute("drop table " + name + ";")
    except Exception as exc:
        print(exc)
        return False
    return True

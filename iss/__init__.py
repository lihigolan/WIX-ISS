import csv_handler
from config_data import getData
from datetime import datetime
from sql_conector import *
import constants

def start_task():
    cities_data = getData()
    if len(cities_data) <= 0:
        print("DATA error, did nothing, BYE !!!!!")
        return

    if not connect_db():
        print("CONNECTION ERROR TO DB,BYE")
        return

    if not create_orbital_table():
        print("TABLE orbital ERROR, BYE")
        return

    initial_orbital(cities_data)
    initial_stats(cities_data)
    calc_stats()

def calc_stats():
    proc_stat_name = create_stat_update_proc()
    if proc_stat_name is not None:
        success = call_proc(proc_stat_name)
        if success:
            return make_union()
    print("ERROR, Something went wrong with the procedure: "+constants.PROCEDURE_STAT_NAME+", BYE BYE!")

def make_union():
    proc_union_name = create_union_proc()
    if proc_union_name is not None:
        success = call_proc(proc_union_name)
        if success:
            return create_csv()
    print("ERROR, Something went wrong with the procedure: "+constants.PROCEDURE_UNION_NAME+", BYE BYE!")

def create_csv():
    csv_handler.write_union_data_to_csv();
    delete_table(constants.TABLE_UNION)
    print("DONE!!!! BYE ..... ")

def initial_orbital(cities_data):
    for city in cities_data:
        data = []
        for i in range(len(cities_data[city])):
            timestamp = cities_data[city][i][constants.RISE_TIME]
            dt_object = datetime.fromtimestamp(timestamp)
            row = (city, dt_object, cities_data[city][i][constants.DURATION])
            data.append(row)

        insert_to_orbital(data)


def initial_stats(cities_data):
    data = []
    for city in cities_data:
        row = (city, 0)
        data.append(row)

    reset_stats_table(data)



start_task()




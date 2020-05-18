import csv
import constants
from sql_conector import get_data_from_table

fields = [constants.CITY, constants.POPULATION, constants.MAX_TEMP, constants.MIN_TEMP, constants.UPDATE_DATE,
          constants.AVG_APPEARANCE]

filename = constants.CSV_FILE_NAME + ".csv"

def write_union_data_to_csv():
    try:
        with open(filename, 'w') as csvfile:
            csvwriter = csv.writer(csvfile)
            data = get_data_from_table(constants.TABLE_UNION)
            if (data):
                csvwriter.writerow(fields)
                csvwriter.writerows(data)
                print("output file name is: " + filename)
            else:
                print("Oops, Error - data from sql is null")
    except Exception as exc:
        print(exc)

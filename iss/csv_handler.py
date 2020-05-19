import csv
from sql_conector import get_data_from_table, get_col_names

def write_table_to_csv(table_name, filename):
    try:
        with open(filename + ".csv", 'w') as csvfile:
            csvwriter = csv.writer(csvfile)
            fields = get_col_names(table_name)
            data = get_data_from_table(table_name)

            if (data and fields):
                fields = arrange(fields)
                csvwriter.writerow(fields)
                csvwriter.writerows(data)
                print("output file name is: " + filename)
            else:
                print("Oops, Error - data from sql is null")
    except Exception as exc:
        print(exc)

def arrange(fields):
    arrangedfields = []
    for field in fields:
        arrangedfields.append(field[0])
    return arrangedfields
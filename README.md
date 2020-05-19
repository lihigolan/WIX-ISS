# WIX-ISS
Wix interview assignment

SRC DIR: iss

The run starts from __ init__.py

output file: union_data.csv

The code generates the 2 stored procedure:

 * calc_stat_and_update - calc daily avg statistics per city and updates city_stats_lihi
 * calc_union_table - calc union of all statics and creates new union table, which is deleted later.

The output generated file is attached, you can delete, it will be created/updated every run, as well as the tables and the procedures.

In the output file - appearance col is my addition (the daily avg per city)

## Dependencies:
packages I used (need to be (pip/pip3) install for run the program):

 * datetime
 * requests - pip3
 * json
 * csv
 * mysql.connector

The db credentials are hard coded (as your example)

## NOTE:
I think 'State pattern' will fit here, because each level depends and executes the next one. If I had to write in java, I probably would implement this pattern. I think Python Combines both scripts and OO so I didnt go with this pattern in this case - (made it more scripted), but I dont know what is better, I really think it depends on programin language .....

Tell me if there are any issues.

Thanks, Lihi

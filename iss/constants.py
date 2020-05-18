URL = "URL"
PARAMS = "params"
PASSES = "passes"
LATITUDE = "latitude"
LATITUDE__PARAM = "lat"
LONGITUDE = "longitude"
LONGITUDE_PARAM = "lon"
NUMBER_PARAM = "n"
RESPONSE = "response"

CONFIG_CITIES_PATH = "config/config_cities.json"
CONFIG_WEB_PATH = "config/config_web"

TABLE_ORBITAL = "orbital_data_lihi"
TABLE_STATS = "city_stats_lihi"
TABLE_UNION = "union_table"
PROCEDURE_STAT_NAME = "calc_stat_and_update"
PROCEDURE_UNION_NAME = "calc_union_table"
CITY = "city"
DATE = "UTCdate"
DURATION = "duration"
AVG_APPEARANCE = "appearance"

RISE_TIME = "risetime"
POPULATION = "population"
MAX_TEMP = "max_temperature"
MIN_TEMP = "min_temperature"
UPDATE_DATE="update_date"
CSV_FILE_NAME = "union_data"
OK = 200
ALR_EXIST = "already exists"

##############################################

SQL_STAT_PROC = "CREATE PROCEDURE " + PROCEDURE_STAT_NAME + "() BEGIN " \
    "CREATE TABLE tmp ( " \
    "city varchar(255), " \
    "appearance double" \
    ");" \
    "insert into tmp " \
    "select city ,avg(appearance) as appearance " \
    "from (select orbital_data_lihi.city,count(orbital_data_lihi.city) " \
    "as appearance , cast(orbital_data_lihi.UTCdate as date) as dt " \
    "from orbital_data_lihi group by cast(orbital_data_lihi.UTCdate as date), " \
    "orbital_data_lihi.city order by orbital_data_lihi.city asc) as tmp_tbl  group by city;" \
    "update city_stats_lihi csl," \
    "tmp " \
    "SET " \
    "csl.appearance= tmp.appearance " \
    "WHERE " \
    "csl.city= tmp.city;" \
    "" \
    "DROP TABLE tmp;" \
    "end;"

SQL_UNION_PROC= "CREATE PROCEDURE " + PROCEDURE_UNION_NAME + "() BEGIN " \
                                                       "CREATE TABLE union_table (" \
                "city varchar(255)," \
                "population int," \
                "max_temperature int," \
                "min_temperature int," \
                "update_date DATETIME," \
                "appearance double" \
                ");" \
                " INSERT INTO union_table (city,population,max_temperature,min_temperature,update_date)" \
                " SELECT * FROM (SELECT * FROM(SELECT * FROM(SELECT * FROM city_stats_beer_sheva csbs " \
                "union all  select * from city_stats_eilat cse ) as beer_eilat" \
                " union all select * FROM city_stats_haifa csh) as haifa" \
                " union all select * from city_stats_tel_aviv ) as tlv;" \
                " update union_table ut,city_stats_lihi csl SET ut.appearance =  csl.appearance WHERE csl.city= ut.city;" \
                                                             "end;"

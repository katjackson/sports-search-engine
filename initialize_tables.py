import csv
import psycopg2

conn = psycopg2.connect("dbname=sports user=kathrynjackson host=/tmp/")
cur = conn.cursor()

cur.execute("""CREATE TABLE stats (player_id varchar, name varchar(25),
            rush_attempts varchar, rush_yds varchar, rush_avg varchar,
            rush_td varchar, receptions varchar, receive_yds varchar,
            receive_avg varchar, receive_td varchar, scrim_plays varchar,
            scrim_yds varchar, scrim_avg varchar, scrim_td varchar)""")

sql_code = """INSERT INTO stats (player_id, name, rush_attempts, rush_yds,
            rush_avg, rush_td, receptions, receive_yds, receive_avg,
            receive_td, scrim_plays, scrim_yds, scrim_avg, scrim_td) VALUES (
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""

with open('nebraska.csv') as f:
    reader = csv.reader(f)
    a_line_after_header = next(reader)
    another_line_after_header = next(reader)
    another_line_after_header = next(reader)
    for row in reader:
        print(row)
        cur.execute(sql_code, (row[0], row[1], row[2], row[3], row[4],
                    row[5], row[6], row[7], row[8], row[9], row[10], row[11],
                    row[12], row[13]))


sql_code = "INSERT INTO players VALUES ({}, '{}', {})"

with open('nebraska.csv') as f:
    reader = csv.reader(f)
    a_line_after_header = next(reader)
    another_line_after_header = next(reader)
    another_line_after_header = next(reader)
    for row in reader:
        rk = row[0]
        name = row[1]
        cur.execute(sql_code.format(rk, name, rk))

cur.execute("""CREATE TABLE scrimmage (player_id integer, plays integer,
            yds integer, avg numeric, td integer)""")

sql_code = "INSERT INTO scrimmage VALUES ({}, {}, {}, {}, {})"

with open('nebraska.csv') as f:
    reader = csv.reader(f)
    skip_line = next(reader)
    skip_line = next(reader)
    skip_line = next(reader)
    for row in reader:
        cur.execute(sql_code.format(row[0], row[-4], row[-3], row[-2],
                                    row[-1]))

cur.execute("""CREATE TABLE rushing (player_id integer, attempts integer,
            yds integer, avg numeric, td integer)""")

sql_code = "INSERT INTO rushing VALUES ({}, {}, {}, {}, {})"

with open('nebraska.csv') as f:
    reader = csv.reader(f)
    skip_line = next(reader)
    skip_line = next(reader)
    skip_line = next(reader)
    for row in reader:
        if row[2] != '':
            # print(sql_code.format(row[0], row[2], row[3], row[4], row[5]))
            cur.execute(sql_code.format(row[0], row[2], row[3], row[4],
                                        row[5]))

cur.execute("""CREATE TABLE receiving (player_id integer, recept integer,
            yds integer, avg numeric, td integer)""")

sql_code = "INSERT INTO receiving VALUES ({}, {}, {}, {}, {})"

with open('nebraska.csv') as f:
    reader = csv.reader(f)
    skip_line = next(reader)
    skip_line = next(reader)
    skip_line = next(reader)
    for row in reader:
        if row[6] != '':
            # print(sql_code.format(row[0], row[6], row[7], row[8], row[9]))
            cur.execute(sql_code.format(row[0], row[6], row[7], row[8],
                                        row[9]))


conn.commit()
cur.close()
conn.close()

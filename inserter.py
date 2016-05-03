import csv
import psycopg2
import argparse

sql_code = """INSERT INTO stats (player_id, name, rush_attempts, rush_yds,
            rush_avg, rush_td, receptions, receive_yds, receive_avg,
            receive_td, scrim_plays, scrim_yds, scrim_avg, scrim_td) VALUES
            (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""


def insert_sample(sample):
    conn = psycopg2.connect("dbname=sports user=kathrynjackson host=/tmp/")
    cur = conn.cursor()

    sample_rows = []

    if '.csv' in sample:
        f = open(sample)
        reader = csv.reader(f)
        for row in reader:
            sample_rows.append(row)
        f.close()
    else:
        sample_rows = [sample]

    for row in sample_rows:
        cur.execute(sql_code, (row[0], row[1], row[2], row[3], row[4],
                    row[5], row[6], row[7], row[8], row[9], row[10], row[11],
                    row[12], row[13]))

    conn.commit()
    cur.close()
    conn.close()
    return True


def main():

    if args.add:
        insert_sample(args.add)
    else:
        data = input("Enter a row of stats for the database:")
        data = data.split(',')
        insert_sample(data)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
                            description='Insert stats into football database')
    parser.add_argument('--add', type=str, help='Add data from one clean file')
    args = parser.parse_args()
    main()

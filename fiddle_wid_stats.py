import psycopg2
import argparse
from inserter import insert_sample

conn = psycopg2.connect("dbname=sports user=kathrynjackson host=/tmp/")
cur = conn.cursor()

stats_keys = ['Player ID', 'Name', 'Rush Attempts', 'Rush Yds', 'Rush Avg Yds',
              'Rush TD', 'Receptions', 'Receiving Yds', 'Receiving Avg Yds',
              'Receiving TD', 'Scrimmage Plays', 'Scrimmage Yds',
              'Scrimmage Avg Yds', 'Scrimmage TD']


def first_prompt():
    print("What would you like to do with your database?")
    print("1. View stats for a player")
    print("2. Enter stats for a new player")
    # print("3. Edit existing entry")
    action = input("Enter 1 or 2: ")
    if int(action) in [1, 2]:
        return int(action)
    else:
        first_prompt()


def run_program(action):
    if action == 1:
        find_player_info(get_name())
    else:
        insert_sample(get_new_stats())


def get_new_stats():
    new_stats = []
    print("Let's see what you know.")
    for key in stats_keys:
        new_stats.append(input("{}: ".format(key)))
    return new_stats


def get_name():
    name = input("Who do you want to lookup? ")
    if is_valid_input(name):
        return name
    else:
        print("Please enter a valid name.")
        get_name()


def is_valid_input(name):
    cur.execute("SELECT * FROM stats;")
    data = cur.fetchall()
    for entry in data:
        if name in entry:
            return True


def find_player_info(name):
    cur.execute("SELECT * FROM stats WHERE name = '{}';".format(name))
    stats = cur.fetchone()
    stats_dict = {key: stats[i] for i, key in enumerate(stats_keys) if stats[i] != ''}
    for key in sorted(stats_dict.keys()):
        print(key, ": ", stats_dict[key])
    print('\n')


def is_not_finished():
    response = input("Are you done here? Y/n\n")
    return response.lower() == 'n'

def main():

    if args.add:
        insert_sample(args.add)

    elif args.view:
        find_player_info(args.view)

    else:
        action = first_prompt()
        run_program(action)

        if is_not_finished():
            main()

    cur.close()
    conn.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='''View/Insert player data
                                     into football database''')
    parser.add_argument('--add', type=str, help='Add stats for new player(s)')
    parser.add_argument('--view', type=str, help='View an entry by name')
    args = parser.parse_args()
    main()

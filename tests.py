from inserter import *
from fiddle_wid_stats import *

conn = psycopg2.connect("dbname=sports user=kathrynjackson host=/tmp/")
cur = conn.cursor()


def test_inserter_csv():
    x = insert_sample('nebraska_test.csv')
    assert x


def test_inserter_list():
    x = insert_sample(['40', 'Turner Gill', '109', '531', '4.9', '11', '', '',
                       '', '', '109', '531', '4.9', '11'])
    assert x


# def test_find_info():
#     find_player_info('Jim Thompson')
#     assert

def test_valid():
    assert is_valid_input('Jim Thompson')
    assert not is_valid_input('Jim Henson')

cur.close()
conn.close()

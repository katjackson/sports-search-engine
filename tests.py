from inserter import *

conn = psycopg2.connect("dbname=sports user=kathrynjackson host=/tmp/")
cur = conn.cursor()


def test_inserter_csv():
    x = insert_sample('nebraska_test.csv')
    assert x


def test_inserter_list():
    x = insert_sample([['40', 'Turner Gill', '109', '531', '4.9', '11', '', '',
                        '', '', '109', '531', '4.9', '11'],
                      ['41', 'Mike Rozier', '275', '2148', '7.8', '29', '10',
                       '106', '10.6', '0', '285', '2254', '7.9', '29']])
    assert x

cur.close()
conn.close()

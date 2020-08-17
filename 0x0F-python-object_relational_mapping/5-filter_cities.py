#!/usr/bin/python3
"""how to use mysql client and compare it so sql alchemy"""
if __name__ == '__main__':
    import sys
    import MySQLdb
    args_ = sys.argv
    # print(args_)

    db = MySQLdb.connect(user=args_[1], passwd=args_[2], db=args_[3])
    c = db.cursor()
    str_ = """SELECT cities.name FROM cities 
    WHERE cities.state_id IN ( SELECT states.id FROM states WHERE states.name = '{}')
    """.format(args_[4])
    c.execute(str_)
    query_rows = c.fetchall()
    print("{}{}{}".format('', '', query_rows[0][0]), end="")
    for row in query_rows[1:]:
        print("{}{}{}".format(',', ' ', row[0]), end="")
    print()
    c.close()
    db.close()

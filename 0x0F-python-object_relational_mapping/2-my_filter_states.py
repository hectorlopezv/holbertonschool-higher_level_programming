#!/usr/bin/python3
"""how to use mysql client and compare it so sql alchemy"""
if __name__ == '__main__':
    import sys
    import MySQLdb
    args_ = sys.argv
    # print(args_)

    db = MySQLdb.connect(user=args_[1], passwd=args_[2], db=args_[3])
    c = db.cursor()
    str_ = """
SELECT * FROM states 
WHERE states.name LIKE BINARY '{}'
ORDER BY states.id ASC
""".format(args_[4])
    c.execute(str_)
    query_rows = c.fetchall()
    for row in query_rows:
        print(row)

#!/usr/bin/python3
"""how to use mysql client and compare it so sql alchemy"""
if __name__ == '__main__':
    import sys
    import MySQLdb
    args_ = sys.argv
    # print(args_)

    db = MySQLdb.connect(user=args_[1], passwd=args_[2], db=args_[3])
    c = db.cursor()
    c.execute(
        """
        SELECT states.id, states.name FROM states 
        WHERE states.name REGEXP '^N' ORDER BY states.id ASC""")
    result = c.fetchall()
    if result:
        for row in c.fetchall():
            print(row)

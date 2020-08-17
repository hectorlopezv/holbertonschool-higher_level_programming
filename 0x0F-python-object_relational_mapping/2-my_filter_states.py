"""how to use mysql client and compare it so sql alchemy"""
if __name__ == '__main__':
    import sys
    import MySQLdb
    args_ = sys.argv
    # print(args_)

    db = MySQLdb.connect(user=args_[1], passwd=args_[2], db=args_[3])
    c = db.cursor()
    c.execute("""
SELECT * FROM states ORDER BY states.id ASC
WHERE states.name = {}""".format(args_[4]))
    query_rows = c.fetchall()
    for row in query_rows:
        print(row)

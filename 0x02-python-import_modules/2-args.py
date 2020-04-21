#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argv = argv[1:]
    count = 0
    if len(argv) == 0:
        print("0 arguments.")
        pass
    elif len(argv) == 1:
        print("1 argument:")
        print("1: {}".format(argv[0]))
    else:
        print("{} arguments:".format(len(argv)))
        for i in argv:
            count += 1
            print("{}: {}".format(count, i))

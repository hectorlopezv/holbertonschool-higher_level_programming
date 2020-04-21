#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    for per in dir():
        if per[1] != "_":
            print(per)

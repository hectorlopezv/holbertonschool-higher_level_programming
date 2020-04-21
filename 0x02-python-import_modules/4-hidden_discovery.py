#!/usr/bin/python3
if __name__ == '__main__':
    namespac = dir('hidden_4')
    for i in namespac:
        if '__' in i:
            continue
        print(i)

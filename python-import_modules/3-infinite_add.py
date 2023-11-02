#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    argc = len(argv) - 1

    if argc == 0:
        print("{0}".format(argc))
    else:
        sum = 0
        for i in range(argc):
            sum = sum + int(argv[i + 1])
        print("{}".format(sum))

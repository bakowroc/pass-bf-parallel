import sys

from master import Master

if __name__ == '__main__':
    master = Master(sys.argv[1])
    master.start()

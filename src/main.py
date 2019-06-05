import sys

from master import Master

NODES = ['10.11.220.20', '10.11.220.21', '10.11.220.22', '10.11.220.23']
USE_NODES = sys.argv[1] | 4
PASSWORD = sys.argv[2] | '9zZ'

if __name__ == '__main__':
    print(f'Running for {len(NODES[:USE_NODES])} nodes: {PASSWORD}')
    master = Master(PASSWORD, nodes=NODES[:USE_NODES], partioning=1)
    master.start()

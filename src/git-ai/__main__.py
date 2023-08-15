import sys
import argparse
import subprocess as sp

if __name__ == '__main__':
    i = sp.call('git status', shell=True, stdout=sp.DEVNULL)
    if i != 0:
        sys.exit(1)

    diff = sp.check_output('git diff', shell=True).decode('utf-8')
    print(diff)
    
    # print all parameters
    print(sys.argv)
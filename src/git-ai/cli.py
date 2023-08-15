import sys
import argparse
import subprocess as sp

def arg_parse():
    parser = argparse.ArgumentParser(description='Git-AI, a tool to help you with your git workflow')
    


if __name__ == '__main__':
    sp.call('pwd', shell=True)
    # print all parameters
    print(sys.argv)
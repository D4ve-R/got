import argparse
import sys
from transformers import pipeline

generator = pipeline(model="mamiksik/T5-commit-message-generation")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--diff", type=str, help="git diff output", default="")

    args = parser.parse_args()
    diff = args.diff

    # use stdin if it's full                                                        
    if not sys.stdin.isatty() and not diff:
        diff = sys.stdin.read()
        #truncate to 512 tokens
        print(len(diff))
        if len(diff) > 512:
            diff = diff[:512]

    print(generator(diff))



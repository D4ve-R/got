#!/usr/bin/env python3
import argparse
import sys
from transformers import pipeline
from backend.client import Client

class HfClient(Client):
    def __init__(self, model="mamiksik/T5-commit-message-generation", device="cpu"):
        super().__init__()
        self.pipe = pipeline(model=model, device=device)

    def __call__(self, data):
        return self._generate(data)
    
    def _generate(self, data):
        return self.pipe(data)[0]['generated_text']

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--diff", type=str, help="git diff output", default="")
    parser.add_argument("-g", "--gpu" , action="store_true", help="use gpu")

    args = parser.parse_args()
    diff = args.diff
    device = "cuda" if args.gpu else "cpu"
    pipe = HfClient(device=device)
                                                       
    if not sys.stdin.isatty() and not diff:
        diff = sys.stdin.read()
        len = len(diff)
        if len > 512:
            print(f"diff too long, {len} characters")
            diff = diff[:512]

    print(pipe(diff))
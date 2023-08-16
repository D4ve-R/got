#!/usr/bin/env python3
import argparse
import sys
import os
from transformers import pipeline
from .client import Client

class HfClient(Client):
    def __init__(self, model="mamiksik/T5-commit-message-generation", device=None):
        super().__init__()
        if not device:
            import torch
            device = "cuda" if torch.cuda.is_available() else "cpu"
        self.pipe = pipeline(model=model, device=device)

    def __call__(self, data):
        return self._generate(data)
    
    def _generate(self, data):
        l = len(data)
        if l > 512:
            print(f"diff too long, {l} characters")
            data = data[:512]
        os.environ["TOKENIZERS_PARALLELISM"] = "false"
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

    print(pipe(diff))

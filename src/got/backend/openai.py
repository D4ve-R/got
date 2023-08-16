#!/usr/bin/env python3
import sys
import os
import requests
from backend.client import Client

class GptClient(Client):
    def __init__(self, api_key="", model="gpt-3.5-turbo", temp=0.5):
        super().__init__()
        self.api_key = api_key
        self.model = model
        self.temp = temp
        if not self.api_key:
            if 'OPENAI_API_KEY' in os.environ:
                self.api_key = os.environ['OPENAI_API_KEY']
            else:
                try:
                    with open(os.path.join(os.environ['HOME'], '.config', 'got', 'oa_token'), 'r') as f:
                        self.api_key = f.read().strip()
                except:
                    key = input("Please enter your OpenAI API key: ").strip()
                    self.api_key = key
                    os.environ['OPENAI_API_KEY'] = key
                    path = os.path.join(os.environ['HOME'], '.config', 'got')
                    os.makedirs(path, exist_ok=True)
                    with open(os.path.join(path, 'token'), 'w') as f:
                        f.write(key)

    def __call__(self, data):
        return self._generate_commit_message(data)

    def _generate_commit_message(self, diff):
        messages = []
        prompt = f"Can you write a commit messages with maximum 72 characters describing the following output:\n\n{diff}"
        messages.append({"role": "user", "content": prompt})
        data = {
            "model": self.model,
            "messages": messages,
            "temperature": self.temp,
        }
        response = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers={"Authorization": f"Bearer {self.api_key}"},
            json=data,
        )

        if response.status_code != 200:
            print(response.text)
            sys.exit(1)

        response = response.json()
        return response['choices'][0]['message']['content']


if __name__ == "__main__":
    pipe = GptClient()
    diff = sys.stdin.read() if len(sys.argv) == 1 else sys.argv[1:].join(' ')
    print(pipe(sys.stdin.read()))

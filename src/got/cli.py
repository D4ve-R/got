import sys
import os
import subprocess
from backend.local import HfClient
from backend.openai import OpenAIClient

def _save_backend(backend):
    try:
        path = os.path.join(os.environ['HOME'], '.config', 'got')
        os.makedirs(path, exist_ok=True)
        with open(os.path.join(path, 'backend'), 'w') as f:
            f.write(backend)
    except Exception as e:
        print(e)

def _get_backend():
    try: 
        path = os.path.join(os.environ['HOME'], '.config', 'got', 'backend')
        with open(path, 'r') as f:
            return f.read()
    except Exception as e:
        print(e)
        return "local"

def _generate_commit_message(diff, backend=None):
    if not backend:
        backend = _get_backend()

    client = None
    if backend == "local" or backend == "hf":
        client = HfClient()
    elif backend == "openai":
        client = OpenAIClient()

    else: 
        print("Using default backend: local")
        backend = "local"
        client = HfClient()

    _save_backend(backend)
    return client(diff)

def sanitize_commit_message(message):
    # remove quotes if they are the first and last character
    if message[0] == '"':
        message = message[1:]
    if message[-1] == '"':
        message = message[:-1]
    return message

def got(*args, backend=""):
    try:
        if args == ("commit",):
            diff = subprocess.check_output(["git", "diff", "--staged"]).decode("utf-8")
            if not diff:
                print("No changes staged.")
                sys.exit(0)

            commit_message = _generate_commit_message(diff, backend=backend)
            commit_message = sanitize_commit_message(commit_message)

            print(f"Generated commit message:\n\n{commit_message}")
            if input("Commit? [Y/n] ").lower() == "n":
                commit_message = input("Please enter commit message: ")

            commit_message = f'"{commit_message}"'
            subprocess.run(["git", "commit", "-m", commit_message])
        else:
            subprocess.run(["git"] + list(args))
    except KeyboardInterrupt:
        print("\nAbort mission!")
        sys.exit(1)


if __name__ == "__main__":
    got(*sys.argv[1:])

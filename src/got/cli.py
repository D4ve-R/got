import sys
import subprocess
from backend.local import HfClient

def generate_commit_message(diff):
    client = HfClient()
    return client(diff)

def got(*args):
    if args == ("commit",):
        diff = subprocess.check_output(["git", "diff", "--staged"]).decode("utf-8")
        if not diff:
            print("No changes staged.")
            sys.exit(0)

        commit_message = generate_commit_message(diff)

        print(f"Generated commit message:\n\n{commit_message}")
        if input("Commit? [Y/n] ").lower() == "n":
            commit_message = input("Please enter commit message: ")
        
        commit_message = f'"{commit_message}"'
        subprocess.run(["git", "commit", "-m", commit_message])
    else:
        subprocess.run(["git"] + list(args))


if __name__ == "__main__":
    got(*sys.argv[1:])

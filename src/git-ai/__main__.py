import os
import subprocess
import openai

# check env for openai api key, if not present check in $HOME/.config/got/credentials, if not present ask for it
if 'OPENAI_API_KEY' in os.environ:
    openai.api_key = os.environ['OPENAI_API_KEY']
else:
    try:
        with open(os.path.join(os.environ['HOME'], '.config', 'got', 'token'), 'r') as f:
            openai.api_key = f.read().strip()
    except FileNotFoundError:
        key = input("Please enter your OpenAI API key: ").strip()
        openai.api_key = key
        os.environ['OPENAI_API_KEY'] = key
        path = os.path.join(os.environ['HOME'], '.config', 'got')
        os.makedirs(path, exist_ok=True)
        with open(os.path.join(path, 'token'), 'w') as f:
            f.write(key)


def generate_commit_message(diff):
    messages = [
        {"role": "system", "content": "Generate good commit messages based on git diff, output must not exceed 72 characters and must be only the message without additional text."},
    ]
    # Call OpenAI GPT-3 to generate a commit message based on the diff
    prompt = f"Generate a commit message based on the following:\n{diff}"
    messages.append({"role": "user", "content": prompt})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
    )
    return response.choices[0].message.content

def git_commit(*args):
    if args == ("commit",):
        diff = subprocess.check_output(["git", "diff"]).decode("utf-8")
        commit_message = generate_commit_message(diff)
        subprocess.run(["git", "commit", "-m", commit_message])
    else:
        subprocess.run(["git"] + list(args))

if __name__ == "__main__":
    import sys
    git_commit(*sys.argv[1:])

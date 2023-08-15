import openai
openai.api_key = "sk-..."

content = """
        Don't answer anything that is not absolutely necessary.
        A commit message has maximum 72 characters and is formatted as follows:
        <type>: <subject>
        Where type can be one of the following:
        feat: a new feature
        fix: a bug fix
        docs: changes to documentation
        style: formatting, missing semi colons, etc; no code change
        refactor: refactoring production code
        test: adding tests, refactoring test; no production code change
        Write a commit message for the following output of git diff:
    """

messages = [
    {"role": "user", "content": content},
]

# create a chat completion
chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)

# print the chat completion
print(chat_completion.choices[0].message.content)
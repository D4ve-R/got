import openai
openai.api_key = "sk-..."

# list models
models = openai.Model.list()

# print the first model's id
print(models.data[0].id)

messages = [
    {"role": "user", "content": "Hello world"}
]

# create a chat completion
chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)

# print the chat completion
print(chat_completion.choices[0].message.content)
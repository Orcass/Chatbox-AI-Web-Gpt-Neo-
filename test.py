import openai

openai.api_key = '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'

response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "user", "content": "Hello, how are you?"}
    ]
)

print(response['choices'][0]['message']['content'].strip())

import openai

openai.api_key = "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"

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Give me 3 ideas for apps I could build with openai apis "}])
print(completion.choices[0].message.content)
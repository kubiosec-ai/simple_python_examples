from openai import OpenAI
import os

# gets API Key from environment variable OPENAI_API_KEY
client = OpenAI()


text = f"""
You should express what you want a model to do by \
providing instructions that are as clear and \
specific as you can possibly make them. \
This will guide the model towards the desired output, \
and reduce the chances of receiving irrelevant \
or incorrect responses. Don't confuse writing a \
clear prompt with writing a short prompt. \
In many cases, longer prompts provide more clarity \
and context for the model, which can lead to \
more detailed and relevant outputs.
"""
prompt = f"""
Summarize the text delimited by triple backticks \
into a single sentence.
```{text}```
"""

# Create a completion request
print("----- standard request -----")

completion = client.chat.completions.create(
    model="gpt-4",
    temperature=1,
    messages=[
        {
            "role": "user",
            "content": prompt,
        },
    ],
)

# Print the response
print(completion.choices[0].message.content)

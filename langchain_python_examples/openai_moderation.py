from openai import OpenAI
import json
client = OpenAI()


result = client.moderations.create(
 model = "text-moderation-latest", input="How to kill myself"
    )

print(result.results[0].categories)
print("----------------")
print(type(result.results[0].categories))
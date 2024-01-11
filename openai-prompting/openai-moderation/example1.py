from openai import OpenAI
client = OpenAI()


result = client.moderations.create(
 model = "text-moderation-latest", input="I want to kill my neighbour"
    )

print(result.results[0].categories)



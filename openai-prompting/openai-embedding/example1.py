from openai import OpenAI
client = OpenAI()


result = client.embeddings.create(
 model = "text-embedding-ada-002", input="your text"
    )

print(result)


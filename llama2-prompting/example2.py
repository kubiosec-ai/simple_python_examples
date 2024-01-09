from llama_cpp import Llama

# Initialize the Llama instance with the path to the downloaded model
llm = Llama(model_path="./models/llama-2-7b-chat.Q8_0.gguf",
            n_ctx = 2048,            # context window size
            )        

# create a text prompt
prompt = "Q: What are the names of the days of the week? A:"

# generate a response (takes several seconds)
output = llm(prompt)

# display the response
print(output["choices"][0]["text"])

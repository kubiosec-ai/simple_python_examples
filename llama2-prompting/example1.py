from llama_cpp import Llama

# Initialize the Llama instance with the path to the downloaded model
llm = Llama(model_path="./models/llama-2-7b-chat.Q8_0.gguf")


output = llm("what is a kubernetes pod", 
            max_tokens=500,
            stop=["###"], 
            temperature=0.1,
            top_p=0.2,
            top_k=10)

print(output)

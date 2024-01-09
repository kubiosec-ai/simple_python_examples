# load the large language model file
from llama_cpp import Llama
LLM = Llama(model_path="./models/llama-2-7b-chat.ggmlv3.q8_0.bin",
              n_ctx = 2048,            # context window size
              n_gpu_layers = 1,        # enable GPU
              use_mlock = True)        # enable memory lock so not swap

# create a text prompt
prompt = "Q: What are the names of the days of the week? A:"

# generate a response (takes several seconds)
output = LLM(prompt)

# display the response
print(output["choices"][0]["text"])

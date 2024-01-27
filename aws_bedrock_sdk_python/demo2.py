import boto3
import json
import os
import botocore
from botocore.config import Config


# Make sure you're using a region that is supporting BedRock
os.environ["AWS_DEFAULT_REGION"] = "us-east-1"

br_client = boto3.client('bedrock-runtime')

def generate(prompt, temperature = 0):
    body = json.dumps({
        "prompt": prompt,
        "temperature": temperature,
        "top_p": 0.9,
        "max_gen_len":512
    })
    response = br_client.invoke_model(body=body, modelId='meta.llama2-13b-chat-v1')
    response = json.loads(response.get('body').read())
    response = response.get('generation')
    return response

def prompt_with_system_message(prompt, system_message):
    prompt = f"""
    <s>[INST] <<SYS>>{system_message}<</SYS>>

    User: {prompt}
    Agent:[/INST]
    """
    return prompt

class LlamaChatbot:
    def __init__(self, system_message):
        self.system_message = system_message
        self.conversation_history = []  # list of tuples (user_msg, agent_response)

    def chat(self, user_msg):
        # Generate the prompt using the conversation history and the new user message
        prompt = prompt_with_examples(user_msg, self.system_message, self.conversation_history)
        
        # Get the model's response
        agent_response = generate(prompt)

        # Store this interaction in the conversation history
        self.conversation_history.append((user_msg, agent_response))

        return agent_response

    def reset(self):
        # Clear conversation history
        self.conversation_history = []


def prompt_with_examples(prompt, system_message, examples=[]):
    
    # Start with the initial part of the prompt with system message
    full_prompt = f"<s>[INST] <<SYS>>{system_message}<</SYS>>\n"

    # Add each example to the prompt
    for user_msg, agent_response in examples:
        full_prompt += f"{user_msg} [/INST] {agent_response} </s><s>[INST]"

    # Add the main prompt and close the template
    full_prompt += f"{prompt} [/INST]"

    return full_prompt



shoes = [
    {
        "model": "Sky Glider",
        "type": "Running", 
        "features": {
            "upper": "Mesh",
            "sole": "EVA foam",
            "lacing": "Quick-tie",
            "drop": "8mm",
            "color": "Blue with yellow accents"
        },
        "usps": ["Lightweight", "Responsive cushioning", "Seamless upper"],
        "price": 119.95,
        "internal_id": "SG123",
        "weight": "220g",
        "manufacturer_location": "Vietnam"
    },
    {   
        "model": "Trail Trekker",
        "type": "Hiking",
        "features": {
            "upper": "Synthetic leather",
            "sole": "Rubber lug", 
            "lacing": "Traditional",
            "drop": "12mm",
            "color": "Khaki green"
        },
        "usps": ["Rugged construction", "Super grippy sole", "Waterproof"], 
        "price": 129.99,
        "internal_id": "TT321",
        "weight": "340g",
        "manufacturer_location": "China"
    },
    {
        "model": "Marathon Master",
        "type": "Racing",
        "features": {
            "upper": "Mesh",
            "sole": "Carbon fiber plate",
            "lacing": "Speed laces",
            "drop": "6mm",
            "color": "Neon yellow and black"
        },
        "usps": ["Maximizes energy return", "Lightning fast", "Seamless comfort"],
        "price": 179.50, 
        "internal_id": "MM111",
        "weight": "180g",
        "manufacturer_location": "USA"
    }
]




system_message = """
You are a friendly chatbot knowledgeable about shoes. \
When asked about specific shoe models or features, you try to provide accurate and helpful answers. \
Your goal is to assist and inform potential customers to the best of your ability.
"""

chatbot = LlamaChatbot(system_message)

print(chatbot.chat("Can you tell me about the latest models?"))


chatbot.reset()




system_message = f"""
You are a friendly chatbot knowledgeable about these bicycles from Cloudrunners Shoes {shoes}. \
When asked about specific shoe models or features, you try to provide accurate and helpful answers. \
Your goal is to assist and inform potential customers to the best of your ability.
"""

chatbot = LlamaChatbot(system_message)


print(chatbot.chat("Can you tell me about the latest models?"))

print(chatbot.chat("How much do each of the models cost?"))

print(chatbot.chat("I'm torn between the Sky Glider and the Marathon Master, how should I decide which is best or me?"))

print(chatbot.chat("I'm torn between the Marathon Master and the Trail Trekker, how should I decide which is best or me?"))

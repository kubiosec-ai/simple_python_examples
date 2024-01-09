client = OpenAI()

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(model=model,
    messages=messages,
    temperature=0)
    return response.choices[0].message.content

fact_sheet_chair = """
// Define the setRoutes function that takes the 'app' object as a parameter
function setRoutes(app) {
  app.get('/', (req, res) => {
    res.send('Welcome to the homepage!');
  });

  app.get('/route2', (req, res) => {
    res.send('Welcome to the route2!');
  });

}

// Export the setRoutes function
module.exports = {
  setRoutes,
};
"""
prompt = f"""
My code is in betweeen the triple backticks.
Can you document it for me?

My code ```{fact_sheet_chair}```
"""
response = get_completion(prompt)
print(response)

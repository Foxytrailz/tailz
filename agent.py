import os
import openai

# Make sure you set your OpenAI API key in your environment first, e.g.:
# Windows (PowerShell): $env:OPENAI_API_KEY="your_api_key_here"
# Mac/Linux (bash): export OPENAI_API_KEY="your_api_key_here"

openai.api_key = os.getenv("OPENAI_API_KEY")

def run_agent(task):
    response = openai.ChatCompletion.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "You are a helpful AI agent."},
            {"role": "user", "content": task}
        ]
    )
    return response['choices'][0]['message']['content']

if __name__ == "__main__":
    while True:
        user_input = input("Ask me something (or type quit): ")
        if user_input.lower() == "quit":
            break
        print(run_agent(user_input))

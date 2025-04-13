from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables (e.g., OPENAI_API_KEY)
load_dotenv()

# Initialize OpenAI client
client = OpenAI()

# Define your conversation messages
messages = [
    {
        "role": "system",
        "content": """You are a helpful assistant that can answer questions and provide information.
You will be given a question, and you should respond with a clear and concise answer.

Example:
User: What is the capital of France?
Assistant: The capital of France is Paris. FunFact: The Eiffel Tower is located in Paris.
User: What is the capital of Germany?
Assistant: The capital of Germany is Berlin. FunFact: The Berlin Wall once divided the city into East and West."""
    },
    {
        "role": "user",
        "content": "What is 2*2?"
    }
]


# Chat loop
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break

    # Add user message to history
    messages.append({"role": "user", "content": user_input})

    # Get response from OpenAI
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages
    )

    # Extract assistant message
    reply = response.choices[0].message.content
    print(f"Assistant: {reply}\n")

    # Add assistant response to history
    messages.append({"role": "assistant", "content": reply})

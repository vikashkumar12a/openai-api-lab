from openai import OpenAI
from dotenv import load_dotenv
import os

# Load variables from .env
load_dotenv()

# Create OpenAI client
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


# Send request to the model
question = input("Enter your question: ")

response = client.responses.create(
    model="gpt-5.6-luna",
    input=question
)


# Display the response
print(response.output_text)
print("GitHub connection successful!")
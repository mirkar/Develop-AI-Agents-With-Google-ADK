#!/usr/bin/env python3
import os
from pathlib import Path
from dotenv import load_dotenv
from google import genai

# Load environment variables from .env file
load_dotenv()

# Use the API key from the GOOGLE_API_KEY environment variable
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

# List all models
for model in client.models.list():
    print(f"Model: {model.name}")
    print(f"Capabilities: {model.supported_actions}")
    print(f"Description: {model.description}")
    print(f"Input Token Limit: {model.input_token_limit}")
    print(f"Display Name: {model.display_name}")
    print(f"Output Token Limit: {model.output_token_limit}")
    print("-" * 20)
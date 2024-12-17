import os
from dotenv import load_dotenv
import google.generativeai as genai

def main():
    # Load environment variables
    load_dotenv()
    
    # Configure the Gemini API
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("API key must be provided in GOOGLE_API_KEY environment variable")
    
    genai.configure(api_key=api_key)
    
    # List all available models
    print("Available models:")
    for model in genai.list_models():
        print(f"- {model.name}")
        print(f"  Supported generation methods: {model.supported_generation_methods}")
        print()

if __name__ == "__main__":
    main() 
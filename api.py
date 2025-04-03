import openai
import requests
from groq import Groq

# 🔥 Your Groq API Key
GROQ_API_KEY = "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"

client = Groq(api_key=GROQ_API_KEY)

# Function to query Groq's AI models
def query_groq(prompt, persona):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": persona,
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
        model="llama3-70b-8192",  # Using the LLaMA-3 70B model for responses
        temperature=0.7,
        top_p=1,
    )
    return chat_completion.choices[0].message.content

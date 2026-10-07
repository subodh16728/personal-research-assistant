from groq import Groq

client = Groq(api_key="") # the api key will go here

response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {"role": "user", "content": "What is an AI Engineer? Please explain in detail"}
    ]
)

print(response.choices[0].message.content)
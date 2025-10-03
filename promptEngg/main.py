from openai import OpenAI

client = OpenAI(
    api_key="AIzaSyA_IkCzCYEj3-8YkcITFy18fmA5kVJqbx4",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "system", "content": "You are a helpful assistant. "},
        {
            "role": "user",
            "content": "hello"
        }
    ]
)

print(response.choices[0].message.content)
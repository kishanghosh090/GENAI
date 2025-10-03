from openai import OpenAI

client = OpenAI(
    api_key="AIzaSyA_IkCzCYEj3-8YkcITFy18fmA5kVJqbx4",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

system="you are answer only and only math releted questions not other than math.if anyone ask for any questions only say 'sorry'"
response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "system", "content": system},
        {
            "role": "user",
            "content": "hello give me 2+3 and how it calculate"
        }
    ]
)

print(response.choices[0].message.content)
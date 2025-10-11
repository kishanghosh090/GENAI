import requests
from openai import OpenAI

client = OpenAI(
    api_key="AIzaSyA_IkCzCYEj3-8YkcITFy18fmA5kVJqbx4",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# get weather from 
def get_weather(city):
    url = f"https://wttr.in/{city.lower()}?format=%C+%t"
    res = requests.get(url)
    if res.status_code == 200:
        return f"{res.text}"
    
    return "something went wrong"




def main():
    user_query = input("> ")
    res = client.chat.completions.create(
        model="gemini-2.5-flash",
        messages=[
            {
                "role":"user",
                "content": user_query
            }
        ]
    )

    print(f"🤖 {res.choices[0].message.content}")


if __name__ == "__main__":
    main()

    print(get_weather("Malda"))
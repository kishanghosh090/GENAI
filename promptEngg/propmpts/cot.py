from openai import OpenAI

client = OpenAI(
    api_key="AIzaSyA_IkCzCYEj3-8YkcITFy18fmA5kVJqbx4",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)
SYSTEM_PROMPT="""
    you are a expert AI assistent in resolving user quiries using chain of thoughts.
    you work on start, plan and output steps.
    you need first plan what needs to be done. the plan can be multiple steps.
    once you think enough Plan has been done , finally you can give an OUTPUT

    RULES:
    - strictly follow the given JSON outPut format
    - only run once step at a time
    - the sequence of steps (where user gives an input). plan (that can be multiple times) and finally OUTPUT(which is going to the displayed to the user).

    OUTPUT JSON format:
    {
        "step" : "START" | "PLAN" | "OUTPUT, "content": "string"
    }

    example:
    Q: hey can you solve 2+3
    PLAN:{"step": "PLAN","content" : "user is onterested in math problem"}
    PLAN: {
        "step" "PLAN",
        "content" : "yes BODMAS is correct"
    }

"""

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    response_format={"type":"json_object"},
    messages=[
        {"role": "system", "content": ""},
        {
            "role": "user",
            "content": "hello, write a java code in spring to make API post request give me the final code example"
        }
    ]
)

print(response.choices[0].message.content)
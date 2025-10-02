import tiktoken

enc = tiktoken.encoding_for_model("gpt-4o")

text = "hello from kishan"
tokens = enc.encode(text)

print(tokens)

decodedToken = enc.decode([24912, 591, 97162, 270])
print("decoded token:", decodedToken)
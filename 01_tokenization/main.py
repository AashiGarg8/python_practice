import tiktoken


enc = tiktoken.encoding_for_model("gpt-4o")
text = "Hey there! How are you doing today?"

tokens = enc.encode(text)

print (tokens)  # [25216, 1354, 0, 3253, 553, 481, 5306, 4044, 30]


#can we detokenize it?
decoded = enc.decode([25216, 1354, 0, 3253, 553, 481, 5306, 4044, 30])
print(decoded)

# now what happend is we give tokens to transformer model and it will generate some output tokens, we can decode those tokens to get the text back.
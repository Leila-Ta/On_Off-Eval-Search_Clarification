from time import sleep
import openai

openai.api_key = "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"

def chat_with_chatgpt(prompt):
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [{"role": "system", "content": prompt}],
        max_tokens = 100,
        n = 1,
        temperature = 0,
    )

    return response['choices'][0]['message']['content'] # Change this

file1 = open('/5GPTMain-Understandable28.txt', 'r')
f = open("/5GPTMain-Understandable28Predict.txt", "w")
Lines = file1.readlines()

for line in Lines:
    user_prompt = str(line)
    chatbot_response = chat_with_chatgpt(user_prompt)
    f.write(chatbot_response)
    f.write('\n')
    print(chatbot_response)
    sleep(4)
print("Done")

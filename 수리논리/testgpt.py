import openai

openai.api_key = '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'

messages = [ {"role": "system", "content":

              "You are a intelligent assistant."} ]

while True:
    message = input("User : ")
    if message:
        messages.append(

            {"role": "user", "content": message},

        )

        chat = openai.ChatCompletion.create(

            model="gpt-3.5-turbo", messages=messages

        )

    reply = chat.choices[0].message.content

    print(f"ChatGPT: {reply}")

    messages.append({"role": "assistant", "content": reply})
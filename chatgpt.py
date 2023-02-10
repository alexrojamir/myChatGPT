import openai 
openai.api_key = "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"
while True:
    pregunta = input("\n ¿Cual es tu pregunta?: ")

    if pregunta == "exit":
        break
    completion = openai.Completion.create(
        engine="text-davinci-003",
        prompt=pregunta,
        max_tokens=2048
    )
    print(completion.choices[0].text)
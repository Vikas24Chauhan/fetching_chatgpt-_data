import openai

API_KEY = "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"

openai.api_key = API_KEY


def generate_text(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    return response.choices[0].text.strip()


prompt = input("")
response = generate_text(prompt)

print(response)

import openai

def GoAskAI_ChatCompletion(prompt):
    """
    This GoAskAI API function is used to generate a response to a prompt from the AI model.
    """
    raw_return = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content" : prompt},
        ]
    )

    return raw_return['choices'][0]['message']['content']

if __name__ == '__main__':
    while True:
        prompt = input("\nenter a prompt for the AI model to respond to, or type 'exit' to stop:\n")
        if prompt == "exit":
            break
        print(GoAskAI_ChatCompletion(prompt))
    print("Good-bye!")
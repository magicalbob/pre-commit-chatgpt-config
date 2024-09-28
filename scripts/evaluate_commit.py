import openai
import sys
import os

def evaluate_code(code):
    openai.api_key = os.getenv("OPENAI_API_KEY")

    with open(code, "r") as file:
        # Read the file contents into a string
        try:
            file_changed = file.read()
        except:
            print(f"DEBUG: file {code} cannot be read.")
            exit(0)

    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant."
        },
        {
            "role": "user",
            "content": f"Evaluate the following Python code changes (include 'Looks good' in the response if acceptable):\n{file_changed}",
        },
    ]
    model_id = "gpt-3.5-turbo"
    response = openai.chat.completions.create(model=model_id, messages=messages)

    # Interpret the response from ChatGPT here
    print("vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv")
    print(messages)
    print(response)
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    answer = response.choices[0].message.content
    if "Looks good" in answer:
        return True
    else:
        return False


def main():
    # Read the code changes from the first command-line argument
    code = sys.argv[1]

    # Evaluate the code
    if evaluate_code(code):
        print("Commit approved by ChatGPT.")
    else:
        print("Commit rejected by ChatGPT.")
        sys.exit(1)


if __name__ == "__main__":
    main()

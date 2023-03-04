from flask import Blueprint, json, request
import openai
import os


chat = Blueprint('chat', __name__)
openai.api_key = "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"


@chat.route('/service', methods=['POST'])
@chat.route('/')
def getGpt():
    prompt = request.form['prompt']
    return gpt(prompt)


def gpt(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.6,
        max_tokens=700
    )

    # data = response["choices"][0]["text"]
    responseJson = str(os.path.dirname(__file__)) + "\\response.json"
    with open(responseJson, "w") as f:
        json.dump(response, f)

    return response["choices"][0]["text"]
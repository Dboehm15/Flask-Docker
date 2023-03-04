from flask import Blueprint, json, request
import openai
import os


chat = Blueprint('chat', __name__)
openai.api_key = "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"


@chat.route('/cli', methods=['POST'])
@chat.route('/')
def gpt():
    prompt = request.form['prompt']

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



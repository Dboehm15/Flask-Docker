from flask import Blueprint, request
from main.chatGPT.chatService import gpt
import random

recipe = Blueprint('recipe', __name__)


@recipe.route('/recipe', methods=['POST'])
@recipe.route('/')
def getRecipe():
    ingredients = [request.form['0'], request.form['1'], request.form['2'], request.form['3'], request.form['4']]
    theList = [
        "Give me a recipe using",
        "What goes good with"
    ]
    randomInt = random.randint(0, len(theList) - 1)
    prompt = str(theList[randomInt])

    for i in ingredients:
        prompt += " " + str(i)

    response = gpt(prompt)

    return response

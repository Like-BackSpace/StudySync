import google.generativeai as genai

# Configure the API key
genai.configure(api_key='AIzaSyB4C9dy-WK4HbatM47NNMhykDUJGuoHsRo')

# Create a model instance
model = genai.GenerativeModel('gemini-pro')

def tutor_response(user_question):
    system_prompt = """
    You are a dedicated AI tutor for college students.
    You only assist with academic subjects like Computer Science, Math, Physics, etc.
    Do not engage in unrelated conversations.
    Provide clear explanations, step-by-step solutions, and encourage learning.
    """

    # Combine system prompt and user question
    prompt = system_prompt + "\n\nStudent: " + user_question + "\n\nTutor:"

    response = model.generate_content(prompt)
    
    return response.text


from fastapi import FastAPI
from pydantic import BaseModel
from ai import tutor_response  # function from earlier

app = FastAPI()

class Question(BaseModel):
    question: str

@app.post("/ask")
def ask_tutor(q: Question):
    answer = tutor_response(q.question)
    return {"answer": answer}

from flask import Flask, request, jsonify
import nltk

app = Flask(__name__)

@app.route('/process', methods=['POST'])
def process():
    data = request.json
    text = data['param']
    # Call your Python function here
    result = processParagraph(text)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
 

from flask import flask,render_template
@app.route('/')
def home():
    return render_template('sample.html')

if __name__ == '__main__':
    app.run(debug=True)   
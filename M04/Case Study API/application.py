from flask import Flask
from flask import jsonify
import json

app = Flask(__name__)



        

@app.route('/')
def index():
    return 'Hello!'


@app.route('/books')
def get_books():
    with open('bookcontainer3.json') as f:
        book_data = json.load(f)
    return jsonify(book_data)
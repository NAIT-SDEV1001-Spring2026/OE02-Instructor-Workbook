from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to the Book Library API</h1>"

books = [
    {"title": "1984", "author": "George Orwell"},
    {"title": "The Hobbit", "author": "J.R.R. Tolkien"}
]

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)
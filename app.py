import requests
from flask import Flask, render_template, request, jsonify, redirect, url_for
app = Flask(__name__)


def fetch_book_recommendations(book_title):
    GOOGLE_BOOKS_API_URL = "https://www.googleapis.com/books/v1/volumes"

    # Query Google Books API using the book title
    query_params = {
        "q": f"intitle:{book_title}",
        "maxResults": 5,
        "printType": "books"
    }
    response = requests.get(GOOGLE_BOOKS_API_URL, params=query_params)

    # Check if the request was successful
    if response.status_code != 200:
        return []

    # Parse the API response to extract the book recommendations and their details
    books_data = response.json()
    books = []
    for item in books_data.get("items", []):
        book_info = item["volumeInfo"]
        book = {
            "title": book_info.get("title", ""),
            "authors": book_info.get("authors", []),
            "description": book_info.get("description", ""),
            "thumbnail": book_info.get("imageLinks", {}).get("thumbnail", ""),
        }
        books.append(book)

    return books


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/recommendations", methods=["POST"])
def recommendations():
    book_title = request.form.get("book_title", "").strip()
    if not book_title:
        return jsonify({"error": "Book title is required"}), 400

    books = fetch_book_recommendations(book_title)
    return render_template("recommendations.html", book_title=book_title, books=books)


if __name__ == "__main__":
    app.run(debug=True)

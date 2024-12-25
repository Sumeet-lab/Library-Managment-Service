from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data for books and members
books = [
    {"id": 1, "title": "The Great Gatsby", "author": "ABC", "available": True},
    {"id": 2, "title": "Event in 1984", "author": "DEF", "available": True},
]

members = [
    {"id": 1, "name": "Alice Johnson", "membership_type": "Gold"},
    {"id": 2, "name": "Bob Smith", "membership_type": "Silver"},
]


# Get all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

# Get a single book by ID
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = None
    for i in books:
        if i["id"]==book_id:
            book = i
    return jsonify(book) if book else ({"MESSAGE": "Book not found"}, 200)

# Add a new book
@app.route('/books', methods=['POST'])
def add_book():
    new_book = request.get_json()
    new_book["id"] = len(books) + 1
    books.append(new_book)
    return jsonify(new_book)

# Update an existing book
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = None
    for i in books:
        if i["id"]==book_id:
            book = i
    if not book:
        return {"MESSAGE": "Book not found"}

    data = request.get_json()
    book.update(data)
    return jsonify(book)

# Delete a book
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    temp = []
    for i in books:
        if i["id"]!=book_id:
            temp.append(i)
    books = temp
    return {"message": "Book deleted"}


# Get all members
@app.route('/members', methods=['GET'])
def get_members():
    return jsonify(members)

# Get a single member by ID
@app.route('/members/<int:member_id>', methods=['GET'])
def get_member(member_id):
    member = None
    for i in members:
        if i["id"]==member_id:
            member = i
    return jsonify(member) if member else ({"MESSAGE": "Member not found"})

# Add a new member
@app.route('/members', methods=['POST'])
def add_member():
    new_member = request.get_json()
    new_member["id"] = len(members) + 1
    members.append(new_member)
    return jsonify(new_member)

# Update an existing member
@app.route('/members/<int:member_id>', methods=['PUT'])
def update_member(member_id):
    member = None
    for i in members:
        if i["id"]==member_id:
            member = i

    if not member:
        return {"MESSAGE": "Member not found"}
    data = request.get_json()
    member.update(data)
    return jsonify(member)

# Delete a member
@app.route('/members/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    global members
    members = [m for m in members if m["id"] != member_id]
    return {"MESSAGE": "Member deleted"}


if __name__ == '__main__':
    app.run(debug=True)

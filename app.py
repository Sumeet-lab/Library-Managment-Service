from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)


# Implementation of SQLite database

# Get all books
@app.route('/books', methods=['GET'])
def get_books():
    cursor.execute('select * from books;')
    recs= []
    for i in cursor.fetchall():
        recs.append(dict(zip(["id","title","author"],i)))
    return jsonify(recs)

# Get a single book by ID
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    cursor.execute('select * from books where id={}'.format(book_id))
    book = cursor.fetchall()
    if len(book)!=0:
        return jsonify(dict(zip(["id","title","author"],book[0])))
    return {"MESSAGE": "Book not found"}

# Add a new book
@app.route('/books', methods=['POST'])
def add_book():
    new_book = request.get_json()
    cursor.execute('insert into books (title, author) values (?,?)',(new_book["title"], new_book["author"]))
    connection.commit()
    return {"MESSAGE": "Book added successfully"}

# Update an existing book
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    cursor.execute('select * from books where id={}'.format(book_id))
    book = cursor.fetchall()
    if len(book) == 0:
        return {"MESSAGE": "Book not found"}
    new_book = request.get_json()
    cursor.execute(f"update Books set title='{new_book['title']}', author='{new_book['author']}' where id={book_id};")
    connection.commit()
    return {"MESSAGE": "Book updated successfully"}

# Delete a book
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    cursor.execute('select * from books where id={}'.format(book_id))
    book = cursor.fetchall()
    if len(book) == 0:
        return {"MESSAGE": "Book not found"}

    cursor.execute("delete from Books where id={}".format(book_id))
    connection.commit()
    return {"message": "Book deleted"}


# Get all members
@app.route('/members', methods=['GET'])
def get_members():
    cursor.execute('select * from members;')
    recs = []
    for i in cursor.fetchall():
        recs.append(dict(zip(["id", "name", "membership_type"], i)))
    return jsonify(recs)

# Get a single member by ID
@app.route('/members/<int:member_id>', methods=['GET'])
def get_member(member_id):
    cursor.execute('select * from members where id={}'.format(member_id))
    member = cursor.fetchall()
    if len(member) != 0:
        return jsonify(dict(zip(["id", "title", "author"], member[0])))
    return {"MESSAGE": "Member not found"}

# Add a new member
@app.route('/members', methods=['POST'])
def add_member():
    new_member = request.get_json()
    cursor.execute('insert into members (name, membership_type) values (?,?)', (new_member["name"], new_member["membership_type"]))
    connection.commit()
    return {"MESSAGE": "Member added successfully"}

# Update an existing member
@app.route('/members/<int:member_id>', methods=['PUT'])
def update_member(member_id):
    cursor.execute('select * from members where id={}'.format(member_id))
    member = cursor.fetchall()
    if len(member) == 0:
        return {"MESSAGE": "Member not found"}
    new_member = request.get_json()
    cursor.execute(f"update members set name='{new_member['name']}', membership_type='{new_member['membership_type']}' where id={member_id};")
    connection.commit()
    return {"MESSAGE": "Member updated successfully"}

# Delete a member
@app.route('/members/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    cursor.execute('select * from members where id={}'.format(member_id))
    member = cursor.fetchall()
    if len(member) == 0:
        return {"MESSAGE": "Member not found"}

    cursor.execute("delete from members where id={}".format(member_id))
    connection.commit()
    return {"message": "Member deleted successfully"}


if __name__ == '__main__':
    connection = sqlite3.connect("LMS.db", check_same_thread=False)
    cursor = connection.cursor()

    cursor.execute("create table if not exists Books (id INTEGER PRIMARY KEY, title VARCHAR(255), author VARCHAR(255));")
    cursor.execute("create table if not exists Members (id INTEGER PRIMARY KEY, name VARCHAR(255), membership_type VARCHAR(255))")
    connection.commit()

    app.run(host="0.0.0.0", port=8080)

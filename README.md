
# Library Managment System (Flask API)

Flask API for Library Managment wiht CRUD operations. Deployed at Railway Hosting Service



#### Install all requirements using pip

```http
  pip install -r requirements.txt

```
#### Run app

```http
  python app.py
```

## API Usage

#### Get all Books

```http
  GET apiurl/books

  For instance: http://127.0.0.1:8080/books
```

#### Get a book by id

```http
  GET apiurl/books/<id>

  For instance: http://127.0.0.1:8080/books/2  
```

#### Add a new book

```http
  POST apiurl/books

  For instance: http://127.0.0.1:8080/books
  (Requires title and author in body of POST request) 
  {"title":"ABC","author":"XYZ"}
  
```

#### Update a book entry at <id>

```http
  PUT apiurl/books/<id>

  For instance: http://127.0.0.1:8080/books/2

  (Requires title and author in body of PUT request) 
  {"title":"newtitle","author":"newauthor"}  
```

#### Delete a book at <id>

```http
  DELETE apiurl/books/<id>

  For instance: http://127.0.0.1:8080/books/2 
```


### ** Same follows for Endpoints for Members (books -> members)** 

```http
  Member JSON

  {"name":"ABC", "membership_type":"A"}
```



## Links

 - [Deployed here (Live) ](https://library-managment-service-production.up.railway.app/books)





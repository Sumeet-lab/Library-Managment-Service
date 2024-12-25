
# Library Managment System (Flask API)

Flask API for Library Managment wiht CRUD operations. Deployed at Railway Hosting Service


## API Reference

#### Install all requirements using pip

```http
  pip install -r requirements.txt

```
#### Run app

```http
  python app.py
```

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
```

#### Update a book entry

```http
  PUT apiurl/books/<id>

  For instance: http://127.0.0.1:8080/books/2  
```

#### Delete a book

```http
  DELETE apiurl/books/<id>

  For instance: http://127.0.0.1:8080/books/2  
```


```http
Same follows for Endpoints for Members 
```


## Acknowledgements

 - [Deployed here ](https://library-managment-service-production.up.railway.app/books)



# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a fully functional REST API using the FastAPI framework in Python, learning how to define routes, handle request/response data with Pydantic models, and interact with the API using standard HTTP methods.

## 📝 Tasks

### 🛠️ Set Up a FastAPI Application

#### Description
Create a new FastAPI application and define a root endpoint that returns a welcome message. Run the development server and verify the API is accessible.

#### Requirements
Completed program should:

- Import and instantiate a `FastAPI` app
- Define a `GET /` route that returns a JSON welcome message
- Run the app using `uvicorn` and confirm it responds at `http://127.0.0.1:8000`


### 🛠️ Build a CRUD Endpoint for a Resource

#### Description
Design and implement a full set of CRUD (Create, Read, Update, Delete) endpoints for a simple resource — a list of **books**. Use Pydantic models to validate request and response data.

#### Requirements
Completed program should:

- Define a `Book` Pydantic model with fields: `id` (int), `title` (str), `author` (str), and `year` (int)
- Implement `GET /books` to return all books
- Implement `GET /books/{book_id}` to return a single book by ID, returning a 404 error if not found
- Implement `POST /books` to add a new book
- Implement `PUT /books/{book_id}` to update an existing book
- Implement `DELETE /books/{book_id}` to remove a book by ID


### 🛠️ Explore the Automatic API Documentation

#### Description
FastAPI automatically generates interactive API documentation. Use it to test each of your endpoints without writing any extra code.

#### Requirements
Completed program should:

- Access the Swagger UI at `http://127.0.0.1:8000/docs`
- Successfully test each CRUD endpoint (GET, POST, PUT, DELETE) using the interactive docs
- Verify that invalid requests (e.g., a missing book ID) return appropriate error responses

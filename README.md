# Pydantic Assignment – FastAPI User API

## Overview 
This task demonstrates the use of Pydantic to build a simple User API.
It covers:

1. Data validation using Pydantic models
2. Custom field validators
3. Environment configuration using BaseSettings
4. API integration with FastAPI

---

## Project Structure
pydantic-assignment/
│
├── app/
│   ├── __init__.py
│   ├── main.py         # FastAPI app (routes)
│   ├── models.py       # Pydantic models + validators
│   ├── config.py       # BaseSettings (env config)
│   ├── database.py     # In-memory database
│
├── .env                # Environment variables
├── requirements.txt
└── README.md

---

## Setup Instructions

### Create Virtual Environment
Virtual Environment is a Isolated Python Environment.
→ Virtual Environment installs packages separately - prevent conficts between different
     that may require different versions of same library.
→ Virtual Environment does not effect system/global Python - each Virtual Environment is
     a self contained directory with its own Python interpreter and package directory, different
     from others.
→ Each project has its own dependencies which prevents conflicts where one project’s
     required version is different from version of different projects.
→ When a Virtual Environment is active, system’s path variable is temporarily modified to
     use virtual environment’s executable and packages, not the global paths.
→ When, activation of Virtual Environment:
     env\Scripts\activate
     Path variable temporarily modified (not permanently).
→ Before Activation:
     C:\Users\Ashish\AppData\Local\Python\pythoncore-3.14-64\python.exe
→ After Activation: \env\Scripts\python.exe


```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### Install Dependencies
1. pip → The default package manager for Python used to install and manage libraries and dependencies.
2. fastapi → A modern, high-performance web framework for building APIs with Python using type hints.
3. uvicorn → A fast ASGI server used to run FastAPI applications.
4. pydantic → A data validation and settings management library using Python type annotations.
5. python-dotenv → Loads environment variables from a .env file into your application.
6. pydantic-settings → Extends Pydantic to manage application configuration via environment variables.
7. email-validator → A library for validating email addresses according to standards.

```bash
pip install fastapi uvicorn pydantic python-dotenv pydantic-settings email-validator
```

---

### Save Dependencies
```bash
pip freeze > requirements.txt
```

---

### Setup `.env` File
Create a `.env` file in root:

```env
APP_NAME=Pydantic Assignment
DEBUG=True
ADMIN_EMAIL=ashu11vats@gmail.com
```

---

## Run the Application
```bash
uvicorn app.main:app --reload
```

Open in browser:
1. API Root → http://127.0.0.1:8000/

---

## Features Implemented

### Pydantic Models

Defined a `User` model with:
1. id (int)
2. name (str)
3. age (int, default = 18)
4. email (EmailStr)
5. is_active (bool, default = True)

---

### Custom Validators
1. Age must be between 0 and 120
2. Name cannot be empty

---

### BaseSettings (Environment Config)
Using `pydantic-settings` to load:
1. APP_NAME
2. DEBUG
3. ADMIN_EMAIL

---

### FastAPI Integration
APIs implemented:
| Method | Endpoint      | Description      |
| ------ | ------------- | ---------------- |
| GET    | `/`           | Check API status |
| POST   | `/users`      | Create user      |
| GET    | `/users`      | Get all users    |
| GET    | `/users/{id}` | Get single user  |

---

### Request & Response Validation
1. Request body validated using Pydantic model
2. Response formatted using `response_model`

---

## Example Request

### POST `/users`
```json
{
  "id": 1,
  "name": "Ashish",
  "age": 25,
  "email": "ashish@gmail.com"
}
```

---

### Invalid Example
```json
{
  "id": 1,
  "name": "",
  "age": -5,
  "email": "invalid"
}
```

-> Returns validation errors automatically

---

## Key Concepts Learned

1. Pydantic BaseModel
2. Field validation
3. Custom validators
4. Environment configuration
5. FastAPI integration
6. JSON serialization

---

## Future Improvements
1. Add PUT/PATCH/DELETE APIs
2. Use real database (PostgreSQL)
3. Add authentication
4. Add logging


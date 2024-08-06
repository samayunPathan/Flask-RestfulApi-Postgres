
# Flask User Management API

## Project Description

This project is a RESTful API built with Flask for user management. It provides functionality for user registration, authentication, password management, and user administration. The API follows OpenAPI standards, uses JWT for authentication, and is documented using Swagger.

## Table of Contents

1. [Project Description](#project-description)
2. [Features](#features)
3. [Project Structure](#project-structure)
4. [Technology Stack](#technology-stack)
5. [Setup and Installation](#setup-and-installation)
6. [Database Migration](#database-migration)
7. [API Documentation](#api-documentation)
   - [Key Endpoints](#key-endpoints)
     - [Authentication Endpoints](#authentication-endpoints)
     - [User Management Endpoints](#user-management-endpoints)
8. [User Model](#user-model)
9. [Authentication](#authentication)
10. [Role-Based Access Control](#role-based-access-control)
11. [Screenshots](#screenshots)



## Features

- User registration and authentication
- Password reset functionality
- Role-based access control (Admin/User)
- User management (CRUD operations)
- JWT-based authentication
- OpenAPI standard compliance with Swagger documentation
- Automatic database schema generation using SQLAlchemy


## Project Structure
````
flask_user_management/
├── app/                                                           
│   ├── __init__.py
│   ├── models/
│   │   └── user.py
│   ├── schemas/
│   │   └── user_schema.py
│   ├── routes/
│   │   ├── auth_routes.py
│   │   └── user_routes.py
│   ├── services/
│   │   ├── auth_service.py
│   │   └── user_service.py
│   └── utils/
│       ├── helpers.py
│       └── decorators.py
├── config.py
├── .env
├── .gitignore
├── requirements.txt
└── run.py

````


## Technology Stack

- Flask
- PostgreSQL
- SQLAlchemy
- JWT for authentication
- Swagger for API documentation

## Setup and Installation

1. Clone the repository:
`git clone repo_url`

cd flask_user_management

2. Set up a virtual environment:

`python -m venv venv`

`source venv/bin/activate # On Windows use venv\Scripts\activate`

3. Install dependencies:

`pip install -r requirements.txt`

4. Set up environment variables:

Create a .env file and add the following variables according to `config.py` file for example

`DATABASE_URL=postgresql://username:password@localhost/dbname
SECRET_KEY=your_secret_key_here
SECRETE_ADMIN_KEY=your admin_secret_key`

5. Run the application:
`python run.py`

## Database Migration
To manage database migrations, use the following commands:

Create a new migration:

`flask db migrate -m "message"`

Apply the migration:

`flask db upgrade`

## API Documentation

The API is documented using Swagger. Once the application is running, you can access the Swagger UI at:

`http://localhost:5000/apidocs/`


### Key Endpoints

#### Authentication Endpoints

- **POST** `/auth/register`: Register a new user

  ````
  {
  "email": "your email",
  "first_name": "your first name",
  "last_name": "your last name",
  "password": "your password",
  "secret_admin_key": "your secrete admin key",
  "username": "your username"
  }
  ````
     Response:
    ````
   {
  msg: user create successfully
   }
    ````

- **POST** `/auth/login`: User login (returns JWT token)
  ````
   {
  "email": "your email",
  "password": "your password"
  }
  ````
   Response:
    ````
   {
  msg: your jwt_access_token
   }
    ````

- **POST** `/auth/forgot-password`: Request password reset and  get a reset_token via email
  ````
  {
  "email": "your email"
  }
   ````
   Response:
    ````
   {
  msg: password reset_token
   }
    ````
- **POST** `/auth/reset-password`: Reset password with token
  ````
  {
  "email": "your email",
  "password reset_token":"password reset_token",
  "new password":"your new password"
  }
   ````
   Response:
    ````
   {
  msg: password reset successfully
   }
    ````

#### User Management Endpoints

- **GET** `/users`: Get all users (Admin only)

  Response:
  ````
    {
    "active": "your status",
    "created_at": "created time",
    "email": "your email",
    "first_name": "your first_name",
    "id": your id,
    "last_name": "yourlast_name",
    "reset_token": null,
    "reset_token_expires_at": null,
    "role": "your role",
    "updated_at": "updated time",
    "username": "your user_name"
  }
  ````
- **GET** `/users/<user_id>`: Get user by ID
- **PUT** `/users/<user_id>`: Update user 
        Activate/Deactivate,Promote user to Admin (Admin only)
    ````
  {
  "role":"USER/ADMIN"  *Admin only
  "active":"active/deactive" *Admin only
  "email": "your email",
  "first_name": "your first name",
  "last_name": "your last name",
  "secret_admin_key": "your secrete admin key",
  "username": "your username"
  }
  ````

   Response:
    ````
   {
  msg: user updated successfully
   }
    ````
- **DELETE** `/users/<user_id>`: Delete user (Admin only)

   Response:
    ````
   {
  msg: user deleted successfully
   }
    ````


## User Model

The User model includes the following fields:
- username (varchar, unique)
- first_name (varchar)
- last_name (varchar)
- password (varchar, encrypted)
- email (varchar, unique)
- role (enum: 'ADMIN', 'USER')
- created_at (datetime, auto-inserted)
- updated_at (datetime, auto-updated)
- is_active (boolean)

## Authentication

All protected endpoints require a valid JWT token in the Authorization header:

`Authorization: <your_jwt_token>`

## Role-Based Access Control

- Admin users can perform all operations
- Regular users can only view and update their own information
- Only admins can delete users, change user roles, or activate/deactivate accounts

## Screenshots


![Screenshot (2)](https://github.com/user-attachments/assets/52542fcb-ccf9-4f18-9a71-f6069ee6723c)


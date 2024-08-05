
# Flask User Management API

## Project Description

This project is a RESTful API built with Flask for user management. It provides functionality for user registration, authentication, password management, and user administration. The API follows OpenAPI standards, uses JWT for authentication, and is documented using Swagger.

## Table of Contents

1. [Project Description](#project-description)
2. [Features](#features)
3. [Project Structure](#project-structure)
4. [Technology Stack](#technology-stack)
5. [Setup and Installation](#setup-and-installation)
6. [API Documentation](#api-documentation)
   - [Key Endpoints](#key-endpoints)
     - [Authentication Endpoints](#authentication-endpoints)
     - [User Management Endpoints](#user-management-endpoints)
7. [User Model](#user-model)
8. [Authentication](#authentication)
9. [Role-Based Access Control](#role-based-access-control)
10. [Screenshots](#screenshots)



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
SECRET_KEY=your_secret_key_here`

5. Run the application:
`python run.py`

## API Documentation

The API is documented using Swagger. Once the application is running, you can access the Swagger UI at:

`http://localhost:5000/apidocs/`


### Key Endpoints

#### Authentication Endpoints

- **POST** `/auth/register`: Register a new user
- **POST** `/auth/login`: User login (returns JWT token)
- **POST** `/auth/forgot-password`: Request password reset and  get a reset_token via email
- **POST** `/auth/reset-password`: Reset password with token

#### User Management Endpoints

- **GET** `/users`: Get all users (Admin only)
- **GET** `/users/<user_id>`: Get user by ID
- **PUT** `/users/<user_id>`: Update user 
        Activate/Deactivate,Promote user to Admin (Admin only)
- **DELETE** `/users/<user_id>`: Delete user (Admin only)


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

![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)


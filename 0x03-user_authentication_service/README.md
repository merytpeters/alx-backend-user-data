# 0x03. User Authentication Service

## Project Overview

The **User Authentication Service** is a backend project designed to handle user authentication, providing features such as registration, login, password hashing, and user session management. This service is implemented using **Node.js** with a focus on security, scalability, and best practices for modern authentication systems.

This project is part of the **0x03** curriculum, aimed at demonstrating how to build a secure and efficient authentication system.

## Features

- **User Registration**: Allows users to create an account by providing a username and password.
- **Login**: Authenticates users based on their credentials and generates a session.
- **Password Hashing**: Secure storage of user passwords using a cryptographic hashing algorithm.
- **Session Management**: User sessions are tracked with JWT (JSON Web Tokens) for stateless authentication.
- **Error Handling**: Includes robust error handling for invalid inputs and failed authentication attempts.
- **Secure Routes**: Protects routes requiring authentication with JWT-based verification.

## Technologies Used

- **Node.js**: JavaScript runtime used to build the backend.
- **Express.js**: Web framework for building the API.
- **bcrypt**: Library used to hash and compare passwords securely.
- **JWT (JSON Web Token)**: Used for stateless authentication (session management).
- **dotenv**: Used for managing environment variables securely.
- **MongoDB**: Database used to store user information (you can replace this with another database if preferred).
- **Mongoose**: ODM (Object Document Mapper) for interacting with MongoDB.

## Setup and Installation

### Prerequisites

- Node.js (v14 or higher)
- MongoDB (either locally or using a cloud-based service like MongoDB Atlas)

### Clone the Repository

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/user-authentication-service.git
   cd user-authentication-service

2. Install dependencies:
   npm install

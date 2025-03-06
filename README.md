"# auth_jwt" 
# Django REST API with JWT Authentication  

## Overview  
This project is a beginner-friendly Django REST API that implements JWT authentication and utilizes Django REST Framework (DRF) serializers to manage user data.  

## Features  
- User registration  
- User login with JWT authentication  
- Protected API endpoints requiring authentication  
- CRUD operations using Django REST Framework  

## Installation  

1. **Clone the Repository**  
   ```bash
   git clone <repository_url>
   cd <project_directory>
   ```

2. **Create a Virtual Environment**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install Dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Migrations**  
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a Superuser**  
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the Server**  
   ```bash
   python manage.py runserver
   ```

## API Endpoints  

| Method | Endpoint         | Description                | Authentication |
|--------|-----------------|----------------------------|---------------|
| POST   | `/api/register/` | Register a new user        | No            |
| POST   | `/api/login/`    | Obtain JWT token           | No            |
| GET    | `/api/user/`     | Get user details           | Yes (JWT)     |
| PUT    | `/api/user/`     | Update user details        | Yes (JWT)     |
| DELETE | `/api/user/`     | Delete user                | Yes (JWT)     |

## Usage  

### Register a User  
```bash
curl -X POST http://127.0.0.1:8000/api/register/ -H "Content-Type: application/json" -d '{"username": "testuser", "password": "testpass"}'
```

### Login and Get Token

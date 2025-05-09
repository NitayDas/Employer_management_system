# Employer_management_system

# Employer Management System API (Django REST Framework)

## Features
- RESTful API with CRUD operations
- JWT Authentication
- Custom User Model with email login
- Employer management with company details




## 🔧 Installation
1. Clone the repo:
```python
git clone https://github.com/NitayDas/Employer_management_system.git
```

2. Create virtual env and activate (Optiontal):

```python
python -m venv venv
```
```python
venv/Scripts/activate
```


3. Install dependencies:
   
```python
pip install -r requirements.txt
```


4. Run migrations:
   
```python
python manage.py makemigrations
python manage.py migrate
```


5. Start server:
   
```python
python manage.py runserver
```

## API Documentation

Base URL

```python
http://127.0.0.1:8000/
```
## API Endpoints

```python
POST /api/auth/signup/
POST /api/auth/login/
GET /api/auth/profile/
POST /api/employers/
GET /api/employers/
GET /api/employers/<id>/
PUT /api/employers/<id>/
DELETE /api/employers/<id>/
```


## Example Requests

```curl

curl -X POST http://127.0.0.1:8000/api/auth/signup/ 
-H "Content-Type: application/json" 
-d '{"email":"user@example.com","first_name":"John","last_name":"Doe","password":"password123"}'

curl -X POST http://127.0.0.1:8000/api/auth/login/
-H "Content-Type: application/json" 
-d '{"email":"user@example.com","password":"password123"}'

curl -X GET http://127.0.0.1:8000/api/employers/ 
-H "Authorization: Bearer your_access_token"

curl -X POST http://127.0.0.1:8000/api/employers/
-H "Authorization: Bearer your_access_token"
-H "Content-Type: application/json"
-d '{"company_name":"Test Company","contact_person_name":"Jane Smith","email":"contact@test.com","phone_number":"1234567890","address":"123 Test St"}'

```






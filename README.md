1.Clone the repository:
  git clone https://github.com/Anoop0325/Task-Manager.git
  cd Task-Manager

2. Create and activate virtual environment:
  python -m venv venv
  source venv/bin/activate  # Linux/Mac
  venv\Scripts\activate #windows

3. Install dependencies:
  pip install -r requirements.txt

5. Run migrations:
  python manage.py makemigrations task
  python manage.py migrate

6. Run development server:
   python manage.py runserver


API Documnetaion

1. Authentication:
   Get your token:
     curl -X POST http://localhost:8000/api-token-auth/ \
    -H "Content-Type: application/json" \
    -d '{"username":"yourusername", "password":"yourpassword"}'

   for username and password you have to open your shell_plus and create user manually

   Include token in headers:
     Authorization: Token your_token_here

2. Endpoints:
   i. Task Creation:
     URL: /api/tasks/create/
     Method: POST
     Headers:
     Content-Type: application/json
     Authorization: Token your_token_here

     Request Body:
       {
        "name": "Complete project",
        "description": "Finish the backend API",
        "task_type": "W"
       }
  
     Response:
      {
        "id": 1,
        "name": "Complete project",
        "description": "Finish the backend API",
        "created_at": "2023-06-15T10:30:00Z",
        "task_type": "W",
        "status": "P",
        "assigned_users": []
       }

   ii. Task Assignment:
      URL: /api/tasks/{task_id}/assign/
      Method: PUT
      Headers:
        Content-Type: application/json
        Authorization: Token your_token_here

     Request Body:
       {
         "user_ids": [1, 2, 3]
       }

    iii. User Tasks:
        URL: /user/tasks/?id={user_id}
        Method: GET
        Headers:
          Authorization: Token your_token_here
           

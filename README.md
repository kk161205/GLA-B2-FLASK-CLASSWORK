# User Registration & Login System

A Flask-based user authentication system with PostgreSQL database.

## Features
- User registration with validation
- User login with session management
- Password hashing with bcrypt
- User dashboard with profile management
- Email update functionality
- User listing feature
- Account deletion
- Session-based authentication
- PostgreSQL database integration
- Form validation with Flask-WTF

## Setup

1. **Clone the repository**
   ```bash
   cd B2
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment**
   ```bash
   copy .env.example .env
   ```
   Edit `.env` with your database credentials

5. **Setup PostgreSQL**
   - Create a database named `test`
   - Update DATABASE_URL in `.env`

6. **Run the application**
   ```bash
   python app/app.py
   ```

7. **Access the application**
   - Home: http://localhost:5000/
   - Register: http://localhost:5000/register
   - Login: http://localhost:5000/login
   - Dashboard: http://localhost:5000/dashboard (after login)

## Project Structure
```
B2/
├── app/
│   ├── model/
│   │   └── users.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── dashboard.html
│   │   ├── login.html
│   │   └── register.html
│   ├── app.py
│   └── form.py
├── .env
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Available Routes
- `/` - Home page (redirects to dashboard if logged in, otherwise to register)
- `/register` - User registration
- `/login` - User login
- `/dashboard` - User dashboard (requires login)
- `/update-email` - Update user email (POST)
- `/fetch-users` - View all users
- `/delete-account` - Delete user account (POST)
- `/logout` - User logout

## Deployment

For production deployment:
1. Set `FLASK_ENV=production` in `.env`
2. Use a production WSGI server (gunicorn)
3. Configure proper database credentials
4. Set a strong SECRET_KEY

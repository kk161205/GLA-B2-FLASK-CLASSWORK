# User Registration & Login System

A Flask-based user authentication system with Neon PostgreSQL database, deployed on Vercel.

🌐 **Live Demo**: [https://gla-b2-flask-classwork.vercel.app](https://gla-b2-flask-classwork.vercel.app)

## Features
- User registration with validation
- User login with session management
- Password hashing with bcrypt
- User dashboard with profile management
- Email update functionality
- User listing feature
- Account deletion
- Session-based authentication
- Neon PostgreSQL database integration
- Form validation with Flask-WTF
- Email validation
- Serverless deployment on Vercel

## Local Development Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/kk161205/GLA-B2-FLASK-CLASSWORK.git
   cd GLA-B2-FLASK-CLASSWORK
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   source venv/bin/activate  # macOS/Linux
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment**
   ```bash
   copy .env.example .env  # Windows
   cp .env.example .env    # macOS/Linux
   ```
   Edit `.env` with your Neon database credentials:
   ```
   SECRET_KEY=your-secret-key-here
   DATABASE_URL=postgresql://username:password@ep-xxx-xxx.us-east-1.aws.neon.tech/neondb?sslmode=require
   FLASK_ENV=development
   ```

5. **Run the application**
   ```bash
   python app/app.py
   ```

6. **Access the application**
   - Home: http://localhost:5000/
   - Register: http://localhost:5000/register
   - Login: http://localhost:5000/login
   - Dashboard: http://localhost:5000/dashboard (after login)

## Project Structure
```
B2/
├── api/
│   └── index.py          # Vercel entry point
├── app/
│   ├── model/
│   │   └── users.py       # User model and database
│   ├── static/
│   │   └── favicon.ico    # Static files
│   ├── templates/
│   │   ├── base.html      # Base template
│   │   ├── dashboard.html # User dashboard
│   │   ├── login.html     # Login page
│   │   └── register.html  # Registration page
│   ├── app.py            # Main Flask application
│   └── form.py           # WTForms definitions
├── .env                  # Environment variables (not in repo)
├── .env.example          # Environment template
├── .gitignore           # Git ignore rules
├── requirements.txt     # Python dependencies
├── vercel.json         # Vercel deployment config
└── README.md           # This file
```

## Technologies Used

- **Backend**: Flask (Python web framework)
- **Database**: Neon PostgreSQL (serverless PostgreSQL)
- **Authentication**: bcrypt for password hashing
- **Forms**: Flask-WTF with WTForms validation
- **Email Validation**: email-validator
- **Deployment**: Vercel (serverless platform)
- **Environment**: python-dotenv for configuration

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

### Vercel Deployment (Current)
The application is deployed on Vercel with:
- **Framework Preset**: Other
- **Build Command**: (empty)
- **Output Directory**: (empty)
- **Install Command**: `pip install -r requirements.txt`
- **Environment Variables**:
  - `SECRET_KEY`: Strong secret key for sessions
  - `DATABASE_URL`: Neon PostgreSQL connection string
  - `FLASK_ENV`: `production`

### Local Development
For local development:
1. Set up Neon database and get connection string
2. Configure `.env` file with your credentials
3. Run `python app/app.py`

### Manual Deployment
For other platforms:
1. Set environment variables
2. Use a production WSGI server (gunicorn)
3. Configure proper database credentials
4. Set a strong SECRET_KEY

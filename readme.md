# 🧠 Task Tracker Backend

This is the FastAPI-based backend for the Task Tracker full-stack application. It provides secure JWT authentication, user management, and CRUD functionality for tasks, connected to a PostgreSQL database.

---

## 🚀 Features

- JWT-based user authentication
- Secure protected endpoints
- Task CRUD (Create, Read, Update, Delete)
- SQLAlchemy ORM and Alembic migrations
- Environment variable-based configuration

---

## 🛠️ Tech Stack

- FastAPI
- SQLAlchemy
- Alembic
- PostgreSQL
- Python-JOSE (JWT)
- Passlib (bcrypt hashing)

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/task-tracker-backend.git
cd task-tracker-backend

2. Install dependencies

pip install -r requirements.txt

3. Configure .env

DATABASE_URL=postgresql://postgres:password@localhost:5432/task_db

4. Initialize the database

python -c "from app.db.init_db import init_db; init_db()"

5. Run the app

uvicorn app.main:app --reload

Access the docs: http://localhost:8000/docs

## 🔗 Related Project

- [Backend (FastAPI)](https://github.com/yourusername/task-tracker-backend)

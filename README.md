## Application Form System

A simple full-stack web application built using FastAPI, HTML, CSS, JavaScript, and SQLAlchemy.
This project allows users to submit an application form and stores the data in a database. An admin endpoint is provided to view all submitted applications.
** This is project is made for the understanding working of databases. **

## 🚀 Features

User-friendly application form

Backend built with FastAPI

Database integration using SQLAlchemy

Data persistence using SQLite (can be upgraded to PostgreSQL)

Admin endpoint to view submitted applications

Clean project structure

Ready for deployment

## 🛠️ Tech Stack

Backend

FastAPI

SQLAlchemy

Uvicorn

Frontend

HTML

CSS

JavaScript (Fetch API)

Database

SQLite (default)

PostgreSQL (recommended for production)

## 📁 Project Structure
application-form/
│
└── app/
    ├── main.py
    ├── models.py
    ├── database.py
    ├── schema.py
    │
    ├── static/
    │   ├── style.css
    │   └── script.js
    │
    └── templates/
        └── form.html
## ⚙️ Installation & Setup
1. Clone the Repository
git clone https://github.com/your-username/application-form.git
cd application-form
2. Create Virtual Environment
python -m venv venv

Activate it:

Windows

venv\Scripts\activate

Mac/Linux

source venv/bin/activate
3. Install Dependencies
pip install -r requirements.txt

If requirements.txt does not exist:

pip install fastapi uvicorn sqlalchemy jinja2 python-multipart
▶️ Running the Application

From the project root directory:

uvicorn app.main:app --reload

Open in browser:

http://localhost:8000
## 📊 Viewing Submitted Applications

After users submit the form, you can view all stored data at:

http://localhost:8000/admin

This endpoint returns all application records in JSON format.

## 🗄 Database

By default, the project uses SQLite.

Database file:

app.db

You can inspect it using tools like DB Browser for SQLite.

For production use, it is recommended to switch to PostgreSQL.

## 🔒 Future Improvements

Add authentication for admin panel

Convert SQLite to PostgreSQL

Deploy on cloud platform (e.g., Render or AWS)

Add form validation

Export submissions as CSV

Add dashboard UI for admin

# 🍽️ Meal Genie - Setup Guide

Welcome! 🎉

This guide will help you set up and run **Meal Genie** on your computer.

No prior project configuration is required.

---

# 📋 Prerequisites

Before running the project, make sure the following software is installed.

## Required Software

- Python 3.10 or above
- MySQL Community Server
- Git (optional)

You can verify your Python installation:

```bash
python --version
```

or

```bash
python3 --version
```

---

# 📂 Step 1 — Extract the ZIP

Extract the ZIP anywhere you like.

Example:

```
Desktop/
    Meal-Genie-main/
```

Open this folder inside:

- VS Code
- PyCharm
- Cursor
- Any Python IDE

---

# 🐍 Step 2 — Create a Virtual Environment

This keeps project packages isolated.

## Windows

```bash
python -m venv venv
```

Activate

```bash
venv\Scripts\activate
```

---

## macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## Linux

```bash
python3 -m venv venv

source venv/bin/activate
```

If successful you should see

```
(venv)
```

before your terminal prompt.

---

# 📦 Step 3 — Install Dependencies

Run

```bash
pip install -r requirements.txt
```

Wait until all packages finish installing.

---

# 🔑 Step 4 — Get a Gemini API Key

Meal Genie uses **Google Gemini AI**.

Create a free API key.

Visit:

https://aistudio.google.com/app/apikey

Create a new API Key.

Copy it.

---

# 📄 Step 5 — Create a .env File

Inside the project folder, create a file named

```
.env
```

Copy the following into it:

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY

DB_HOST=127.0.0.1
DB_USER=root
DB_PASSWORD=YOUR_PASSWORD
DB_NAME=mygenie
```

Replace:

- YOUR_GEMINI_API_KEY
- YOUR_PASSWORD

with your own values.

---

# 🗄 Step 6 — Install MySQL

If MySQL is not installed,

Download:

https://dev.mysql.com/downloads/mysql/

During installation remember your password.

---

# 🗄 Step 7 — Create Database

Open MySQL Workbench

or

MySQL Command Line

Run

```sql
CREATE DATABASE mygenie;
```

Database created ✅

---

# ▶ Step 8 — Test Database

Run

```bash
python test_db.py
```

Expected output

```
Successfully connected!
```

If not, verify:

- MySQL is running
- Password is correct
- Database exists

---

# 🚀 Step 9 — Launch Meal Genie

Run

```bash
streamlit run app.py
```

Your browser should automatically open.

If not,

visit

```
http://localhost:8501
```

---

# 📂 Project Structure

```
Meal-Genie-main
│
├── .env
├── .env.example
├── .gitignore
├── app.py
├── config.toml
├── html_templates.py
├── main.py
├── requirements.txt
├── style.css
├── test_db.py
└── README.md
```

---

# 🔄 How Everything Works

```
User
 │
 ▼
Streamlit App
(app.py)
 │
 ├──────────────► Gemini AI
 │                   │
 │                   ▼
 │              Generated Recipe
 │
 ▼
MySQL Database
 │
 ▼
Recipe History
 │
 ▼
Displayed in Streamlit
```

---

# ❓ Common Problems

## ModuleNotFoundError

Install packages again.

```bash
pip install -r requirements.txt
```

---

## streamlit is not recognized

Activate the virtual environment first.

Windows

```bash
venv\Scripts\activate
```

Then

```bash
pip install streamlit
```

---

## Can't connect to MySQL

Check:

- MySQL service is running
- Password is correct
- Database is named

```
mygenie
```

---

## Invalid Gemini API Key

Generate a new API Key.

Update your

```
.env
```

file.

---

## Browser Doesn't Open

Open manually

```
http://localhost:8501
```

---

## Port Already in Use

Run

```bash
streamlit run app.py --server.port 8502
```

---

## dotenv Not Found

Install

```bash
pip install python-dotenv
```

---

# 🔒 Security Notes

Do **NOT** upload your `.env` file to GitHub.

Never share:

- Gemini API Key
- Database Password

Only share:

```
.env.example
```

---

# 🛑 Before Closing

Deactivate the environment

```bash
deactivate
```

---

# 💜 Enjoy!

You're now ready to use Meal Genie!

Happy Cooking 🍜🍕🥗

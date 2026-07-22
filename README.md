# 🍽️ Meal Genie

<p align="center">

<img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white">

<img src="https://img.shields.io/badge/Streamlit-Web%20App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white">

<img src="https://img.shields.io/badge/Google-Gemini%20AI-4285F4?style=for-the-badge&logo=google&logoColor=white">

<img src="https://img.shields.io/badge/MySQL-Database-4479A1?style=for-the-badge&logo=mysql&logoColor=white">

</p>

<p align="center">

<b>AI-Powered Recipe Generator built using Streamlit, Google Gemini AI and MySQL.</b>

Generate personalized recipes, save them to your cookbook, revisit previous recipes, and enjoy a modern responsive interface with light and dark themes.

</p>

---

# 📖 About the Project

Meal Genie is an AI-powered recipe generation application that helps users create recipes instantly using Google Gemini AI.

Instead of manually searching for recipes, users simply enter their available ingredients or cooking preferences and the application generates a complete recipe including:

- Recipe title
- Ingredients
- Step-by-step cooking instructions
- Preparation and cooking time
- Serving size
- Cooking tips

Generated recipes are stored in a MySQL database so they can be viewed later from the application's recipe history.

The application is built entirely using Streamlit with custom HTML and CSS for an interactive and modern user experience.

---

# ✨ Features

### 🤖 AI Recipe Generation

- Recipe generation using Google Gemini AI
- Personalized recipe suggestions
- Ingredient-based recipe generation

### 📚 Recipe Management

- Save recipes into MySQL
- View previously generated recipes
- Persistent recipe history

### 🎨 User Interface

- Streamlit-based web application
- Custom HTML templates
- Custom CSS styling
- Responsive interface
- Dark Mode
- Light Mode

### ⚡ Performance

- Fast recipe generation
- Lightweight architecture
- Easy local deployment

---

# 🛠 Tech Stack

## Frontend

- Streamlit
- HTML
- CSS

## Backend

- Python

## Artificial Intelligence

- Google Gemini AI
- Gemini 2.5 Flash

## Database

- MySQL

---

# 📦 Python Libraries

- streamlit
- google-genai
- PyMySQL
- mysql-connector-python
- python-dotenv

---

# 🗂 Project File Structure

```
Meal-Genie-main
│
├── .env.example          # Sample environment variables
├── .gitignore            # Git ignore rules
├── README.md             # Project documentation
├── app.py                # Main Streamlit application
├── config.toml           # Streamlit configuration
├── html_templates.py     # HTML templates used by the UI
├── main.py               # Console-based recipe generator
├── requirements.txt      # Project dependencies
├── style.css             # Custom styling
└── test_db.py            # Database connectivity test
```

---

# 🧠 Project Mind Map

```
Meal Genie
│
├── User Interface
│   ├── Streamlit
│   ├── HTML Templates
│   └── CSS Styling
│
├── AI Engine
│   └── Google Gemini 2.5 Flash
│
├── Database
│   └── MySQL
│
├── Configuration
│   ├── .env
│   ├── config.toml
│   └── .gitignore
│
├── Main Files
│   ├── app.py
│   ├── main.py
│   └── test_db.py
│
└── Documentation
    └── README.md
```

---

# 💻 System Requirements

- Python 3.10 or above
- MySQL Server
- Git (optional but recommended)

---

# 🚀 Installation

## 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Meal-Genie.git

cd Meal-Genie-main
```

---

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate it

```bash
venv\Scripts\activate
```

---

### macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

### Linux

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔐 Environment Variables

Create a file named

```
.env
```

Copy the following:

```
GEMINI_API_KEY=YOUR_GEMINI_API_KEY

DB_HOST=127.0.0.1
DB_USER=root
DB_PASSWORD=YOUR_PASSWORD
DB_NAME=mygenie
```

Replace the placeholders with your own credentials.

---

# 🗄 MySQL Setup

Create the database

```sql
CREATE DATABASE mygenie;
```

The application will use the credentials provided inside your `.env` file.

---

# ▶️ Running the Application

Start the Streamlit application

```bash
streamlit run app.py
```

The application will automatically open in your browser.

Default URL

```
http://localhost:8501
```

---

# 🧪 Testing Database Connection

A helper file is included to verify MySQL connectivity.

Run

```bash
python test_db.py
```

If everything is configured correctly, a successful database connection message will be displayed.

---

# 🌍 Cross Platform Compatibility

Meal Genie can be executed on

- ✅ Windows
- ✅ macOS
- ✅ Linux

The only requirements are:

- Python
- MySQL
- Internet connection (for Gemini AI)

---

# ❗ Common Issues & Solutions

## ModuleNotFoundError

**Problem**

```
ModuleNotFoundError
```

**Solution**

```
pip install -r requirements.txt
```

---

## Missing Environment Variables

**Problem**

```
API key missing
```

**Solution**

Verify that your `.env` file exists and contains all required variables.

---

## MySQL Connection Error

**Problem**

```
Can't connect to MySQL server
```

**Solution**

- Ensure MySQL is running.
- Verify host, username and password.
- Confirm the `mygenie` database exists.

---

## Google Gemini Authentication Error

**Problem**

```
Invalid API Key
```

**Solution**

Generate a new API key from Google AI Studio and update your `.env` file.

---

## Streamlit Command Not Found

**Problem**

```
streamlit is not recognized
```

**Solution**

Activate your virtual environment first, then run

```bash
pip install streamlit
```

---

# 📄 Files Overview

| File | Purpose |
|-------|---------|
| app.py | Main Streamlit application |
| main.py | Console version of recipe generation |
| html_templates.py | HTML templates used by the interface |
| style.css | Custom application styling |
| test_db.py | Database connection testing |
| config.toml | Streamlit configuration |
| requirements.txt | Python dependencies |
| .env.example | Sample environment configuration |

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push your branch
5. Open a Pull Request

---

# 👩‍💻 Author

**Jahnavi Modi**

Computer Science Engineering Student

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

It helps others discover the project and supports future improvements.

---

# 📜 License

This project is intended for educational and learning purposes.

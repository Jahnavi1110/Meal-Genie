# 🍽️ Meal Genie

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/Streamlit-Web_App-red?style=for-the-badge&logo=streamlit">
  <img src="https://img.shields.io/badge/Google-Gemini_AI-4285F4?style=for-the-badge&logo=google">
  <img src="https://img.shields.io/badge/MySQL-Database-orange?style=for-the-badge&logo=mysql">
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge">
</p>

<p align="center">
<b>Your AI-Powered Personal Cookbook</b><br>
Generate delicious recipes instantly using Google Gemini AI based on ingredients, cuisines, or cravings.
</p>

---

# 📖 About The Project

Meal Genie is an **AI-powered recipe generation web application** that helps users discover personalized recipes in seconds.

Instead of searching through hundreds of websites, users simply enter ingredients or meal preferences, and **Google Gemini AI** generates a complete recipe including ingredients, cooking instructions, preparation time, serving size, and helpful cooking tips.

The application also stores generated recipes in a **MySQL database**, allowing users to revisit their favorite meals while providing a modern, responsive, and interactive user experience through **Streamlit**.

---

# ✨ Features

### 🤖 AI Recipe Generation
- Generate recipes using Google's Gemini AI
- Personalized recipe suggestions
- Natural language understanding

### 🥘 Smart Recipe Creation
- Ingredient-based recipes
- Cuisine-specific recipes
- Meal type recommendations
- Cooking instructions
- Preparation & cooking time
- Serving size

### 🎨 Beautiful User Interface
- Modern Apple-inspired design
- Responsive layout
- Interactive cards
- Smooth animations
- Custom CSS styling

### 🌗 Personalization
- Dark Mode
- Light Mode
- Adjustable Font Size
- User-friendly interface

### 📚 Recipe Management
- Save generated recipes
- Recipe history
- View previously generated recipes
- Organized storage using MySQL

### ⚡ Performance
- Fast AI response
- Lightweight Streamlit application
- Easy deployment

---

# 🛠 Tech Stack

## Frontend

- Streamlit
- HTML Components
- CSS

## Backend

- Python

## Artificial Intelligence

- Google Gemini AI (Gemini 2.5 Flash)

## Database

- MySQL

## Python Libraries

- Streamlit
- google-genai
- PyMySQL
- mysql-connector-python

---

# 📂 Project Structure

```
Meal-Genie/
│
├── app.py                 # Main Streamlit Application
├── database.py            # Database Functions
├── requirements.txt
├── README.md
│
├── assets/
│     ├── images/
│     └── icons/
│
├── database/
│     └── meal_genie.sql
│
└── screenshots/
      ├── home.png
      ├── recipe.png
      ├── history.png
      └── darkmode.png
```

---

# 🚀 Getting Started

## Prerequisites

Before running the project, install:

- Python 3.10 or above
- MySQL Server
- Git

---

# Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/Meal-Genie.git

cd Meal-Genie
```

---

# Create a Virtual Environment

## Windows

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

---

## macOS / Linux

```bash
python3 -m venv venv
```

Activate:

```bash
source venv/bin/activate
```

---

# Install Required Libraries

### Method 1 (Recommended)

```bash
pip install -r requirements.txt
```

---

### Method 2 (Manual Installation)

```bash
pip install streamlit
pip install google-genai
pip install PyMySQL
pip install mysql-connector-python
```

---

# Configure Google Gemini API

Create an API Key from:

https://aistudio.google.com/app/apikey

Do **NOT** hardcode the key inside your project.

Instead create a `.env` file:

```
GEMINI_API_KEY=YOUR_API_KEY
```

Or use Streamlit Secrets.

---

# Configure MySQL

Create a database:

```sql
CREATE DATABASE meal_genie;
```

Update your database credentials inside the project:

```python
host="localhost"
user="root"
password="YOUR_PASSWORD"
database="meal_genie"
```

---

# Run the Application

```bash
streamlit run app.py
```

The application will automatically open in your browser.

Default URL:

```
http://localhost:8501
```

---

# Screenshots

Add screenshots inside the `screenshots` folder.

Example:

```
screenshots/
│
├── home.png
├── recipe.png
├── history.png
├── darkmode.png
```

Then display them like this:

```markdown
## Home Page

![Home](screenshots/home.png)

## Generated Recipe

![Recipe](screenshots/recipe.png)

## Dark Mode

![Dark](screenshots/darkmode.png)
```

---

# Future Enhancements

- Voice-based recipe generation
- Nutrition calculator
- Calorie estimation
- Weekly meal planner
- Shopping list generation
- Image generation for recipes
- Recipe sharing
- User authentication
- Cloud database integration
- Docker deployment
- Multi-language support

---

# Troubleshooting

### ModuleNotFoundError

Install dependencies:

```bash
pip install -r requirements.txt
```

---

### MySQL Connection Error

- Check if MySQL Server is running.
- Verify username and password.
- Ensure the database exists.

---

### Gemini API Error

- Verify your API key.
- Ensure billing/quota is available.
- Check your internet connection.

---

# Contributing

Contributions are always welcome.

1. Fork the repository.
2. Create a new feature branch.

```
git checkout -b feature-name
```

3. Commit your changes.

```
git commit -m "Added new feature"
```

4. Push to GitHub.

```
git push origin feature-name
```

5. Create a Pull Request.

---

# License

This project is licensed under the MIT License.

---

# Author

### 👩‍💻 Jahnavi Modi

Computer Science Engineering Student

Interested in:

- Artificial Intelligence
- Full Stack Development
- Product Design
- UI/UX
- Machine Learning

GitHub: https://github.com/YOUR_USERNAME

LinkedIn: https://linkedin.com/in/YOUR_LINKEDIN

---

# ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub.

It motivates further development and helps others discover the project.

---

<p align="center">
Made with ❤️ using Python, Streamlit, MySQL and Google Gemini AI
</p>

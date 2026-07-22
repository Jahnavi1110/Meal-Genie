import os
from dotenv import load_dotenv
import pymysql

# Load environment variables
load_dotenv()

# Database configuration
DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME"),
}

try:
    connection = pymysql.connect(**DB_CONFIG)

    print("✅ Successfully connected to the MySQL database!")
    print(f"Connected to database: {DB_CONFIG['database']}")

    connection.close()
    print("🔒 Database connection closed.")

except pymysql.MySQLError as e:
    print("❌ Database connection failed!")
    print(f"Error: {e}")

except Exception as e:
    print("❌ Unexpected error occurred!")
    print(f"Error: {e}")

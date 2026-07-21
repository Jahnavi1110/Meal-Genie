import mysql.connector

print("--- 🔍 DIAGNOSTIC TEST STARTING ---")

config = {
    "host": "127.0.0.1",
    "user": "root",
    "password": "Saibaba11",  # <--- Update this
    "database": "mygenie",
    "use_pure": True  # <--- THE MAGIC FIX
}

try:
    print("Attempting to connect...")
    conn = mysql.connector.connect(**config)

    if conn.is_connected():
        print("✅ SUCCESS! Connection established in Pure Python mode.")
        conn.close()
    else:
        print("❌ Connection failed.")

except Exception as e:
    print(f"❌ Error: {e}")

import os
import requests

# Hardcoded sensitive data (SonarQube should flag these)
API_KEY = "12345-SECRET-API-KEY"
DB_PASSWORD = "supersecretpassword"

def fetch_data():
    url = "https://jsonplaceholder.typicode.com/posts"
    headers = {"Authorization": f"Bearer {API_KEY}"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        print("Data fetched successfully!")
        return response.json()
    else:
        print("Failed to fetch data!")
        return None

def connect_db():
    # Simulating DB connection with hardcoded password (bad practice)
    print(f"Connecting to DB with password: {DB_PASSWORD}")
    return True

if __name__ == "__main__":
    data = fetch_data()
    if data:
        print("First Post Title:", data[0]['title'])
    connect_db()

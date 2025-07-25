
import os
from dotenv import load_dotenv
import requests

# Load token from .env file
load_dotenv()

# Get token from environment variable
token = os.getenv('token')

# Set headers with token
headers = {
    'Authorization': f'Token {token}'
}

# Make GET request to your Django API endpoint
response = requests.get('http://127.0.0.1:8000/todo/todos/', headers=headers)

# Print the JSON response
print(response.status_code)
print(response.json())
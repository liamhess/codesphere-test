import requests
import os

backend_address: str = os.environ.get("BACKEND_ADDRESS")

def subscribe_user(email: str, interests: str):
    body = {
        "email": email,
        "interests": interests
    }
    response = requests.post(backend_address + "/subscribe", json=body)
    print(response.status_code)
    return response.status_code
    
def unsubscribe_user(email: str):
    body = {
        "email": email
    }
    response = requests.post(backend_address + "/unsubscribe", json=body)
    print(response.status_code)
    return response.status_code

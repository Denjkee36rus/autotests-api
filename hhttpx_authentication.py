import httpx


login_payload = {
  "email": "chekalkin_92@mail.ru",
  "password": "12345"
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()
print(login_response.json())
print(login_response.status_code)

refresh_payload = {
   "refreshToken": login_response_data["token"]["refreshToken"]
}

refresh_responce = httpx.post("http://localhost:8000/api/v1/authentication/refresh", json=refresh_payload)
refresh_response_data = refresh_responce.json()

print(refresh_responce.json())
print(refresh_responce.status_code)


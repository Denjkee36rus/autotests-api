import httpx

from httpx_get_user import get_user_headers
from tools.fakers import get_random_email_fake



create_user_payload = {
  "email": get_random_email_fake(),
  "password": "string",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}

create_new_user_response = httpx.post("http://localhost:8000/api/v1/users", json=create_user_payload)
create_new_user_response_data = create_new_user_response.json()
print(f"Registration New User: {create_new_user_response_data}")

authentication_payload = {
    "email": create_user_payload["email"],
    "password": "string"
  }
login_new_user_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=authentication_payload)
login_new_user_response_data = login_new_user_response.json()

print(login_new_user_response.status_code)
print(f"Авторизация: {login_new_user_response_data}")

update_user_payload = {
  "email": get_random_email_fake(),
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}

get_new_user_headers = {
  "Authorization": f"Bearer {login_new_user_response_data['token']['accessToken']}"
}
update_user_response = httpx.patch(f"http://localhost:8000/api/v1/users/{create_new_user_response_data['user']['id']}",
                                   json= update_user_payload,
                                   headers=get_new_user_headers)
update_user_response_data = update_user_response.json()
print(f"New Email: {update_user_response_data['user']['email']}")
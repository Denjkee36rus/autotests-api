import httpx
from httpx import request

response = httpx.get("https://jsonplaceholder.typicode.com/todos/1")


data = {
    "title":"New task",
    "completed":False,
    "userId": 2
}

# params = {"userId":1}
# response = httpx.post("https://jsonplaceholder.typicode.com/todos", json=data)
#
#
# response = httpx.get("https://jsonplaceholder.typicode.com/todos", params = params)
# with httpx.Client() as client:
#     response1 = client.get("https://jsonplaceholder.typicode.com/todos/1")
#     response2 = client.get("https://jsonplaceholder.typicode.com/todos/2")
#
# print(response1.json(), response2.json())

client = httpx.Client(headers={"Authorization": "Bearer my_secret_token"})
response = client.get("https://httpbin.org/get")

try:
    response = httpx.get("https://jsonplaceholder.typicode.com/inavalin-url")
    response.raise_for_status()
except httpx.HTTPStatusError as e:
    print(f"Ошибка запроса: {e}")

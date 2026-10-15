import requests

response = requests.get(
    "https://jsonplaceholder.typicode.com/todos/1",
    timeout = 10
)
if response.status_code == 404:
    print("Resource not found!")
else:
    print("Status code:", response.status_code)
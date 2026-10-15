
import requests

try:
    response = requests.get(
        "https://jsonplaceholder.typicode.com/todos/1",
        timeout=10
    )

    response.raise_for_status()

    data = response.json()

    print(f"Task: {data['title']}")
    print(f"Completed: {data['completed']}")
    print(f"User ID: {data['userId']}")

except requests.exceptions.Timeout:
    print("The request timed out.")

except requests.exceptions.HTTPError as error:
    print(f"HTTP error: {error}")

except requests.exceptions.RequestException as error:
    print(f"Request failed: {error}")

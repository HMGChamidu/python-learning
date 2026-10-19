
import requests


def count_tasks(tasks):
    completed_count = 0
    incomplete_count = 0

    for task in tasks:
        if task["completed"]:
            completed_count += 1
        else:
            incomplete_count += 1

    return completed_count, incomplete_count


url = "https://jsonplaceholder.typicode.com/todos"

try:
    # 1. Fetch tasks from the API
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    tasks = response.json()

    # 2. Count completed and incomplete tasks
    completed, incomplete = count_tasks(tasks)

    # 3. Display the menu
    print("Status code:", response.status_code)
    print("Total tasks:", len(tasks))
    print("\nWhat would you like to see?")
    print("1. Show the first 5 tasks")
    print("2. Show completed task count")
    print("3. Show incomplete task count")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        for task in tasks[:5]:
            print(task["title"])

    elif choice == "2":
        print("Completed tasks:", completed)

    elif choice == "3":
        print("Incomplete tasks:", incomplete)

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

except requests.exceptions.Timeout:
    print("Error: The request took too long.")

except requests.exceptions.ConnectionError:
    print("Error: Check your internet connection.")

except requests.exceptions.HTTPError:
    print("Error: The API returned an unsuccessful status code.")

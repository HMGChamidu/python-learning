
import requests


# 1. Count completed and incomplete tasks
def count_tasks(tasks):
    completed_count = 0
    incomplete_count = 0

    for task in tasks:
        if task["completed"]:
            completed_count += 1
        else:
            incomplete_count += 1

    return completed_count, incomplete_count


# 2. Display the menu and handle user choices
def show_menu(tasks, completed, incomplete):
    while True:
        print("\n===== TODO MENU =====")
        print("1. Show the first 5 tasks")
        print("2. Show completed task count")
        print("3. Show incomplete task count")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            print("\nFirst 5 tasks:")

            for task in tasks[:5]:
                print("-", task["title"])

        elif choice == "2":
            print("Completed tasks:", completed)

        elif choice == "3":
            print("Incomplete tasks:", incomplete)

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


# 3. Fetch tasks from the API
url = "https://jsonplaceholder.typicode.com/todos"

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    tasks = response.json()

    print("Status code:", response.status_code)
    print("Total tasks:", len(tasks))

    completed, incomplete = count_tasks(tasks)

    print("Completed tasks:", completed)
    print("Incomplete tasks:", incomplete)

    # 4. Start the repeating menu
    show_menu(tasks, completed, incomplete)

except requests.exceptions.Timeout:
    print("Error: The request took too long.")

except requests.exceptions.ConnectionError:
    print("Error: Check your internet connection.")

except requests.exceptions.HTTPError:
    print("Error: The API returned an unsuccessful status code.")

except requests.exceptions.RequestException:
    print("Error: Something went wrong with the API request.")

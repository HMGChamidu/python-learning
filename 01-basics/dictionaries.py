developer = {
    "name" : "Chamidu",
    "role" : "DevOps Engineer",
    "language" : "Python",
    "experience" : 5
}

print(developer)
print(developer["name"])
print(developer["role"])

developer["country"] = "Sri Lanka"
developer["language"] = "Java"

developer.pop("experience")

print(developer)

for key, value in developer.items():
    print(f"{key}: {value}")

    
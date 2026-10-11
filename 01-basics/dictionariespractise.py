developer = {
    "name" : "Chamidu Sandeepa",
    "role": "DevOps Engineer",
    "Country": "Sri Lanka",
    "Language": "Python"
}

print(developer["name"])
print(developer["role"])

developer["Exeperience"] = 2
developer["language"] = "Python"

for key,value in developer.items():
    print(f"{key}: {value}")
languages = ["python", "java", "Javascript", "PHP"]

print(languages)
print(languages[0])
print(languages[1])

skills = ["HTML", "css", "JavaScript"]
skills[1] = "React"

print(skills)

#usefull list methods

skills = ["HTML", "CSS", "JavaScript"]

skills.append("Python") #Add an item
skills.remove("CSS") #Remove an item
skills.insert(1,"React") #Insert an item at a specific index

print(skills)

print(len(skills))

projects = ["Portfolio", "Solar API", "Student Tracking APP"]

for project in projects:
    print(project)
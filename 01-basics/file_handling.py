with open("notes.txt", "w") as file:
    file.write("I am learning Python.\n")
    file.write("Next, I will build APIs.")

print("File saved successfully!")

with open("notes.txt", "r") as file:
    content = file.read()
with open("notes.txt", "a") as file:
    file.write("\nI am building Python projects.")

print("New line added!")

print(content)
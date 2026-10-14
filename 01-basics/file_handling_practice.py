

with open("tasks.txt", "w") as file:
    file.write("Learn Python functions\n")


with open("tasks.txt", "a") as file:
    file.write("Build a Python API\n")

with open("tasks.txt", "r") as file:
    for line in file:
        print(line.strip())

age = 23

if age >= 18:
    print("You are an adult.")

    age = 16

    if age >= 18:
        print("You are an adult.")
    else:
        print("You are a minor.")


username = "admin"
password = "password123"

entered_username = "admin"
entered_password = "password123"

if entered_username == username and entered_password == password:
    print("Login successful.")  
else:

    print("Invalid username or password.")



marks = 70

if marks >= 75:
    print("A")
elif marks >= 65:
    print("B")
elif marks >= 55:
    print("C")
else:
    print("Fail")
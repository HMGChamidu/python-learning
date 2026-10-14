
def introduce(name, role, country):
    print(f"My name is {name}, I am a {role}, and I am from {country}.")

introduce("Chamidu Sandeepa", "DevOps Engineer", "Sri Lanka")


def calculate_total(price, quantity):
    return price * quantity

total = calculate_total(1500,3)
print(total)


def calculate_discount(price, quantity, discount_percentage):
    total = price * quantity
    discount = total * (discount_percentage / 100)
    return total - discount

final_price = calculate_discount(2000, 3,10)
print(final_price)

def greet (name, message="Welcome"):
   print(f"{message}, {name}!")

greet("Chamidu")
greet("Chamidu", "Good morning")


def introduce(name, role, country):
    print(f"{name} is a {role} from {country}.")


introduce(
        country="Sri Lanka",
        name="Chamidu Sandeepa",
        role="DevOps Engineer"

    )

name = "Chamidu"

def greet():
    message = "Hello"
    print(f"{message}, {name}!")

greet()
print(name)  



name = "Chamidu"

def change_name():
    name = "Alex"
    print("Inside:", name)

change_name()
print("Outside:", name)
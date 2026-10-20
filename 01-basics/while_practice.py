while True:
    print("1.Say hello")
    print("2.Exit")

    choice = input("Choose: ")

    if choice == "1":
        print("Hello, bro!")

    elif choice == "2":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")
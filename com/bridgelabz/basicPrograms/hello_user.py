name = input("Enter User Name")  # Takes users input
if len(name) > 3:  # Checks for input length
    print("Hello", name, "How are you")
else:
    print("User name should be minimum three characters")
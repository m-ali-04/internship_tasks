# function_arguments.py

# 1. Regular arguments
def greet(name):
    print("Hello", name)

greet("Ali")


# 2. Default arguments
def greet(name="Guest"):
    print("Hello", name)

greet()
greet("Zara")


# 3. *args - Variable number of positional arguments
def add_all(*numbers):
    total = sum(numbers)
    print("Sum:", total)

add_all(1, 2, 3)
add_all(10, 20)


# 4. **kwargs - Variable number of keyword arguments
def show_profile(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

show_profile(name="Ali", age=22, city="Lahore")

#my own example
def user_summary(username, role="Member", *hobbies, **extra_info):
    print(f"Username: {username}")
    print(f"Role: {role}")
    
    if hobbies:
        print("Hobbies:")
        for h in hobbies:
            print(f"- {h}")
    else:
        print("No hobbies listed.")

    if extra_info:
        print("Extra Info:")
        for key, value in extra_info.items():
            print(f"{key}: {value}")
    else:
        print("No extra info provided.")

    print("\n")  # Just for spacing


# Example 1 - Only required arg
user_summary("ali82")

# Example 2 - Required + default overridden
user_summary("ayesha97", "Admin")

# Example 3 - With *args
user_summary("raheel21", "Moderator", "reading", "gaming", "cycling")

# Example 4 - With *args and **kwargs
user_summary("sana_k", "Editor", "photography", location="Karachi", age=25)

# Example 5 - Full combo
user_summary("faizan_dev", "Contributor", "coding", "music", city="Lahore", joined="2023", verified=True)

# Constants
PASSWORD = "secret"
MAX_ATTEMPTS = 5

# Program
success = False
for attempts in range(MAX_ATTEMPTS):
    word = input("Enter the password: ")

    # Program
    if word == PASSWORD:
        print("Access granted")
        success = True
        break
    else:
        print("Access denied")

    print(f"Attempt {attempts + 1} of {MAX_ATTEMPTS}")

if not success:
    print("You are locked out") 

    
    



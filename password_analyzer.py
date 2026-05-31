
# Greetings
print("Password Analyzer")
print("=================")
# giving samples to compare 
special_char = "`~!@#$%^&*()_-+={[]};:<,>.?/|\\\""
common_password = ["password", "12345678", "password123", "12341234"]

# defining the method
def password_analyzer():
    special_check = False
    
    # getting input from the user
    user_password = input("Enter Your Password : ")
    
    # Validation 1: Check Length
    if len(user_password) < 8:
        print("This Password is Too Short...! Try Again")
        password_analyzer()  # Restart
        return  # Stop execution of the current function instance

    # Validation 2: Scan for special characters quietly
    for ch in user_password:
        if ch in special_char:
            special_check = True
            break  # Found one, we can stop the loop safely

    if not special_check:
        print("Use a special character in Password For Better Security..!!")
        password_analyzer()  # Restart
        return 

    # Validation 3: Check for common passwords (no loop required)
    if user_password.lower() in common_password:
        print("[🚨 WARNING]: This is a very common password. Try Again.")
        password_analyzer()  # Restart
        return 

    # If the code reaches here, all security checks passed successfully!
    print("\n======================================")
    print("✅ SUCCESS: Your password is safe and strong!")
    print("======================================")

password_analyzer() # calls the function

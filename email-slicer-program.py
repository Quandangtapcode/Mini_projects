import re 

email = input("Enter your email: ")
#ex: abc@gmail.com

pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

if re.match(pattern, email):
    index = email.index("@")
    username = email[:index]
    domain = email[index + 1 :]
    print(f"Your username is: {username} and domain is: {domain}")
else:
    print("Please enter the gmail format correctly (ex: abc@gmail.com).")    
    



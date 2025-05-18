def add(x,y):
    return x + y
    
def subtract(x,y):
    return x - y
    
def multiply(x,y):
    return x * y
    
def divide(x,y):
    if y == 0:
        return "Error: Can not divide by zero"
    return x / y 

def calculator():
    while True:
        print("\n====Calculator====")
        print("Select operation: ")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Divide (/)") 
        print("5. Exit")
    
    
        choice = input("Enter choice: ")
        if choice == '5':
            print("Exit.")
            break 
        
        if choice not in ['1', '2', '3', '4']:
            print("Invalid input.")
            continue
    
    
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input number.")
            continue
    
    
        if choice == '1':
            result = add(num1, num2)
        elif choice == '2':
            result = subtract(num1, num2)
        elif choice == '3':
            result = multiply(num1, num2)
        elif choice == '4':
            result = divide(num1, num2)
          
        print("Result: ", result)
                
if __name__=='__main__':
    calculator()            
            
              
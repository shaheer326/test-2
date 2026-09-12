print("==========================") 
print(" Calculator") 
print("==========================") 

def calculate():
    global user_value, num1, num2 
    
    def addition(): 
        if user_value == "+": 
            print(num1 + num2) 
        else: 
            pass 
            
    def subtraction(): 
        if user_value == "-": 
            print(num1 - num2)
        else: 
            pass 
            
    def multiplication(): 
        if user_value == "*": 
            print(num1 * num2)
        else: 
            pass 
            
    def division(): 
        if user_value == "/": 
            if num2 == 0:
                print("zero division error")
            else:
                print(num1 / num2)
            pass 

    try: 
        user_value = input("Enter a opration (+, -, *, /): ") 
        num1 = float(input("Enter the First number: ")) 
        num2 = float(input("Enter the Second number: ")) 
        
        addition()
        subtraction()
        multiplication()
        division()
        
    except ValueError: 
        print("wrong input") 

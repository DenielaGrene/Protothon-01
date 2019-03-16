def add(num1, num2): 
    return num1 + num2 
  
  
def subtract(num1, num2): 
    return num1 - num2 
  

def multiply(num1, num2): 
    return num1 * num2 
  
 
def divide(num1, num2): 
    return num1 / num2 
  
print("Please select operation -\n" 
        "1. Add\n" 
        "2. Subtract\n" 
        "3. Multiply\n" 
        "4. Divide\n") 
  
  

it = input("Select operations form 1, 2, 3, 4 :") 
 
x = dict()
x['number_1'] = float(input("Enter first number: ")) 
x['number_2'] = float(input("Enter second number: ")) 
  
if it == '1':
      print(x['number_1'], "+", x['number_2'], "=", 
                    add(x['number_1'], x['number_2'])) 
   

elif it == '2': 
    print(x['number_1'], "-", x['number_2'], "=", 
                    subtract(x['number_1'], x['number_2'])) 
  
elif it == '3': 
    print(x['number_1'], "*", x['number_2'], "=", 
                    multiply(x['number_1'], x['number_2'])) 
  
elif it == '4': 
    print(x['number_1'], "/", number_2, "=", 
                    divide(x['number_1'], x['number_2'])) 
else: 
    print("Invalid input")
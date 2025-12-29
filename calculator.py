print ("=== SIMPLE CALCULATOR ===")
print ("1.Addition")
print ("2.Subtraction")
print ("3.Multiplication")
print ("4. Division")

choice = input ("Choose an opration (1-4): ")

num1 = float (input("Enter first number: "))
num2 = float (input ("Enter second number: "))

if choice == "1":
    print ("Result:", num1+num2)
elif choice == "2":
    print ("Result:", num1 - num2)
elif choice == "3":
    print ("Result:", num1 * num2)
elif choice == "4":
    if num2 == 0:
         print ("Error: Cannot divide by zero")
    else:
        print ("Result:", num1/num2)
else:
    print("Invalid choice")

    
                

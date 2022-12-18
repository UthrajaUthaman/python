# Program to generate a simple calculator

while True:
    print("Select an operation to perform :")
print("1. ADD")
print("2. SUBTRACT")
print("3. MULTIPLY")
print("4. DIVIDE")

choice = int(input("Enter an option :"))

if choice == "1":
    num1 = float(input("Enter number 1 :"))
    num2 = float(input("Enter number 2 :"))
    print(num1,"+",num2,"=",(num1+num2))
elif choice == "2":
    num1 = float(input("Enter number 1 :"))
    num2 = float(input("Enter number 2 :"))
    print(num1,"-",num2,"=",(num1-num2))
elif choice == "3":
    num1 = float(input("Enter number 1 :"))
    num2 = float(input("Enter number 2 :"))
    print(num1,"*",num2,"=",(num1*num2))
elif choice == "4":
    num1 = float(input("Enter number 1 :"))
    num2 = float(input("Enter number 2 :"))
    print(num1,"/",num2,"=",(num1/num2))
else:
    print("Invalid entry")


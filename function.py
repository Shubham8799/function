print("1. addition")
print("2. Multiplication ") 
operation = input("choose number:")
if operation =="1":
   num1 = input("enter first number : ")
   num2 = input("enter second number :")
   print(int(num1)+int(num2))
elif operation == "2":
    num1 = input("enter first number : ")
    num2 = input("enter second number :")
    print(int(num1)*int(num2))
else:
  print("invalid input 🤨")

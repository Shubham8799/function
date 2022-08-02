print("1. addition")
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
  print("invalid")

#Simple Calculator
num1 = int(input("Enter you number : "))
num2 = int(input("Enter your second number : "))
opr = input("Give me an operation to perform : ")

if opr == "+":
  print(num1+num2)
elif opr == "-":
 print(num1-num2)
elif opr == "*":
  print(num1*num2)
elif opr == "/":
 print(num1/num2)
else:
  print("wrong input")
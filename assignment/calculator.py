# 1. Add
# 2. Subtract
# 3. multiply
# 4. Division

print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Division")

operation=input()

if operation== "1":
  num1=input("Enter the first number ")
  num2=input("Enter the second number ")
  print("The sum is " + str(int(num1) + int(num2)))
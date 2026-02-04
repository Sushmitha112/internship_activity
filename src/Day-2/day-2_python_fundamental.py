
age = 10
height = 5.9
name = "sush"
is_student = True

print(type(age))
print(type(height))
print(type(name))
print(type(is_student))
print("Data types printed successfully")

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
opp = input("Enter the operation  to perform (+, -, *, /, %): ")

if opp == '+':
    print("The sum of two numbers is:", a + b)

elif opp == '-':
    print("The difference of two numbers is:", a - b)

elif opp == '*':
    print("The product of two numbers is:", a * b)

elif opp == '/':
    if b != 0:
        print("The quotient of two numbers is:", a / b)
    else:
        print(" Division by zero is not allowed.")

elif opp == '%':
    if b != 0:
        print("The remainder of two numbers is:", a % b)
    else:
        print(" Division by zero is not allowed.")

else:
    print("Invalid operation")

#Task 1
name=input("enter the name:")
age=int(input("enter the age:"))
print(f"Hey {name}, you will be {age+4} next year 2030 !")
print(f"i am {name},nice to meet you,and i am {age} old")

#Task 2
total_amount=float(input("enter the total bill amount:"))
total_perosns=int(input("enter the total persons:"))
total_split=total_amount/total_perosns
print(f"Total Bill: {total_amount}. Each person pays: {total_split}")
print(type(total_amount))
print(type(total_perosns))

#Task 3
item_name=str(input("enter the item name:"))
item_price=int(input("enter the item price:"))
item_qut=int(input("enter the Qty:"))
price=item_price*item_qut
in_stock=True
print(f"Item:{item_name}, Price:{item_price}, Qty:{item_qut},Total Price:{price},Available:{in_stock}")


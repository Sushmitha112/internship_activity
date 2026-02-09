# file=open("sample.txt","w")
# file.write("hello,this is a file handling example")
# file.close()
# file=open("sample.txt","r")
# content=file.read()
# print(content)
# file.close()
#open() and close() are the contenxt manager function used for opening and closing the file respectivly.
# with open("sample.txt","r") as file:
#     content=file.read()
#     print(content)

# try:
#     with open("missing.txt","r") as file:
#         content=file.read()
#         print(content)    
# except FileNotFoundError:
#     print("The file was not found. Please check the file name.")
# import csv
# with open("data.csv","r") as file:
#     reader=csv.reader(file)
#     for row in reader:
#         print(row)

# from openpyxl import load_workbook

# wb = load_workbook("data1.xlsx")
# sheet = wb.active   # gets the first sheet

# for row in sheet.iter_rows(values_only=True):
#     print(row)

# name=input("enter your name: ")
# daily_goal=input("enter your daily goal:")
# with open("journal.txt","a")as file:
#     file.write(f"Name:{name}\n")
#     file.write(f"daily goal:{daily_goal}\n")
# file.close() 
# 
# import csv
# with open("students.csv", "r") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         if row[2] == "Pass":
#             print(row[0])

f1=input("enter the file name:")
try:
    with open(f1,"r")as file:
        reader=file.read()
        print(reader)
except FileNotFoundError:
    print("Oops! That file doesn't exist yet")

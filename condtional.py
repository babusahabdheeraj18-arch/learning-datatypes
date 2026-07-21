'''a=int(input("enter the number:"))
if a<0:
    print("a is negative")
else:
    print("a is positive")'''

#2 looking for greater number 
# a=int(input("enter the first number:"))
# b=int(input("enter the second number:"))
# if a<b:
#     print("a is less then b")
# else:
#     print("a is greater then b")

#checking whetehr student is pass or fail
# marks=int(input("enter the marks:"))
# student=input("enter the student name:")
# if marks>=33:
#     print(f"{student} is pass")
# else:
#     print(f"{student} is fail")
#check wheteher year is leap year or not
# year=int(input("enter the year:"))
# if year%4==0:
#     if year%100==0:
#         if year%400==0:
#             print(f"{year} is a leap year")
#         else:
#             print(f"{year} is not a leap year")
#     else:
#         print(f"{year} is a leap year")
# else:
#     print(f"{year} is not a leap year") 

#number is divisble by 3 nd 7
# num=int(input("enter the number:"))
# if num%3==0 and num%7==0:
#     print(f"{num} is divisible by 3 and 7")
# else:
#     print(f"{num} is not divisible by 3 and 7")

#finding the greatest number among three numbers
# a=int(input("enter the first number:"))
# b=int(input("enter the second number:"))
# c=int(input("enter the third number:"))
# if a>b and a>c:
#      print(f"{a} is the greatest number")
# elif b>a and b>c:
#     print(f"{b} is the greatest number")
# else:
#     print(f"{c} is the greatest number")

#addibng grades to students based on marks
# marks=int(input("enter the marks:"))
# if 90<marks<=100:
#     print("A+")
# elif 80<marks<=90:
#     print("B")
# elif 70<marks<=80:
#     print("C")
# elif 60<marks<=70:
#     print("D")
# elif 50<marks<=60:
#     print("E")
# elif 33<=marks<=50:
#     print("F")    
# else:
#     print("student is fail")

#calculate a simple calculator using if else statement
num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
operation=input("enter the operation (+, -, *, /):")
if operation=="+":
    print(f"{num1} + {num2} = {num1+num2}")
elif operation=="-":
    print(f"{num1} - {num2} = {num1-num2}")
elif operation=="*":
    print(f"{num1} * {num2} = {num1*num2}")
elif operation=="/":
    print(f"{num1} / {num2} = {num1/num2}")
else:
    print("Invalid operation")

#count the number of positive number in the list 
# num=[1,-2,3,-4,5,-6,7,-8,9,10]
# n = len(num)
# count=0
# for i in num:
#     if i<0:
#         count+=1
# print("Number of positive numbers:", n-count)

#calculate the sum of even no upto a given numbers 
# sum=0
# for i in range(1,21):
#     if i%2==0:
#         sum+=i
# print("Sum of even numbers:", sum)

# #calculate the sum of odd numbers upto a given numbers
# sum=0
# for i in range(1,21):
#     if i%2!=0:
#         sum+=i
# print("Sum of odd numbers:", sum)

# #print the multiplication table of a given number 
# number=int(input("Enter a number: "))
# for i in range(1,11):
#     print(number,"*",i,"=",number*i)

#reverse a string using for loop
# string="Elephant"
# for i in range(len(string)-1,-1,-1):
#     print(string[i],end="")

#given as string,find the first repeating character in it
# string = "programming"
# for char in string:
#     if string.count(char) > 1:
#         print("The first repeating character is:", char)
#         break
    

# #find the factorial of a number 
# num=int(input("Enter a number: "))
# factorial=1
# for i in range(1,num+1):
#     factorial*=i
# print("The factorial of", num, "is:", factorial)

#keep asking the user to enter a number until they enter a between 1 and 10
# while True:
#     num=int(input("Enter a number between 1 and 10: "))
#     if 1<=num<=10:
#         print("Thank you!")
#         break
#     else:
#         print("Invalid input. Please try again.")

#check whether a number is prime or not
# num=int(input("Enter a number: "))
# is_prime=True
# for i in range(2,num):
#     if num%i==0:
#         is_prime=False
#         break
# if is_prime:
#     print("The number is prime.")
# else:
#     print("The number is not prime.")

#check all element in list are unique and if duplicate print duplicate value
# items=["apple","banana","orange","orange","apple","grape","orange"]
# duplicates = []
# for fruits in items:
#     if items.count(fruits)>1 and fruits not in duplicates:
#         duplicates.append(fruits)
# for fruit in duplicates:
#     print(fruit,"is duplicate")
# if not duplicates:
#     print('All elements are unique')

#exponential backoff algorithm
import time
wait_time = 1

for i in range(6):
    print(f"Retry {i}: {wait_time} seconds")
    time.sleep(wait_time)
    wait_time = wait_time * 2
    if wait_time > 32:
        break
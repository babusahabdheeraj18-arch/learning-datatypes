#print all the even between 1 to 20 using while loop
# i = 1
# while i<=20:
#     if i%2==0:
#         print(i)
#     i=i+1

# #print all the odd between 1 to 20 using while loop
# i = 1
# while i<=20:
#     if i%2!=0:
#         print(i)
#     i=i+1

#print multiplication table of a given number using while loop
# num=int(input("Enter a number: "))
# i=1
# while i<=10:
#     print(num,"*",i,"=",num*i)
#     i+=1

#Keep asking the user to enter a number until they enter 0
# num=int(input("Enter a number: "))
# while num!=0:
#     print("You entered:", num)
#     num=int(input("Enter a number (0 to exit): "))

#Ask the user to enter a password until they enter the correct password.
# correct_password="python123"
# password=input("Enter the password: ")
# while password!=correct_password:
#     print("Incorrect password. Please try again.")
#     password=input("Enter the password: ")
# print("Access granted.")

#Keep taking numbers from the user and find their sum. Stop when the user enters -1.
# sum=0
# user_input=int(input("Enter a number (-1 to stop): "))
# while user_input!=-1:
#     sum+=user_input
#     user_input=int(input("Enter a number (-1 to stop): "))
# print("The sum is:", sum)

#Count how many numbers the user entered before entering 0.
# count=0
# user_input=int(input("Enter a number (0 to stop): "))     
# while user_input!=0:
#     count+=1
#     user_input=int(input("Enter a number (0 to stop): "))
# print("You entered", count, "numbers before entering 0.")

#reverse a number using while loop
#reverse=0
# num=int(input("Enter a number: "))
# while num>0:
#     digit=num%10
#     reverse=reverse*10+digit
#     num=num//10
# print("The reversed number is:", reverse)

#count the number of digits in a number using while loop
# num=int(input("Enter a number: "))
# count=0
# while num>0:
#     num=num//10
#     count+=1
# print("The number of digits is:", count)

#sum of digits in a number using while loop
# num=int(input("Enter a number: "))
# sum=0
# while num>0:
#     digit=num%10
#     sum=sum+digit
#     num=num//10
# print("The sum of digits is:", sum)
 
#check whether a number is palindrome or not using while loop
# num=int(input("Enter a number: "))
# original_num=num
# reverse=0  
# while num>0:
#     digit=num%10
#     reverse=reverse*10+digit
#     num=num//10
# if original_num==reverse:
#     print("The number is a palindrome.")
# else:
#     print("The number is not a palindrome.")

#check whether a number is prime or not using while loop

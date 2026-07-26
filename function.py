# def fun(name):
#     print("Hello, " + name + "!")
# fun("dheeraj")    

# def student(fname, lname):
#     print(fname, lname)

# student('Geeks','Practice')
# student('Practice','Geeks')

# def f1():
#     s = 'I love GeeksforGeeks'
#     def f2():
#         print(s)
        
#     f2()
# f1()

# def myFun(*args, **kwargs):
#     print("Non-Keyword Arguments (*args):")
#     for arg in args:
#         print(arg)

#     print("Keyword Arguments (**kwargs):")
#     for key, value in kwargs.items():
#         print(f"{key} == {value}")

# myFun('Hey', 'Welcome', first='Geeks', mid='for', last='Geeks')

# def myFun(x):
#     x[0] = 20

# b = [10, 11, 12, 13]
# myFun(b)
# print(b)

# def myFun2(x):
#     x = 20

# a = 10
# myFun2(a)
# print(a)

# res = lambda x: x * x
# print(res(4))

# def function(n):
#     if n==4:
#         return n
#     else:
#         return 2*function(n+1)
        
# print(function(2))

#pratice problem 
# def sum(a,b):
#     print(a+b)
# sum(10,20)

# def square(x):
#     print(x*-x)
# square(5)

def max(a, b, c):
    if a>b & a>c:
        print("a is greater ")
    elif b>a & b>c:
        print("b is greater")
    else:
        print("c is greater")

max(10, 40, 30)
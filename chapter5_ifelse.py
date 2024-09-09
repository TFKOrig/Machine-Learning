#eligible for vote

age=input("Enter your age: ")

#age=int(input("Enter your age: "))
                #or
age=int(age)                


if(age>=18):
    print("You are eligible for casting vote")

else:
    print("You are not eligible for casting vote")


a=10
b=20

if(a>b):
    print("a is greater than b")
elif a==b:
    print("a is equal to b")
else:
    print("b is greater")    


i=10
j=20
k=30


if(i>j>k):
    print("i is greater than j and k")
elif(i<j>k):
    print("j is greater than i and k")
else:
    print("k is greater than i and j")
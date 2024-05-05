# a =int(input("Enter your age :"))
# print("Your age is", a)
# if (a>=18) :
#     print("You can drive")
# else :  
#     print("You can not drive")

# num=float(input("Enter a number :"))
# if (num<0) :
#     print("The number is negative")
# elif (num==0) :
#     print("The number is zero")
# else :
#     print("The number is positive")

num=float(input("Enter a number :"))
if (num<0):
    print("The number is negative")
elif(num>0):
    if(num<=10):
        print("The number is between 1-10")
    elif(num>10 and num<=20) :
        print("The number is between 11-20")
    else: 
        print("The number is gretter than 20")
else :
    print ("The number is zero")
print("What do you want to do ?")
print("Type A for Additon")
print("Type S for Subtraction")
print("Type M for Multiplication")
print("Type D for Division")
print("Type AREA for Area of a Circle")

operation = input("Type now: ").upper()

if operation != "AREA":
   x = float(input("Input X: "))
   y = float(input("Input Y: "))
else:
     z = float(input("Input the radius: "))
     area = (3.14*z*z)
     print (area)


if operation == "A":
    print(x+y)
elif operation == "S":
    print(x-y)
elif operation == "M":
    print(x*y)
elif operation == "D":
    print(x/y)

print("What do you want ?")
print("Type A for Additon")
print("Type S for Subtraction")
print("Type M for Multiplication")
print("Type D for Division")
print("Type AREA for Area of a Circle")

x = int(input("Input X: "))
y = int(input("Input Y: "))


arithmetic = input("Type now: ").upper()
if arithmetic == "A":
    print(x+y)
if arithmetic == "S":
    print(x-y)
if arithmetic == "M":
    print(x*y)
if arithmetic == "D":
    print(x/y)
if arithmetic == "AREA":
    z = float(input("Input the radius: "))
    area = (3.14*z*z)
    print (area)

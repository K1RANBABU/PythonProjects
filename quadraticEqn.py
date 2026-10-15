import math

a=int(input("enter a: "))
b=int(input("enter b: "))
c=int(input("enter c: "))
d=b**2-4*a*c
if d==0:
    root=-b/(2*a)
    print("root: ",root)
elif d>0:
    root1=-b+math.sqrt(d)/(2*a)
    root2=-b-math.sqrt(d)/(2*a)
    print("root1: ",root1)
    print("root2: ",root2)
else:
    print("No root")
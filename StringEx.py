a=input("enter a string: ")
print("Entered string is ",a)
print("After exchanging")
if len(a)>1:
    ex=a[-1]+a[1:-1]+a[0]
else:
    ex=a
print(ex)
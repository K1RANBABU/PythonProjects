list1=["red","green","blue","yellow","orange"]
print("first color="+list1[0]+ " \nsecond color= "+list1[-1])
list2=["red","green","blue"]
d=[color for color in list1 if color not in list2]
print("color difference: ",d)
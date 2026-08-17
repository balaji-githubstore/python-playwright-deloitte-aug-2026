print("hello world")

a=10
b=10.2 

c=a+b

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

my_name="bala"



print(my_name)
print(type(my_name))

print(my_name[1])

print(len(my_name))

print(my_name.upper())

colors=["red","green","yellow","black"]

print(colors)
print(type(colors))
print(len(colors))
print(colors[0])

# add an item - blue 
colors.append("blue")

print(colors)

# insert pink at index 0 
colors.insert(0,"pink")
print(colors)

colors.remove("yellow")
print(colors)

# colors.remove(colors[2])
# fixed set of collection then go tuple - immutable (can't add or remove items after creation, faster)
signal=("red","yellow","green")

print(signal)
print(type(signal))
print(len(signal))
print(signal[0])

res=()

print(type(res))

# print(signal.count("red"))
print(len(signal))

check=True

print(check)
print(type(check))

emp_record={
    "id":101,
    "name":"bala",
    "role":"trainer",
    "mobile":[1233424,45454543534]
}

print(emp_record)
print(type(emp_record))

print(emp_record["id"])
print(emp_record["name"])
print(emp_record["mobile"][1])

# [{},{}]
# # create dict to store Samsung, android, 11 

# {
# deviceName
# platformName
# platformVersion 
# }

appium_dic={
    "deviceName" : "Samsung",
    "platformName":"android",
    "platformVersion":11,
    "app":["zomato","swiggy"]
}

output=len(signal)
print(output)

print(len(signal))


print(5>20)



for i in range(1,21):
    print(i)


colors=["red","green","yellow","black","blue"]

for i in range(0,len(colors)):
    print(colors[i])

for color in colors:
    print(color)
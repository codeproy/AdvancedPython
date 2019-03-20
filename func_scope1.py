def add():
    global z
    z = x + y

def add1():
    z = x + y



z = 0
x = 2
y = 3

print('befor ',z)
#add()
#print('add ',z)

add1()
print('add1',z)


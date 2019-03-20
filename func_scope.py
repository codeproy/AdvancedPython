def z():
    print('Inside Z',s)

def f():
    #global s
    #print('Inside f before assign ',s)
    s = "Local"
    z()
    print('Inside f after assign ',s)


s = " I am global "

f()
print(s)

import os

def outer_func1(msg):

    out_var = 'Hello' + ' '+ msg

    def inner_func():

        print(out_var)

    return inner_func()

def outer_func2(msg):


    def inner_func(name):

        print(name + msg)

    return inner_func

if __name__ == "__main__":

    of1 = outer_func1
    #print(of1)

    of1('Partha')
    of1('Suman')

    of2 = outer_func2('hello')
    print(of2)
    of2('Partha')
    



          

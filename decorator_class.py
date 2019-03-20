import os

class decorator_class(object):

    def __init__(self,original_func):

        self.original_func = original_func


    def __call__(self,*args,** kwargs):


        print('wrapper func executed before {}'.format(self.original_func.__name__))

        return self.original_func(* args, **kwargs)

@decorator_class
def display_func():

    print('display_func_run')
    
@decorator_class
def display_name_age(name,age):

    print('my name is {} and age is {}'.format(name,age))
    

if __name__ == "__main__":

#    disp = decorator_func(display_func)
#    disp()

    display_func()

    display_name_age('John',25)

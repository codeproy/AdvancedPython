import os
# Example of function as decorators..* args & ** kwarags were passed to pass
# any number of arguments and keyword arguments


def decorator_func(original_func):

    
    def wrapper_func(* args, **kwargs):

        print('wrapper func executed before {}'.format(original_func.__name__))

        return original_func(* args, **kwargs)

    return wrapper_func

@decorator_func
def display_func():

    print('display_func_run')
    
@decorator_func
def display_name_age(name,age):

    print('my name is {} and age is {}'.format(name,age))
    

if __name__ == "__main__":

#    disp = decorator_func(display_func)
#    disp()

    display_func()

    display_name_age('John',25)

    


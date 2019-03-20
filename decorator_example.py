import os
import time

from functools import wraps

def my_logger(original_func):

    import logging

    logging.basicConfig(filename= '{}.log'.format(original_func.__name__),level=logging.INFO)


    @wraps(original_func)
    def wrapper_func(*args, **kwargs):

        logging.info('Ran with args {} and kwrags {}'.format(args,kwargs))

        return original_func(*args , **kwargs)

    return wrapper_func

def my_timer(original_func):

    import time

    @wraps(original_func)
    def wrapper_func(*args, **kwargs):

        t1 = time.time()
        result = original_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} function took {} seconds'.format(original_func.__name__,t2))
        return result

    return wrapper_func


        

@my_timer
def display():

    print('this is a display function')

    
@my_logger
def display_age_name(name,age):

    time.sleep(1)

    print('My name is {} and age is {}'.format(name,age))


if __name__ == "__main__":

    display()

    display_age_name('roy',22)


    

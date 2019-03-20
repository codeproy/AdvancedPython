import os


# first class functions are functions that can accept and return fucnctiions as arguments

def cube_num(x):

    return x * x * x

def square_num(x):

    return x * x


def apply_func(func,items):

    return_list = []

    for i in items:
        return_list.append(func(i))

    return return_list


if __name__ == "__main__":

    num_list = [2,7,5,-1]

    print(apply_func(cube_num,num_list))

    print( '-' * 21)
    print(apply_func(square_num,num_list))

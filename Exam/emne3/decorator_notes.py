#Decorator

def add(x,y):
    return x+y

#print(add(1,2))


#Hjemmelavet decorator
#*args og **kwargs gør at metoden kan tage imod alle inputs basicly

def yourResult(func):
    def inner(*args, **kwargs):
        print("The result of the calculation is:")
        return func(*args, **kwargs)
    return inner

#result = yourResult(add)
#print(result(1,2))

#Decorator mere pythonic
@yourResult
def add2(x,y):
    return x+y

@yourResult
def subtract(x,y):
    return x-y

# result2 = add2(2,3)
# print(result2)
# result3 = subtract(3,2)
# print(result3)



# class decorator_class(object):
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, *args, **kwargs):
#         print('call method executed this before {}'.format(self.func.__name__))
#         return self.func(*args, **kwargs)
#
# @decorator_class
# def add3(x, y):
#     print('add metode i dec class kørte med ({}, {})'.format(x, y))
#
# add3(5, 6)
# print(add(5,6))




#Mere brugbar i almen praktis decorator
#Logging af metode brug, og tidsmåling af metoder

def myLog(func):
    import logging
    logging.basicConfig(filename='{}.log'.format(func.__name__), level=logging.INFO)

    def wrapper(*args, **kwargs):
        logging.info(
            'Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return func(*args, **kwargs)
    return wrapper

@myLog
def loggedAdd(x,y):
    return x + y

#loggedAdd(5, 10)
#loggedAdd(2,3)

def myTimer(func):
    import time

    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in : {} sec'.format(func.__name__,t2))
        return result
    return wrapper

@myTimer
def timedLoop():
    sum = 0
    for i in range(1000):
        sum += 1
    return sum
timedLoop()








#1
def sum(x):
    if x == 1:
        return 1
    elif x > 1: 
        return x + sum(x - 1)

#2
def fib(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fib(x - 1) + fib(x - 2)

from tkinter import Y


def firstFunction(fx):
    y = 1/2 * fx + 29
    return y

def secondFunction(x):
    y = (3.44/2) * x + 1350
    print('first function is ' + str(y))
    return firstFunction(y)

print(secondFunction(100))
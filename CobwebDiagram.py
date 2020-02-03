import numpy as np  
import matplotlib.pyplot as plt  

def cobweb(iterations, nextX):
    count = 0
    nextY = 0
    x = [nextX]
    y = [nextY]
    while count < iterations:
        nextY = formula2(nextX)
        x.append(nextX)
        y.append(nextY)
        nextX = formula1(nextY)
        x.append(nextX)
        y.append(nextY)
        count+=1
    plt.plot(x,y)

def graph(formula, min, max):  
    n = min
    x = []
    y = []
    while n <= max:
        x.append(n)
        y.append(formula(n))
        n+=.01
    plt.plot(x,y) 

def formula1(x):
    return x

fx = input("enter function --> ")
formula2 = lambda x: eval(fx)

graph(formula1, 0, 1)

graph(formula2, 0, 1)

iterations = int(input("how many iterations --> "))
seed = float(input("what is your seed value --> "))

cobweb(iterations, seed)

plt.show() 

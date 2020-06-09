#!/usr/bin/python

import matplotlib.pyplot as plt
import random 

fig = plt.figure()
ax = plt.axes()

prediction = lambda x, theta: sum([theta[i] * x**i for i in range(len(theta))])
cost = lambda theta, x, y : sum([((y[i] - prediction(x[i], theta)) ** 2) for i in range(len(x))]) / len(x)

points = 20
degree = 2
alpha = 0.005 / (10**(degree * 2))

theta = [random.random() for i in range(degree + 1)]
X = range(points)
Y = [random.randrange(100) for x in range(points)]
prevCost = cost(theta, X, Y)
gradient = prevCost

while abs(gradient) > 1:
    for i in range(len(X)):
        for j in range(len(theta)):
            theta[j] -= alpha * sum([-2 * X[i]**j * (Y[i] - prediction(X[i], theta)) for i in range(len(X))]) / len(X)

    print(f"Cost: {prevCost} Weights: {theta}")

    gradient = (cost(theta, X, Y) - prevCost)
    prevCost = cost(theta, X, Y)

    plt.cla()
    ax.scatter(X, Y)
    ax.plot([prediction(x, theta) for x in range(points + 1)])
    ax.set_xlim([0, points])
    ax.set_ylim([0, 100])
    plt.pause(0.005)

plt.scatter(X, Y)
plt.plot([prediction(x, theta) for x in range(points + 1)])
ax.set_xlim([0, points])
ax.set_ylim([0, 100])
print(f"Finished gradient descent with degree {degree} and {points} points")
plt.show()


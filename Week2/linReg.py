#!/usr/bin/python

import matplotlib.pyplot as plt
import random 

prediction = lambda x, theta: sum([theta[i] * x**i for i in range(len(theta))])
cost = lambda theta, x, y : sum([((y[i] - prediction(x[i], theta)) ** 2) for i in range(len(x))]) / len(x)

degree = 1

X = []
Y = []
for line in open("data.train", "r"):
    values = line.split(",")
    X.append(float(values[0]))
    Y.append(float(values[1]))

theta = [random.random() for i in range(degree + 1)]
prevCost = cost(theta, X, Y)
alpha = .000000005
gradient = prevCost
loopCount = 0

while abs(gradient) > 1:
    for i in range(len(X)):
        for j in range(len(theta)):
            theta[j] -= alpha * sum([-2 * X[i]**j * (Y[i] - prediction(X[i], theta)) for i in range(len(X))]) / len(X)

    print(f"Cost: {cost(theta, X, Y)} Weights: {theta}")

    gradient = (cost(theta, X, Y) - prevCost)
    prevCost = cost(theta, X, Y)

print(f"a is approximately {theta[1]} and b is approximately {theta[0]}")

fig = plt.figure()
ax = plt.axes()
plt.scatter(X, Y)
plt.plot([prediction(x, theta) for x in range(1000)])
ax.set_xlim([0, 200])
ax.set_ylim([0, 1000])
plt.show()


#!/usr/bin/python

import numpy as np
import math
import pprint

data = np.loadtxt("expanded.Z", delimiter=",", dtype=str)
data = data.T

Y, X = np.split(data, [1])
Y = Y[0]

prob = lambda X, x : np.count_nonzero(X == x) / X.shape[0]
entropy = lambda Y : -1 * np.sum([prob(Y, y) * math.log(prob(Y, y)) for y in np.unique(Y) if y != '?'])
entropyConditional = lambda X, Y : np.sum([prob(Y, y) * entropy(X[np.where(Y == y)]) for y in np.unique(Y) if y != '?'])
informationGain = lambda y, x : entropy(y) - entropyConditional(y, x)

def genTree(x, y):
    if np.unique(y).shape[0] > 1:
        infGain = [informationGain(y, attr) for attr in x]
        bestAttr = np.where(infGain == np.max(infGain))[0]
        return {key:genTree(np.delete(x, bestAttr, 0)[:, x[bestAttr][0] == key], y[x[bestAttr][0] == key]) for key in np.unique(x[bestAttr])}
    else:
        if np.unique(y).shape[0] == 1:
            return y[:][0]
        else:
            return ""

pprint.pprint(genTree(X, Y))

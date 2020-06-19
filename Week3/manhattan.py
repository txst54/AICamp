#!/usr/bin/python3
import numpy as np
import pprint

puzzle = np.array([
    [17, 11, 18, 19, 23],
    [15,  9,  6, 12, 24],
    [8,   1,  7, 14,  3],
    [16, 22, 20, 13,  5],
    [21,  4,  2, 10,  0]
    ])

def calcManhattan(puzzle):
    ideal = np.reshape(np.arange(1, np.prod(puzzle.shape) + 1), puzzle.shape)
    ideal[ideal.shape[0] - 1, ideal.shape[1] - 1] = 0
    actual = [np.where(puzzle == el) for el in ideal.flatten()]
    optimal = [np.where(ideal == el) for el in ideal.flatten()]
    return np.sum(np.abs(np.subtract(actual, optimal)))

pprint.pprint(calcManhattan(puzzle))

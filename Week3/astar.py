#!/usr/bin/python3
import numpy as np
import copy
import os

puzzle = np.array([
    [17, 11, 18, 19, 23],
    [15,  9,  6, 12, 24],
    [8,   1,  7, 14,  3],
    [16, 22, 20, 13,  5],
    [21,  4,  2, 10,  0]
    ])

ideal = np.reshape(np.arange(1, np.prod(puzzle.shape) + 1), puzzle.shape)
ideal[ideal.shape[0] - 1, ideal.shape[1] - 1] = 0

class Node:
    def __init__(self, h, g, state, parent=None):
        self.h = h
        self.g = g
        self.f = g + h
        self.state = state
        self.neighbours = self.findNeighbours()
        self.parent = parent

    def findNeighbours(self):
        currentPos = np.where(self.state == 0)
        offsets = np.indices((3,3)).reshape(2, -1).T[1::2] - 1
        offsets[:, 0] += currentPos[0]
        offsets[:, 1] += currentPos[1]
        offsets = offsets[np.all((offsets < np.array(self.state.shape)) & (offsets >= 0), axis=1)].T
        return self.state[offsets[0], offsets[1]]

    def __le__(self, other):
        return self.f <= other.f

def manhattan(initial, solution):
    actual = [np.where(initial == el) for el in solution.flatten() if el != 0]
    optimal = [np.where(solution == el) for el in solution.flatten() if el != 0]
    return np.sum(np.abs(np.subtract(actual, optimal)))

def misplaced(initial, solution):
    return np.sum((initial == solution))

def astar(heuristic, initial, solution):
    startNode = Node(heuristic(initial, solution), 0, initial)
    frontier = np.array([startNode])
    visited = np.array([])

    while frontier.size > 0:
        current = np.amin(frontier)
        frontier = np.delete(frontier, np.where(frontier == current))
        print(f"Frontier Size: {frontier.size}")
        print(f"Visited Size: {visited.size}")
        print(f"Current Score: {current.f}")
        print(f"Current Depth: {current.g}")
        print(f"Current Heuristic: {current.h}")
        print("Current Position:")
        print(current.state)
        print()
        print("Possible moves")
        for neighbour in current.neighbours:
            state = copy.deepcopy(current.state)
            coords = [np.where(state == neighbour), np.where(state == 0)]
            state[coords[0]], state[coords[1]] = state[coords[1]], state[coords[0]]

            if np.array_equal(current.state, solution):
                path = []
                while current != None:
                    path.append(current)
                    current = current.parent
                return path.reverse()
            
            if True in [(state == el.state).all() and heuristic(state, solution) < el.h  for el in visited]:
                print("Already inside visited")
            else:
                child = Node(heuristic(state, solution), current.g + 1, state, current)
                frontier = np.append(frontier, copy.deepcopy(child))
                print(state)
            print()

        visited = np.append(visited, copy.deepcopy(current))
        os.system("clear")

print(astar(manhattan, puzzle, ideal))

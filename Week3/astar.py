#!/usr/bin/python3
import numpy as np
import copy
import os
import time

puzzle = np.array([
    [1, 3, 14, 4],
    [15, 2, 8, 11],
    [6, 7, 5, 12],
    [9, 13, 10, 0],
    ])

ideal = np.reshape(np.arange(1, np.prod(puzzle.shape) + 1), puzzle.shape)
ideal[ideal.shape[0] - 1, ideal.shape[1] - 1] = 0

class Node:
    def __init__(self, h, g, state, parent=None, move=None):
        self.h = h
        self.g = g
        self.f = g + h
        self.state = state
        self.neighbours = self.findNeighbours()
        self.parent = parent
        self.move = move

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
    return np.sum((initial != solution))

def astar(heuristic, initial, solution):
    startNode = Node(heuristic(copy.deepcopy(initial), copy.deepcopy(solution)), 0, copy.deepcopy(initial))
    frontier = np.array([startNode])
    visited = np.array([Node(0, 0, solution)])

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
        print("Possible Moves:")
        for neighbour in current.neighbours:
            state = copy.deepcopy(current.state)
            coords = [np.where(state == neighbour), np.where(state == 0)]
            state[coords[0]], state[coords[1]] = state[coords[1]], state[coords[0]]

            if state.tobytes() == solution.tobytes():
                print("Found solution")
                current = Node(heuristic(state, solution), current.g + 1, state, current, np.where(neighbour == current.neighbours))
                path = []
                nodes = []
                while current.parent != None:
                    currentPos = np.where(current.state == 0)
                    prevPos = np.where(current.parent.state == 0)
                    move = tuple(np.subtract(currentPos, prevPos))
                    if move[0] == -1:
                        path.append("up")
                    elif move[0] == 1:
                        path.append("down")
                    elif move[1] == -1:
                        path.append("left")
                    elif move[1] == 1:
                        path.append("right")
                    nodes.append(current)
                    current = current.parent
                os.system("clear")
                for node in nodes[::-1]:
                    print("Optimal path looks like:")
                    print(node.state)
                    time.sleep(1)
                    os.system("clear")
                return path[::-1]
            
            if True in [state.tobytes() == el.state.tobytes() and current.g < el.g for el in visited]:
                print("Already inside visited")
            elif True in [state.tobytes() == el.state.tobytes() and current.g < el.g for el in frontier]:
                print("Already inside frontier")
            else:
                child = Node(heuristic(state, solution), current.g + 1, state, current, np.where(neighbour == current.neighbours))
                frontier = np.insert(frontier, 0, copy.deepcopy(child), 0)
                print(state)
            print()

        visited = np.insert(visited, 0, copy.deepcopy(current), 0)
        os.system("clear")

print(astar(manhattan, puzzle, ideal))

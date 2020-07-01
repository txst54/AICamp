#Reference Change in X occurs in brackets >, Change in Y occurs between brackets ^
#  Y
#X [0,0,0]
#  [0,0,0]
#  [0,0,0]
import copy
Puzzle = [[17, 11, 18, 19, 23], [15, 9, 6, 12, 24], [8, 1, 7, 14, 3], [16, 22, 20, 13, 5], [21, 4, 2, 10, 0]] #Current Puzzle State
idealPuzzle = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 0]] #Puzzle State when Solved
#Map = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 0] #Map of all of the componets of the puzzle
#Puzzle = [[1, 3, 14, 4], [15, 2, 8, 11], [6, 7, 5, 12], [9, 13, 10, 0]] #Test Puzzle 4 x 4
#idealPuzzle = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]
class Node():
  def __init__(self, parent = None, position = []):
    self.parent = parent
    self.position = position

    self.g = 0
    self.h = 0
    self.f = 0
  def __eq__(self, other):
    return self.position == other.position
def printList(Input, msg):
  print(msg)
  for i in Input:
    print(i)
printList(Puzzle, "Original Puzzle")
def calcManhattan(Puzzle, IdealPuzzle, Map): #ActualX = X Ideal X = X' ActualY = Y Ideal Y = Y'; |X-X'| + |Y-Y'|
  IdealPos = []
  RealPos = []
  Difference = []
  for k in Map: 
    for j in range(len(Puzzle)):
      for i in range(len(Puzzle[j])):
        if Puzzle[j][i] == k:
          RealPos = [i, j]
        if IdealPuzzle[j][i] == k:
          IdealPos = [i, j]
    Difference.append(abs(RealPos[0]-IdealPos[0])+abs(RealPos[1]-IdealPos[1]))
  return sum(Difference)
def findLocation(Input): #Finds the location of the blank space
  for j in range(len(Input)):
      for i in range(len(Input[j])):
        if Input[j][i] == 0:
          Out = [j, i] #(x, y)
  return Out
def findPossibleMoves(Puzzle): #Finds all possible moves
  out = []
  Location = findLocation(Puzzle)
  if Location[0] != 0:
    out.append([-1, 0])
  if Location[0] != (len(Puzzle)-1):
    out.append([1, 0])
  if Location[1] != 0:
    out.append([0, -1])
  if Location[1] != (len(Puzzle)-1):
    out.append([0, 1])
  return out
def Swap(Input, xpos1, xpos2, ypos1, ypos2): #swap (x1, y1) and (x2, y2)
  Input[xpos1][ypos1], Input[xpos2][ypos2] = Input[xpos2][ypos2], Input[xpos1][ypos1] 
  return Input
def createNodes(Location, PossibleMoves, Puzzle):
  out = []
  tempPuzzle = copy.deepcopy(Puzzle)
  for i in range(len(PossibleMoves)):
    if PossibleMoves[i] != 0:
      if i < 2:
        swapResult = Swap(tempPuzzle, Location[0], Location[0] + PossibleMoves[i], Location[1], Location[1])
        out.append(swapResult)
        tempPuzzle = copy.deepcopy(Puzzle)
      if i >1:
        swapResult = Swap(tempPuzzle, Location[0], Location[0], Location[1], Location[1] + PossibleMoves[i])
        out.append(swapResult)
        tempPuzzle = copy.deepcopy(Puzzle)
  return out
def aStar(Puzzle, idealPuzzle, Map):
  startNode = Node(parent = None, position = Puzzle)
  endNode = Node(parent = None, position = idealPuzzle)
  startNode.f = startNode.g = startNode.h = 0
  endNode.f = endNode.g = endNode.h = 0

  frontierQueue = [] #Queue that contains the children of the current node aka Open List
  visitedNodes = [] #Queue that contains all explored branches
  
  frontierQueue.append(startNode)


  while len(frontierQueue) > 0: #Loop until end of tree
    currentNode = frontierQueue[0]
    currentIndex = 0
    for index, item in enumerate(frontierQueue): #Searches if there is a better cost in the frontierQueue that it can use
      if item.f < currentNode.f:
        currentNode = item
        currentIndex = index

    frontierQueue.pop(currentIndex)
    visitedNodes.append(currentNode)

    if calcManhattan(currentNode.position, idealPuzzle, Map) == 0: #if goal is reached return path
      path = []
      current = currentNode
      while current is not None: #finds path by going to the setting current to parent node and adding it to path until current is a None type
        path.append(current.position)
        current = current.parent
      return path[::-1]

    children = [] #generate children or succesors of currentNode
    Location = findLocation(currentNode.position)
    PossibleMoves = findPossibleMoves(currentNode.position)
    for i in range(len(PossibleMoves)): #Loop that generates the children
      tempPuzzle = copy.deepcopy(currentNode.position)
      swapResult = Swap(tempPuzzle, Location[0], Location[0] + PossibleMoves[i][0], Location[1], Location[1] + PossibleMoves[i][1])
      newNode = Node(currentNode, swapResult)
      children.append(newNode)
    #print(len(children))
    for child in children:
      if len([visitedChild for visitedChild in visitedNodes if visitedChild == child]) > 0:
        continue

      child.g = currentNode.g + 1 # Calculates g, h, and f
      child.h = calcManhattan(child.position, endNode.position, Map)
      child.f = child.g + child.h

      if len([frontierChild for frontierChild in frontierQueue if frontierChild == child and child.g > frontierChild.g]) > 0:
        continue

      frontierQueue.append(child)
Map = [1, 2, 3, 4, 5, 6, 11, 16, 21] #Change the Map to which tiles you want Astar to solve
path = aStar(Puzzle, idealPuzzle, Map)
for i in path:
  printList(i, "")
Map = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 16, 17, 21, 22]
path2 = aStar(path[-1], idealPuzzle, Map)
for i in path2:
  printList(i, "")
Map = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 0]
path3 = aStar(path2[-1], idealPuzzle, Map)
for i in path3:
  printList(i, "")

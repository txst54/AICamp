Puzzle = [[17, 11, 18, 19, 23], [15, 9, 6, 12, 24], [8, 1, 7, 14, 3], [16, 22, 20, 13, 5], [21, 4, 2, 10, 0]] #Current Puzzle State
idealPuzzle = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 0]] #Puzzle State when Solved
Map = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 0] #Map of all of the componets of the puzzle
for i in Puzzle:
  print(i)
def calcManhattan(Puzzle, IdealPuzzle): #ActualX = X Ideal X = X' ActualY = Y Ideal Y = Y'; |X-X'| + |Y-Y'|
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
Manhattan = calcManhattan(Puzzle, idealPuzzle)

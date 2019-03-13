from queue import *
from collections import deque
import time


def validate_position(position):
    global solutionsAmount

    for i in range(n):
        if position[i] == -1:
            return

    for i in range(n):
        for j in range(i + 1, n):
            if position[i] == position[j]:
                return

    for i in range(n):
        for j in range(n):
            if i != j:
                distance = (position[j] - position[i]) / (j - i)
                if distance == 1 or distance == -1:
                    return

    solutions.append(position.copy())
    solutionsAmount += 1


def create_QueueBFS(start, n):

    nodeQueue = deque([start])
    currentRow = 0
    currentPower = n
    flag = 0

    while nodeQueue:
        if currentRow == n:
            flag = 1
        currentNode = nodeQueue.popleft()
        validate_position(currentNode)
        nextRow = currentNode.copy()

        if flag == 0:
            for i in range(n):
                nextRow[currentRow] = i
                nodeQueue.append(nextRow.copy())
                currentPower -= 1
            if currentPower == 0:
                currentRow += 1
                currentPower = n ** (currentRow + 1)


def create_QueueDFS(start, n):

    nodeList = [start]
    currentRow = 0

    while nodeList:
        currentNode = nodeList.pop()
        validate_position(currentNode)

        for i in range(n):
            currentNode[i] = currentRow
            nodeList.insert(0, currentNode.copy())

        currentRow += 1


# TODO: finish print, not vital, and impliment DFS
def printSolutions():

    pass


n = int(input("Enter n: "))
alg = str(input("Enter the algorithm to be used BFS or DFS (B/D): "))


if n > 8:
    print("n is too high to be calculated using BFS")
    exit()

if n == 1:
    print("Cannot provide an answer for N=1")

startState = [-1] * n
solutions = []
solutionsAmount = 0

start = time.time()

if alg == 'B':
    create_QueueBFS(startState, n)
else:
    create_QueueDFS(startState, n)
end = time.time()

printSolutions()

executeTime = end - start
print("finished in: " + str(executeTime) + " seconds")
print("")
print("found " + str(solutionsAmount) + " Solutions")
print(solutions)


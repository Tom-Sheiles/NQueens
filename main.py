from queue import *
from collections import deque
import time


# TODO: finish this function and then add a print function to print the results
def validate_position(position):

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


def create_Queue(start, n):

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
    print("done")


n = int(input("Enter n: "))

if n > 8:
    print("n is too high to be calculated using BFS")
    exit()

startState = [0] * n
solutions = []

start = time.time()
create_Queue(startState, n)
end = time.time()

executeTime = end - start
print("finished in: " + str(executeTime) + " seconds")
print("")
print(solutions)


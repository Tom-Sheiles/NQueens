from queue import *
from collections import deque
import time

# TODO: finish this function and then add a print function to print the results
def validate_position(position):

    for i in range(n):
        for j in range(1, n):
            if position[i] == position[j]:
                return
            else:
                solutions.append(position)



def create_Queue(start, n, startTime):

    nodeQueue = deque([start])
    currentRow = 0
    currentPower = n

    while nodeQueue:
        if currentRow == n:
            break
        currentNode = nodeQueue.popleft()
        validate_position(currentNode)
        nextRow = currentNode.copy()

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

startState = [-1] * n
solutions = []

start = time.time()
create_Queue(startState, n, start)
end = time.time()

executeTime = end - start
print("finished in: " + str(executeTime) + " seconds")
print("")
print(solutions)


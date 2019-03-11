from queue import *
from collections import deque
import time

def create_Queue(start, n, startTime):

    nodeQueue = deque([start])
    currentRow = 0
    currentPower = n

    while nodeQueue:
        if currentRow == n:
            break
        currentNode = nodeQueue.popleft()
        # check if node is goal state
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

start = time.time()
create_Queue(startState, n, start)
end = time.time()

executeTime = end - start
print("finished in: " + str(executeTime) + " seconds")


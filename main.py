from collections import deque
import time

# function used to verify if a passed in solution is a solution to the problem
def validate_position(position):
    global solutionsAmount

    # if any entrant has an empty row, it cannot be a solution
    for i in range(n):
        if position[i] == -1:
            return

    # if any queen on the board has the same value, and therefor the same column as another, it cannot be a solution
    for i in range(n):
        for j in range(i + 1, n):
            if position[i] == position[j]:
                return

    # calculate the gradient between all the queens on the board, if the gradient is 1 or -1, the two queens share
    # a diagonal and can take one another
    for i in range(n):
        for j in range(n):
            if i != j:
                distance = (position[j] - position[i]) / (j - i)
                if distance == 1 or distance == -1:
                    return

    # if all these conditions are false, a solution has been found and should be added to the list of solutions
    solutions.append(position.copy())
    print(position)
    solutionsAmount += 1


# Function responsible for both the creation and traversal of the BFS graph
def create_QueueBFS(start, n):

    # the queue used to explore the graph, beginning with the initial node
    nodeQueue = deque([start])
    currentRow = 0
    currentPower = n
    flag = 0

    # while the queue contains nodes and their children to explore, continue
    while nodeQueue:
        if currentRow == n:
            flag = 1

        # pop the current next node from the queue and verify if it is a goal state
        currentNode = nodeQueue.popleft()
        validate_position(currentNode)
        nextRow = currentNode.copy()

        if flag == 0:
            # for all possible children of the currently popped node, add them to the queue
            for i in range(n):
                nextRow[currentRow] = i
                nodeQueue.append(nextRow.copy())
                currentPower -= 1
            if currentPower == 0:
                currentRow += 1
                currentPower = n ** (currentRow + 1)


# Function responsible for the creation and traversal of the DFS graph
def create_QueueDFS(start, n):

    nodeList = [start]
    currentRow = 0
    flag = 0

    # while the stack contains nodes and their children to explore, continue
    while nodeList:

        if currentRow == n:
            flag = 1

        if flag == 0:

            # pop the current node from the top of the stack and verify if it is a goal state
            currentNode = nodeList.pop(0)
            validate_position(currentNode)

            # for every possible child of the pop node, add them to the beginning of the stack.
            # the loop begins at the last node sequentially as the nodes at the beginning
            # of the loop should be popped first
            for i in range(n - 1, -1, -1):
                currentNode[currentRow] = i
                nodeList.insert(0, currentNode.copy())

            currentRow += 1
        else:
            # once the algorithm has reached the leaf level, no more children need to be added the stack
            for i in range(n):
                currentNode = nodeList.pop(0)
                validate_position(currentNode)
            flag = 0
            currentRow = 0
            # this loop is used to return to previous branches, for every nonempty element on the board increase the
            # board, add another row that must be calculated
            for i in range(n):
                if nodeList and nodeList[0][i] != -1:
                    currentRow += 1


# User inputs to determine board size and algorithm type
n = int(input("Enter n: "))
alg = str(input("Enter the algorithm to be used BFS or DFS (B/D): "))


if n > 8 and alg == 'B':
    print("n is too high to be calculated using BFS")
    exit()

if n == 1:
    print("Cannot provide an answer for N=1")
    exit()

# initialise a list that contains the start position of the board, where -1 represents an empty row
# The board is visualized by a standard list where the row of the piece is shown by the location in the list and
# the column of the list is shown by the value, this is done to save memory over a 2D array
startState = [-1] * n
solutions = []
solutionsAmount = 0

start = time.time()

if alg == 'B':
    create_QueueBFS(startState, n)
else:
    create_QueueDFS(startState, n)
end = time.time()

executeTime = end - start
print("finished in: " + str(executeTime) + " seconds")
print("")
print("found " + str(solutionsAmount) + " Solutions")
print(solutions)

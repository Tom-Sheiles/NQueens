import time
import random


def costCalculation(position):

    heuristic = 0

    for i in range(n):
        if position[i] == -1:
            return

    for i in range(n):
        for j in range(i + 1, n):
            if position[i] == position[j]:
                heuristic += 1
            distance = (position[j] - position[i]) / (j - i)
            if distance == 1 or distance == -1:
                heuristic += 1

    return heuristic


def hill_climb(position):

    possibleMoves = []
    move_costs = []
    permutations = []

    for i in range(n):
        positionTemp = position.copy()

        for j in range(n):
            positionTemp[i] = j
            permutations.append(positionTemp.copy())

    for i in permutations:
        if i not in possibleMoves:
            possibleMoves.append(i)

    permutations.clear()

    for i in range(len(possibleMoves)):
        cost = costCalculation(possibleMoves[i])
        move_costs.append(cost)

    cost = move_costs[0]
    for i in range(len(possibleMoves)):
        if move_costs[i] < cost:
            cost = move_costs[i]

    solutions = []
    for i in range(len(possibleMoves)):
        if move_costs[i] == cost:
            solutions.append(possibleMoves[i].copy())

    chosen_value = random.randint(0, len(solutions) - 1)
    return solutions[chosen_value]


def solve(startState, n):

    h = costCalculation(startState)
    next_position = startState

    while h > 0:
        next_position = hill_climb(next_position)
        h = costCalculation(next_position)
    print(next_position)

n = int(input("Enter n: "))
alg = input("Enter algorithm to be used Hill climbing or annealing (H/A): ")

startState = [0] * n
solutions = []

start = time.time()

solve(startState, n)


end = time.time()
executeTime = end - start
print("Found solution in " + str(executeTime) + " Seconds")

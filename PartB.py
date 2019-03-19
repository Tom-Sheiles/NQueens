import time
import random
import math
import sys


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


def simulated_annealing(position, temperature, tempmin, decayrate):

    permutations = []
    possibleMoves = []
    nextCosts = []
    initialCost = costCalculation(position)

    while temperature >= tempmin:

        for i in range(n):
            positionTemp = position.copy()
            for j in range(n):
                positionTemp[i] = j
                permutations.append(positionTemp.copy())

        for i in permutations:
            if i not in possibleMoves:
                possibleMoves.append(i)

        permutations.clear()

        for i in range(len(possibleMoves) - 1):
            if possibleMoves[i] == position:
                possibleMoves.remove(possibleMoves[i])
            cost = costCalculation(possibleMoves[i])
            nextCosts.append(cost)


        for i in range(len(possibleMoves)):
            if nextCosts[i] < initialCost:
                initialCost = nextCosts[i]
                position = possibleMoves[i]
            else:
                delta = nextCosts[i] - initialCost
                probability = math.exp(-delta/temperature)
                if probability > random.randint(0, 1):
                    initialCost = nextCosts[i]
                    position = possibleMoves[i]
            if initialCost == 0:
                return position
            temperature *= decayrate
        if temperature <= tempmin:
            return position


def solve(startState, n):

    h = costCalculation(startState)
    next_position = startState

    while h > 0:
        next_position = hill_climb(next_position)
        h = costCalculation(next_position)
    print(next_position)

# TODO: work on this part
def print_result(position):

    for i in position:
        for j in range(position[i]):
            sys.stdout.write("* ")
        sys.stdout.write("Q")
        print("")



n = int(input("Enter n: "))
alg = input("Enter algorithm to be used Hill climbing or annealing (H/A): ")

initial = 1
startState = [0] * n
start = time.time()

if alg == 'H':
    print("using Hill climbing")
    solve(startState, n)
else:
    print("using Simulated Annealing")
    while initial != 0:
        startState = simulated_annealing(startState, 100, 0.01, 0.2)
        initial = costCalculation(startState)
    print(startState)

end = time.time()
executeTime = end - start
print("Found solution in " + str(executeTime) + " Seconds")
print_result(startState)

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

    k = 10000
    permutations = []
    possibleMoves = []
    initialCost = costCalculation(position)

    for current_iteration in range(k):

        for i in range(n):
            positionTemp = position.copy()
            for j in range(n):
                positionTemp[i] = j
                permutations.append(positionTemp.copy())

        for i in permutations:
            if i not in possibleMoves:
                possibleMoves.append(i)

        permutations.clear()

        next_move = possibleMoves[random.randint(0, len(possibleMoves) - 1)]
        print(next_move)
        '''for i in range(len(possibleMoves) - 1):
            if possibleMoves[i] == position:
                possibleMoves.remove(possibleMoves[i])
            cost = costCalculation(possibleMoves[i])
            nextCosts.append(cost)'''

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


def solve(startState, n, alg):

    if alg == 'H':
        h = costCalculation(startState)
        next_position = startState

        while h > 0:
            next_position = hill_climb(next_position)
            h = costCalculation(next_position)
        print(next_position)
        return next_position
    else:
        temperature = float(input("Enter starting temperature: "))
        decay_rate = float(input("Enter temperature decay rate: "))
        next_position = simulated_annealing(startState, temperature, 0, decay_rate)
        return next_position
        #TODO: finish sim anneal here


def print_result(position):

    for i in range(len(position)):
        for j in range(position[i]):
            sys.stdout.write("* ")
        sys.stdout.write("Q ")
        if position[i] == 0:
            for l in range(n - 2):
                sys.stdout.write("* ")
        for k in range(j + 1, n - 1):
            sys.stdout.write("* ")
        print("")


def initial_board(n):

    board = []
    for i in range(n):
        position = random.randint(0, n - 1)
        board.append(position)
    return board


n = int(input("Enter n: "))
alg = input("Enter algorithm to be used Hill climbing or annealing (H/A): ")

initial = 1
startState = initial_board(n)
print("Initial board: " + str(startState))
start = time.time()

if alg == 'H':
    print("using Hill climbing")
    solution = solve(startState, n, alg)
elif alg == 'A':
    print("using Simulated Annealing \n")
    solution = solve(startState, n, alg)
else:
    print("algorithm name not defined")
    exit()


    '''while initial != 0:
        startState = simulated_annealing(startState, 100, 0.01, 0.2)
        initial = costCalculation(startState)
    print(startState)'''

end = time.time()
executeTime = end - start
print("Found solution in " + str(executeTime) + " Seconds")
print_result(solution)

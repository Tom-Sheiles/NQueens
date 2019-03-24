import time
import random
import math
import sys
import numpy as np


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


def simulated_annealing(position, temperature, decayrate, k):

    permutations = []
    possibleMoves = []
    initial_heuristic = costCalculation(position)

    while temperature > 0:

        for current_iteration in range(k):
            if possibleMoves:
                possibleMoves.clear()
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

            next_heuristic = costCalculation(next_move)
            initial_cost = (1 / (initial_heuristic + 1))
            next_cost = (1 / (next_heuristic + 1))

            if initial_heuristic == 0:
                return position

            if next_cost < initial_cost:
                position = next_move
                initial_heuristic = next_heuristic
            else:
                delta = initial_heuristic - next_heuristic
                probablity = math.exp(-(delta / temperature))
                rnumb = random.uniform(0.0, 1.0)
                if probablity > rnumb and probablity < 1:
                    position = next_move
                    initial_heuristic = next_heuristic

        temperature *= decayrate
    return position


def solve(startState, n, alg):

    if alg == 'H':
        h = costCalculation(startState)
        next_position = startState

        start = time.time()
        while h > 0:
            next_position = hill_climb(next_position)
            h = costCalculation(next_position)
        print(next_position)
        end = time.time()
        print("finished in: " + str(end - start) + " seconds")
        return next_position
    else:
        temperature = float(input("Enter starting temperature (recommended 100,000): "))
        decay_rate = float(input("Enter temperature decay rate (recommended 0.8 - 0.99): "))
        k = int(input("Enter the number of iterations until the temperature decreases (rec 10,000): "))
        start = time.time()
        next_position = simulated_annealing(startState, temperature, decay_rate, k)
        end = time.time()
        print(next_position)
        print("finished in: " + str(end - start) + " seconds")
        return next_position


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


if alg == 'H':
    print("using Hill climbing")
    solution = solve(startState, n, alg)
elif alg == 'A':
    print("using Simulated Annealing \n")
    solution = solve(startState, n, alg)
else:
    print("algorithm name not defined")
    exit()

print_result(solution)

import time
import random
import math
import sys


# calculate the heuristic cost of the board
def costCalculation(position):

    heuristic = 0

    for i in range(n):
        if position[i] == -1:
            return

    # for any queen that occupies the same row, column or diagonal = add 1 to the total heuristic cost
    for i in range(n):
        for j in range(i + 1, n):
            if position[i] == position[j]:
                heuristic += 1
            distance = (position[j] - position[i]) / (j - i)
            if distance == 1 or distance == -1:
                heuristic += 1

    # return the total heuristic value of the board
    return heuristic


# the algorithm for the hill climbing solution
def hill_climb(position):

    possibleMoves = []
    move_costs = []
    permutations = []

    # generate a list of all possible moves and add them to a separate list of permutations of the board
    for i in range(n):
        positionTemp = position.copy()

        for j in range(n):
            positionTemp[i] = j
            permutations.append(positionTemp.copy())

    # remove all duplicate possible moves
    for i in permutations:
        if i not in possibleMoves:
            possibleMoves.append(i)

    permutations.clear()

    # calculate the cost for all the neighbour moves and add their cost to a list of integers. the location of the move
    # and the location of the cost map to each other
    for i in range(len(possibleMoves)):
        cost = costCalculation(possibleMoves[i])
        move_costs.append(cost)

    # find the lowest cost move in the list of possible moves
    cost = move_costs[0]
    for i in range(len(possibleMoves)):
        if move_costs[i] < cost:
            cost = move_costs[i]

    # find all solutions with this cost and randomly select one with the most optimal value
    solutions = []
    for i in range(len(possibleMoves)):
        if move_costs[i] == cost:
            solutions.append(possibleMoves[i].copy())

    chosen_value = random.randint(0, len(solutions) - 1)
    return solutions[chosen_value]


# the algorithm for the simulated annealing solution
def simulated_annealing(position, temperature, decayrate, k):

    permutations = []
    possibleMoves = []
    initial_heuristic = costCalculation(position)

    while temperature > 0:

        # for the total specified iterations
        for current_iteration in range(k):
            if possibleMoves:
                possibleMoves.clear()
            # add all possible neighbour moves to a list of moves
            for i in range(n):
                positionTemp = position.copy()
                for j in range(n):
                    positionTemp[i] = j
                    permutations.append(positionTemp.copy())

            for i in permutations:
                if i not in possibleMoves:
                    possibleMoves.append(i)

            permutations.clear()

            # randomly select a move to make from the list of available moves
            next_move = possibleMoves[random.randint(0, len(possibleMoves) - 1)]

            # calculate the cost of this move and compare it to the cost of the current
            next_heuristic = costCalculation(next_move)
            initial_cost = (1 / (initial_heuristic + 1))
            next_cost = (1 / (next_heuristic + 1))

            if initial_heuristic == 0:
                return position

            # if the chosen move is better than the previous then accept the move
            if next_cost < initial_cost:
                position = next_move
                initial_heuristic = next_heuristic
            # if the chosen move is worse than the previous then accept the move with a certain probability based on
            # the current temperature and difference in energy between the two nodes
            else:
                delta = initial_heuristic - next_heuristic
                probablity = math.exp(-(delta / temperature))
                rnumb = random.uniform(0.0, 1.0)
                if probablity > rnumb and probablity < 1:
                    position = next_move
                    initial_heuristic = next_heuristic

        # reduce the temperature and therefor the probability to accept worse moves by the decay rate
        temperature *= decayrate
    return position


# defines the running conditions of both the algorithms. takes in initial board configiration, size of the board and the
# algorithm type
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


# takes a solution and prints a representation of the board where "*" is a blank space and "Q" is a queen
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


# generates a random board of size n, returns the board as a List where the position is the vertical position and the
# value its horizontal position
def initial_board(n):

    board = []
    for i in range(n):
        position = random.randint(0, n - 1)
        board.append(position)
    return board


n = int(input("Enter n: "))
alg = input("Enter algorithm to be used Hill climbing or annealing (H/A): ")

initial = 1
# generate a random board and assign it to startState
startState = initial_board(n)
print("Initial board: " + str(startState))

# Call the solve function with the random starting board and the algorithm type entered
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

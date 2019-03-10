import time
start = time.time()

def solution():

    queen_placer(0)
    print("done")


def queen_placer(currentRow):

    queens[currentRow] = 0

    for i in range(n):
        if verify_position(queens, currentRow, i):
            queens[currentRow] == i
            queen_placer(currentRow + 1)

    finish_problem(queens)


def verify_position(queens, currentRow, yPosition):
    for i in range(currentRow):
        if queens[i] == yPosition:
            return False
    return True

def finish_problem(queens):
    print(queens)


n = int(input("Enter n size of board: "))

queens = [-1] * n
print(queens)

solution()
end = time.time()
executeTime = end - start
print(executeTime)


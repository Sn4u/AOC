import numpy as np

with open("input", "r") as f:
    file = f.read().splitlines()

bingo = list(map(int, file[0].split(",")))
boards = []
for i in range(2, len(file), 6):
    boards.append(np.array([a.split() for a in (file[i:i + 5])], dtype=int))


def one():
    def get_bingo():
        for num in bingo:
            for i, board in enumerate(boards):
                boards[i] = (np.where(num == board, -1, board))  # replace every occurance of the number with -1

            for i, board in enumerate(boards):
                if -5 in np.sum(board, axis=0) or -5 in np.sum(board, axis=1):  # checking for bingo
                    print("BINGO", i)
                    print(board)
                    return board, num

    b, num = get_bingo()
    s = np.sum(b[np.where(b >= 0)])
    print(s * num)


def two():
    def get_last_bingo(boards):
        order = []  # the order that bingos happen
        for num in bingo:
            for i, board in enumerate(boards):
                boards[i] = np.where(num == board, -1, board)

            for i, board in enumerate(boards):
                if board != "":
                    if -5 in np.sum(board, axis=0) or -5 in np.sum(board, axis=1):
                        if boards.count("") == len(boards) - 1:
                            return board, num

                        order.append(board)
                        boards[i] = ""

    board, num = get_last_bingo(boards)

    s = np.sum(board[np.where(board >= 0)])
    print(s * num)


two()

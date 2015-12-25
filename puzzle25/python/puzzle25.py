"""Day 25 Puzzle"""

# index <- 1
# R <- 1
# A <- array
# while true
#   col <- 0
#   for row from R down to 1
#     col <- col + 1
#     A[row, col] <- index
#     index <- index + 1
#   R <- R + 1

DEBUG = False

import tqdm

def log(msg):
    """Prints message if DEBUG == True."""
    if DEBUG:
        print msg


def calculate_code(previous_code):
    """Calculates next code based on previous code."""
    return (previous_code * 252533) % 33554393

def diagonals(row_to_find, col_to_find, initial_value, func):
    """Calculates codes on the diagonal."""
    index = initial_value
    max_row = 0
    result = []
    with tqdm.tqdm(None) as pbar:
        while True:
            col = 0
            for row in range(max_row, -1, -1):
                # make sure grid is big enough
                # to hold the index going in
                if len(result) <= row:
                    result.append([])
                result[row].append(index)
                log("%d, %d <- %d" % (row, col, index))

                col = col + 1
                index = func(index)

                # progress bar
                pbar.set_description("%d, %d <- %d" % (row, col, index))
                pbar.update(1)

            if len(result) >= row_to_find \
            and len(result[row_to_find - 1]) >= col_to_find:
                return result[row_to_find - 1][col_to_find - 1]

            max_row = max_row + 1

def main():
    """Main program."""
    row, col = 2947, 3029
    initial_value = 20151125
    result = diagonals(row, col, initial_value, calculate_code)
    print "%d is the code at %d, %d" % (result, row, col)

if __name__ == "__main__":
    main()

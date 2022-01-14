class QueensProblem:
    def __init__(self, num_queens) -> None:
        self.num_queens = num_queens
        self.chess_table = [[None for _ in range(num_queens)]
                            for _ in range(num_queens)]

    def solve_n_queens(self):
        if self.solve(0):
            self.print_queens()
        else:
            print('There is no solution to the problem.')

    def solve(self, col_index):
        if col_index == self.num_queens:
            return True

        for row_index in range(self.num_queens):
            if self.is_place_valid(row_index, col_index):
                self.chess_table[row_index][col_index] = 1

                if self.solve(col_index + 1):
                    return True

                self.chess_table[row_index][col_index] = 0

        return False

    def is_place_valid(self, row_index, col_index):
        for i in range(self.num_queens):
            if self.chess_table[row_index][i] == 1:
                return False

        j = col_index
        for i in range(row_index, -1, -1):
            if i < 0:
                break

            if self.chess_table[i][j] == 1:
                return False

            j = j - 1

        j = col_index
        for i in range(row_index, self.num_queens):
            if i < 0:
                break

            if self.chess_table[i][j] == 1:
                return False

            j = j - 1

        return True

    def print_queens(self):
        for i in range(self.num_queens):
            for j in range(self.num_queens):
                if self.chess_table[i][j]:
                    print(' Q ', end='')
                else:
                    print(' - ', end='')
            print('\n')


if __name__ == '__main__':
    queens = QueensProblem(4)
    queens.solve_n_queens()

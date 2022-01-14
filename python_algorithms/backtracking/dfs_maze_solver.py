from collections import deque


class MazeSolver:
    def __init__(self, matrix) -> None:
        self.matrix = matrix
        self.move_x = [1, 0, 0, -1]
        self.move_y = [0, -1, 1, 0]
        self.visited = [[False for _ in range(len(matrix))]
                        for _ in range(len(matrix))]
        self.min_distance = float('inf')

    def is_valid(self, row, col):
        if row < 0 or row >= len(self.matrix) or col < 0 or col >= len(
                self.matrix):
            return False

        if self.matrix[row][col] == 0:
            return False

        if self.visited[row][col]:
            return False

        return True

    def search(self, x, y, destination_x, destination_y):
        self.visited[x][y] = True
        queue = deque()
        queue.append((x, y, 0))

        while queue:
            (x, y, dist) = queue.popleft()

            if x == destination_x and y == destination_y:
                self.min_distance = dist
                break

            for move in range(len(self.move_x)):
                next_x = x + self.move_x[move]
                next_y = y + self.move_y[move]

                if self.is_valid(next_x, next_y):
                    self.visited[next_x][next_y] = True
                    queue.append((next_x, next_y, dist + 1))

    def show_result(self):
        if self.min_distance != float('inf'):
            print(
                f'The shortest path from source to destination: {self.min_distance}'
            )
        else:
            print('No feasible solution - the destination cannot be reached.')


if __name__ == '__main__':
    matrix1 = [[1, 1, 1, 1, 1], [0, 1, 1, 1, 1], [0, 0, 0, 0, 1],
               [1, 0, 1, 1, 1], [0, 0, 0, 1, 1]]

    maze_solver = MazeSolver(matrix1)
    maze_solver.search(0, 0, 4, 4)
    maze_solver.show_result()

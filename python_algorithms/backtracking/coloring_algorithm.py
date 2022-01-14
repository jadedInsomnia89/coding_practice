class ColoringAlgorithm:
    def __init__(self, adjacency_matrix, num_colors) -> None:
        self.n = len(adjacency_matrix)
        self.adjacency_matrix = adjacency_matrix
        self.num_colors = num_colors
        self.colors = [0 for _ in range(self.n)]

    def coloring_algorithm(self):
        if self.solve(0):
            self.show_result()

        else:
            print('There is no feasible solution.')

    def solve(self, node_index):
        if node_index == self.n:
            return True

        for color_index in range(1, self.num_colors + 1):
            if self.is_color_valid(node_index, color_index):
                self.colors[node_index] = color_index

                if self.solve(node_index + 1):
                    return True

        return False

    def is_color_valid(self, node_index, color_index):
        for i in range(self.n):
            if self.adjacency_matrix[node_index][i] == 1 and color_index == self.colors[i]:
                return False

        return True

    def show_result(self):
        for vertex, color, in zip(range(self.n), self.colors):
            print(f'Node {vertex} has color value: {color}')


if __name__ == '__main__':
    matrix = [[0, 1, 1, 1],
              [1, 0, 1, 0],
              [1, 1, 0, 1],
              [1, 0, 1, 0]]

    coloring_algorithm = ColoringAlgorithm(matrix, 3)
    coloring_algorithm.coloring_algorithm()
                
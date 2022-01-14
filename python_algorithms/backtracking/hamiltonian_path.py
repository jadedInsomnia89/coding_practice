class HamiltonianPath:
    def __init__(self, adjacency_matrix) -> None:
        self.n = len(adjacency_matrix)
        self.adjacency_matrix = adjacency_matrix
        self.path = [0]

    def run(self):
        if self.solve(1):
            self.show_hamiltonian_path()
        else:
            print('There is no solution to the problem.')

    def solve(self, position):
        if position == self.n:
            return True

        for vertex_index in range(1, self.n):
            if self.is_feasible(vertex_index, position):
                self.path.append(vertex_index)

                if self.solve(position + 1):
                    return True

                self.path.pop()

        return False

    def is_feasible(self, vertex_index, position):
        # check to see if there is an edge between the vertices
        if self.adjacency_matrix[self.path[position - 1]][vertex_index] == 0:
            return False

        # check if the given vertex has already been added to the path
        for i in range(position):
            if self.path[i] == vertex_index:
                return False

        return True

    def show_hamiltonian_path(self):
        for vertex in self.path:
            print(vertex)


if __name__ == '__main__':
    matrix = [[0, 1, 0, 0, 0, 1], [1, 0, 1, 0, 0, 0], [0, 1, 0, 0, 1, 0],
              [0, 0, 0, 0, 1, 1], [0, 0, 1, 1, 0, 1], [1, 0, 0, 1, 1, 0]]

    hamiltonian_path = HamiltonianPath(matrix)
    hamiltonian_path.run()

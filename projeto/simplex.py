# testes com algoritmos de simplex


class Simplex:
    def __init__(self, matrix):
        self.matrix = matrix
        self.colunas = len(matrix[0])
        self.linhas = len(matrix)

    def get_colunas(self):
        return self.colunas
    
    def get_linhas(self):
        return self.linhas
    
    def mostra_solucao(self, solucao):
        print("Solução: ")
        for i in range(len(solucao)):
            print("x{} = {}".format(i+1, solucao[i]))


def main():
    matrix = [
        [1, -3, -2, 0, 0, 0],
        [0, 2, 1, 1, 0, 0],
        [0, 1, 2, 0, 1, 0],
    ]
    simplex = Simplex(matrix)
    print(simplex.get_colunas())
    print(simplex.get_linhas())

if __name__ == '__main__':
    main()
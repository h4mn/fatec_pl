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

    def encontra_coluna_pivo(self):
        coluna_pivo = -1
        for i in range(self.colunas - 1):
            celula = self.matrix[0][i]
            if celula < 0:
                if coluna_pivo == -1 or celula < menor_celula:
                    coluna_pivo = i
                    menor_celula = celula
                
        print("Coluna pivo: ", coluna_pivo)
        return coluna_pivo

    def encontra_linha_pivo(self, coluna_pivo):
        linha_pivo = -1
        for i in range(1, self.linhas):
            b = self.matrix[i][-1]
            celula = self.matrix[i][coluna_pivo]
            if celula > 0:
                taxa = b / celula
                if linha_pivo == -1 or taxa < menor_taxa:
                    linha_pivo = i
                    menor_taxa = taxa
        
        print("Linha pivo: ", linha_pivo)
        return linha_pivo

    def performa_pivo(self, coluna_pivo, linha_pivo):
        pivo = self.matrix[linha_pivo][coluna_pivo]
        for i in range(self.colunas):
            self.matrix[linha_pivo][i] /= pivo

        for i in range(self.linhas):
            if i != linha_pivo:
                fator = self.matrix[i][coluna_pivo]
                for j in range(self.colunas):
                    self.matrix[i][j] -= fator * self.matrix[linha_pivo][j]

    def resolve(self):
        print("Resolvendo...")
        print("----------------------------------------------------------------------")
        while True:
            coluna_pivo = self.encontra_coluna_pivo()
            if coluna_pivo == -1:
                break
            linha_pivo = self.encontra_linha_pivo(coluna_pivo)
            if linha_pivo == -1:
                print("Solução não encontrada.")
                return
            self.performa_pivo(coluna_pivo, linha_pivo)
            self.mostra_matriz()
        
        self.mostra_matriz()
        self.mostra_solucao(self.matrix[0])
        self.mostra_resposta(self.matrix[0])

    def mostra_matriz(self):
        print("----------------------------------------------------------------------")
        print("Matriz: ")
        for i in range(self.linhas):
            for j in range(self.colunas):
                print("{:<8.2f}".format(self.matrix[i][j]), end="")
            print()
    
    def mostra_solucao(self, solucao):
        vb = [f"x{i+1} = {solucao[i]:.2f}" for i in range(len(solucao) - 1) if solucao[i] != 0]
        vnb = [f"x{i+1} = {solucao[i]:.2f}" for i in range(len(solucao)) if solucao[i] == 0]
        z = f"z = {solucao[-1]:.2f}"
        print("Solução: ")
        print("{:<15} {:<15} {:<15}".format("VB", "VNB", "Z"))
        for i in range(max(len(vb), len(vnb))):
            vb_i = vb[i] if i < len(vb) else ""
            vnb_i = vnb[i] if i < len(vnb) else ""
            print("{:<15} {:<15} {:<15}".format(vb_i, vnb_i, z if i == 0 else ""))
    
    def mostra_resposta(self, solucao):
        variaveis = [f"{solucao[i]:.2f} unidades do produto {i+1}" for i in range(len(solucao) - 1) if solucao[i] != 0]
        resposta = f"A empresa terá lucro máximo de R$ {solucao[-1]:.2f} com a produção de " + " e ".join(variaveis) + "."
        print("Resposta: ", resposta)


def main():
    matrix = [
        [1, -20, -30, -10, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 0, 0, 400],
        [0, 2, 1, -1, 0, 1, 0, 200],
        [0, 3, 2, -1, 0, 0, 1, 300],
    ]
    simplex = Simplex(matrix)
    simplex.resolve()


if __name__ == '__main__':
    main()
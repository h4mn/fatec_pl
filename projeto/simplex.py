class Simplex:
    """
    Esta classe resolve problemas de programação linear utilizando o método Simplex.
    """
    def __init__(self, matriz, variaveis, usa_big_m=False):
        """Este é o construtor da classe Simplex.

        Args:
            matriz (array): Recebe uma matriz com os valores do problema de programação linear.
            variaveis (integer): Recebe o número de variáveis do problema.
            usa_big_m (boolean, optional): Recebe um booleano que indica se o método Big M deve ser utilizado. O padrão é False.
        """
        self.matriz = matriz
        self.colunas = len(matriz[0])
        self.linhas = len(matriz)

        self.colunas_nomes = ["z"]
        self.colunas_nomes += [f"x{i+1}" for i in range(variaveis)]
        self.colunas_nomes += [f"F{i+1}" for i in range(variaveis)]
        if usa_big_m:
            self.colunas_nomes += [f"M{i+1}" for i in range(variaveis)]
        self.colunas_nomes += ["b"]
        self.vb = []
        self.mostra_matriz(f"Matriz inicial")

    def encontra_coluna_pivo(self):
        """Esta função encontra a coluna pivo, que é a coluna com o valor mais negativo na linha objetivo.

        Returns:
            integer: Retorna o índice da coluna pivo.
        """
        coluna_pivo = -1
        for i in range(self.colunas - 1):
            celula = self.matriz[0][i]
            if celula < 0:
                if coluna_pivo == -1 or celula < menor_celula:
                    coluna_pivo = i
                    menor_celula = celula
        return coluna_pivo

    def encontra_linha_pivo(self, coluna_pivo):
        """Esta função encontra a linha pivo, que é a linha com a menor razão positiva entre a coluna pivo e a coluna da solução.

        Args:
            coluna_pivo (integer): Índice da coluna pivo.

        Returns:
            integer: Retorna o índice da linha pivo.
        """
        linha_pivo = -1
        for i in range(1, self.linhas):
            b = self.matriz[i][-1]
            celula = self.matriz[i][coluna_pivo]
            if celula > 0:
                taxa = b / celula
                if linha_pivo == -1 or taxa < menor_taxa:
                    linha_pivo = i
                    menor_taxa = taxa
        return linha_pivo
    
    def encontra_normalizada(self, coluna):
        """Esta função verifica se a coluna é uma coluna normalizada e retorna o índice da linha que tem o 1. Se não for, retorna 0.

        Args:
            coluna (array): Recebe um array com os valores da coluna.
        """
        uns = sum([1 for i in coluna if i == 1])
        zeros = sum([1 for i in coluna if i == 0])
        if uns == 1 and zeros == len(coluna) - 1:
            return coluna.index(1)
        else:
            return 0

    def performa_pivo(self, coluna_pivo, linha_pivo):
        """Esta função realiza o pivoteamento da matriz, transformando a coluna pivo em uma matriz identidade, o que significa que ela faz a linha pivo ter um valor 1 na coluna pivo e zera todos os outros elementos da coluna pivo.

        Args:
            coluna_pivo (integer): Índice da coluna pivo.
            linha_pivo (integer): Índice da linha pivo.
        """
        pivo = self.matriz[linha_pivo][coluna_pivo]
        for i in range(self.colunas):
            self.matriz[linha_pivo][i] /= pivo

        for i in range(self.linhas):
            if i != linha_pivo:
                fator = self.matriz[i][coluna_pivo]
                for j in range(self.colunas):
                    self.matriz[i][j] -= fator * self.matriz[linha_pivo][j]

    def resolve(self):
        """Esta função executa o algoritmo Simplex até encontrar uma solução ótima ou até descobrir que o problema não tem solução.
        """
        passo = 0
        while True:
            coluna_pivo = self.encontra_coluna_pivo()
            if coluna_pivo == -1:
                break
            linha_pivo = self.encontra_linha_pivo(coluna_pivo)
            if linha_pivo == -1:
                print("Solução não encontrada.")
                return
            if passo == 0:
                self.mostra_matriz(f"Pivo", coluna_pivo, linha_pivo)
            self.performa_pivo(coluna_pivo, linha_pivo)
            passo += 1
            self.mostra_matriz(f"Passo {passo}")
        
        self.mostra_solucao()
        self.mostra_resposta()

    def mostra_matriz(self, titulo, coluna_in=0, linha_out=0):
        """Esta função imprime a matriz na tela.
        """
        self.imprime_titulo(titulo)
        if coluna_in > 0:
            linha_in = [""] * self.colunas
            linha_in[coluna_in] = "IN"
            print("".join(["{:<8}".format(i) for i in linha_in]))
       
        for i in range(0, self.colunas):
            print("{:<8}".format(self.colunas_nomes[i]), end="")
        print()
        print("----------------------------------------------------------------------")
        for i in range(self.linhas):
            for j in range(self.colunas):
                print("{:<8.2f}".format(self.matriz[i][j]), end="")
            if linha_out > 0 and i == linha_out:
                print("OUT", end="")
            print()
        print()
    
    def mostra_solucao(self):
        """Esta função imprime a solução na tela.
        """
        self.imprime_titulo("Solução")
        print("{:<15} {:<15} {:<15}".format("VB", "VNB", "Z"))
        vnb = []
        z = ""
        for i in range(1, self.colunas - 1):
            coluna_nome = self.colunas_nomes[i]
            coluna = [self.matriz[j][i] for j in range(self.linhas)]
            linha = self.encontra_normalizada(coluna)
            if linha > 0:
                self.vb.append(f"{coluna_nome} = {self.matriz[linha][self.colunas - 1]:.2f}")
            else:
                vnb.append(f"{coluna_nome} = 0")
        z += f"z = {self.matriz[0][-1]:.2f}"        
        for i in range(max(len(self.vb), len(vnb))):
            vb_i = self.vb[i] if i < len(self.vb) else ""
            vnb_i = vnb[i] if i < len(vnb) else ""
            print("{:<15} {:<15} {:<15}".format(vb_i, vnb_i, z if i == 0 else ""))
        pass
    
    def mostra_resposta(self):
        """Esta função imprime a resposta final, que é o lucro máximo e a quantidade de cada produto que deve ser produzida para alcançar o lucro máximo.
        """
        self.imprime_titulo("Resposta")
        vb_x = [value for value in self.vb if value.startswith("x")]
        vb_pairs = [value.split(" = ") for value in vb_x]
        variaveis = [f"{float(pair[1]):.2f} unidades de {pair[0]}" for pair in vb_pairs]
        print(f"A empresa terá lucro máximo de R$ {self.matriz[0][-1]:.2f} com a produção de " + " e ".join(variaveis) + ".")
    
    def imprime_titulo(self, titulo):
        """Esta função imprime um título na tela.

        Args:
            titulo (string): Recebe uma string com o título a ser impresso.
        """
        print()
        print(titulo)
        print("=" * len(titulo))


def main():
    """Esta função é a função principal do programa, que é executada quando o programa é iniciado.
    """
    matriz = [
        [1, -20, -30, -10, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 0, 0, 400],
        [0, 2, 1, -1, 0, 1, 0, 200],
        [0, 3, 2, -1, 0, 0, 1, 300],
    ]
    simplex = Simplex(matriz, 3)
    simplex.resolve()


if __name__ == '__main__':
    main()
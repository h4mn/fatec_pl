import unittest
import simplex

class TestSimplex(unittest.TestCase):

    def inicializa(self):
        self.matrix = [
            [1, -20, -30, -10, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 0, 0, 400],
            [0, 2, 1, -1, 0, 1, 0, 200],
            [0, 3, 2, -1, 0, 0, 1, 300],
        ]
        self.simplex = simplex.Simplex(self.matrix)

    @unittest.skipIf(True, "Teste desativado")
    def test_mostra_solucao(self):
        self.inicializa()
        solucao = [233.35, 166.70, 133.35, 0, 0, 0, 8667.50]
        self.simplex.mostra_solucao(solucao)
    
    @unittest.skipIf(True, "Teste desativado")
    def test_mostra_resposta(self):
        self.inicializa()
        solucao = [233.35, 166.70, 133.35, 0, 0, 0, 8667.50]
        self.simplex.mostra_resposta(solucao)

    @unittest.skipIf(True, "Teste desativado")
    def test_encontra_coluna_pivo(self):
        coluna_pivo_correta = 2        
        self.inicializa()        
        self.assertEqual(self.simplex.encontra_coluna_pivo(), coluna_pivo_correta)

    @unittest.skipIf(True, "Teste desativado")
    def test_encontra_linha_pivo(self):
        coluna_pivo = 2
        linha_pivo_correta = 3
        self.inicializa()
        self.assertEqual(self.simplex.encontra_linha_pivo(coluna_pivo), linha_pivo_correta)

    def test_performa_pivo(self):
        coluna_pivo = 2
        linha_pivo = 3
        self.inicializa()
        self.simplex.performa_pivo(coluna_pivo, linha_pivo)

        self.assertEqual(self.simplex.matrix[linha_pivo][coluna_pivo], 1)
        self.assertEqual(self.simplex.matrix[linha_pivo][0], 0)
        self.assertEqual(self.simplex.matrix[linha_pivo][1], 1.5)
        self.assertEqual(self.simplex.matrix[linha_pivo][2], 1)
        self.assertEqual(self.simplex.matrix[linha_pivo][3], -0.5)
        self.assertEqual(self.simplex.matrix[linha_pivo][4], 0)
        self.assertEqual(self.simplex.matrix[linha_pivo][5], 0)
        self.assertEqual(self.simplex.matrix[linha_pivo][6], 0.5)
        self.assertEqual(self.simplex.matrix[linha_pivo][7], 150)

        self.assertEqual(self.simplex.matrix[0][coluna_pivo], 0)
        self.assertEqual(self.simplex.matrix[1][coluna_pivo], 0)
        self.assertEqual(self.simplex.matrix[2][coluna_pivo], 0)
        self.assertEqual(self.simplex.matrix[3][coluna_pivo], 1)

if __name__ == '__main__':
    unittest.main()
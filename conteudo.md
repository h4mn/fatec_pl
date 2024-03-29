# Entendendo a Programação Linear: uma abordagem na Pesquisa Operacional

## Índice

```sumary
1. Introdução
2. Programação Linear
  2.1. História da Programação Linear
  2.2. Áreas de aplicação da Programação Linear
  2.3. Novidades na Programação Linear
3. Métodos de resolução de problemas de Programação Linear
  3.1. Método Analítico
    3.1.1. Variáveis de decisão
    3.1.2. Função objetivo
    3.1.3. Restrições técnicas
    3.1.4. Domínio das variáveis
    3.1.5. Solução viável
    3.1.6. Solução ótima
4. Simplex
5. Conclusão
6. Referências
```

## 1. Introdução

Pesquisa Operacional (PO) é uma área da matemática que estuda métodos e técnicas para a tomada de decisão. A PO é aplicada em diversas áreas, como por exemplo, na economia, na engenharia, na administração, na medicina, na biologia, na física, na química, na computação, etc.

## 2. Programação Linear

### 2.1 História da Programação Linear

A Programação Linear (PL) é área importante da PO, e tem suas raízes na década de 1930, quando o matemático russo Leonid Kantorovich desenvolveu uma técnica chamada método do potencial, que permitia a resolução de problemas de alocação de recursos de maneira mais eficiente. Em 1947, o matemático norte-americano George Dantzig desenvolveu o método simplex, que é o principal algoritmo utilizado para resolver problemas de PL até hoje.

### 2.2 Áreas de aplicação da Programação Linear

As áreas de aplicação da PL podem ser na economia, na engenharia, na administração, na medicina, na biologia, na física, na química, na computação, etc. Como exemplo, podemos citar aplicação no planejamento da produção e distribuição de produtos em empresas, na alocação de recursos em projetos, na programação de horários em escolas e universidades, na otimização de carteiras de investimentos, no planejamento de rotas em transportes e logística, no processo de otimização em indústrias e atividades de agricultura, etc.

### 2.3 Novidades na Programação Linear

Como um campo de estudo muito ativo por muitas décadas e com novas tecnologias surgindo a cada dia, a PL é uma área que está em constante evolução. E com estas evoluções, algumas novidades interessantes estão surgindo, como por exemplo, a modelagem estocástica e o aprendizado de máquina. A programação linear estocástica é uma área da PL que estuda problemas de otimização em que os dados de entrada são probabilísticos. Já o aprendizado de máquina é uma área da computação que estuda métodos e técnicas para a criação de sistemas que aprendem com dados. A PL e o aprendizado de máquina são áreas que estão se tornando cada vez mais próximas, pois o aprendizado de máquina pode ser utilizado para resolver problemas de PL.

A PL é uma técnica matemática que estuda problemas de otimização. Esta técnica visa maximizar ou minimizar uma função linear sujeita a restrições lineares utilizando variáveis de decisão. Esta função linear é chamada de função objetivo e as restrições lineares são chamadas de restrições técnicas. Os métodos utilizados são o método analítico, o método gráfico e o método simplex.

## 3. Métodos de resolução de problemas de Programação Linear

### 3.1 Método Analítico

O método analítico é um método de resolução de problemas de PL que consiste em resolver o problema de PL fazendo uma análise do enunciado do problema, encontrando os componentes do modelo e transformando-o em uma formulação matemática. Este método envolve a formulação matemática do problema de otimização, a construção do modelo matemático, a determinação das variáveis de decisão, a determinação das restrições técnicas, a determinação da função objetivo, a resolução do problema de PL e a interpretação dos resultados.

Os componentes de uma formulação matemática pelo método analítico incluem Variáveis de decisão, Função objetivo, Restrições técnicas, Domínio das variáveis, Solução viável e Solução ótima.

#### 3.1.1 Variáveis de decisão

As variáveis de decisão são as variáveis que podem ser alteradas para atingir o objetivo do problema. São representadas por letras maiúsculas, como por exemplo, X_1, X_2, ..., X_n. Estas variáveis são valores que representam a quantidade de um determinado produto ou serviço que deve ser produzido ou fornecido. Por exemplo, X_1 pode representar a quantidade de um produto que deve ser produzido, X_2 pode representar a quantidade de um produto que deve ser comprado, X_3 pode representar a quantidade de um produto que deve ser vendido.

#### 3.1.2 Função objetivo

A função objetivo é a expressão matemática que representa o objetivo do problema, ou seja, o que deve ser maximizado ou minimizado. A função objetivo é uma combinação linear das variáveis de decisão, com coeficientes que refletem a contribuição de cada variável no objetivo. Se, no caso, o objetivo é maximizar o lucro, a função objetivo será dada por uma combinação linear das receitas e dos custos, como por exemplo, FO Max (z) = RX_1 + RX_2 + ... + RX_n, onde z é a função objetivo, R é o valor da receita formando o coeficiente da função objetivo. Se, no caso, o objetivo é minimizar o custo, a função objetivo será dada por uma combinação linear dos custos, como por exemplo, FO Min (z) = CX_1 + CX_2 + ... + CX_n, onde z é a função objetivo, C é o valor do custo formando o coeficiente da função objetivo.

#### 3.1.3 Restrições técnicas

As restrições técnicas são as limitações que devem ser observadas para que o problema possa ser resolvido. As restrições são expressas por meio de inequações ou equações lineares que relacionam as variáveis de decisão entre si. Por exemplo, se o problema for de maximização, as restrições serão expressas por meio de inequações, como por exemplo, X ≤ 100, Y ≤ 200, Z ≤ 300, etc. Se o problema for de minimização, as restrições serão expressas por meio de inequações, como por exemplo, X ≥ 100, Y ≥ 200, Z ≥ 300, etc.

#### 3.1.4 Domínio das variáveis

#### 3.1.5 Solução viável

#### 3.1.6 Solução ótima

### 3.2 Método Gráfico

```graphviz
  x2
5 ╢
4 ╫───────────+
3 ╢░░░░░░░░░░░|
2 ╢░░░░░░░░░░░|
1 ╢░░░░░░░░░░░|
0 ╚═╤═╤═╤═╤═╤═╪═╤═ x1
∙∙0∙1∙2∙3∙4∙5∙6∙7
```

## 4. Exemplo de resolução de um problema de Programação Linear

## Simplex

## Referências

[1] RODRIGUES, Luís Henrique et al. Pesquisa Operacional - Programação Linear Passo a Passo. Do entendimento do problema à interpretação da solução. São Leopoldo: Ed. UNISINOS, 2014. [Recurso eletrônico em PDF] Disponível em: <http://biblioteca.asav.org.br/vinculos/000045/000045c5.pdf>. Acesso em: 09 de abril de 2023.

https://pt.wikibooks.org/wiki/Pesquisa_operacional/Introdu%C3%A7%C3%A3o_%C3%A0_Programa%C3%A7%C3%A3o_Linear

[2] Pesquisa operacional/Introdução à Programação Linear. In: WikiLivros. Flórida: Wikimedia Foudation, 2021. Disponível em: <https://pt.wikibooks.org/wiki/Pesquisa_operacional/Introdu%C3%A7%C3%A3o_%C3%A0_Programa%C3%A7%C3%A3o_Linear>. Acesso em: 09 de abril de 2023.

[3] PROGRAMAÇÃO LINEAR. In: Wikipédia, a enciclopédia livre. Flórida: Wikimedia Foundation, 2021. Disponível em: <https://pt.wikipedia.org/wiki/Programa%C3%A7%C3%A3o_linear>. Acesso em: 09 de abril de 2023.

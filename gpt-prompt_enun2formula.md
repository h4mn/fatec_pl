# Formulação de prompt para o GPT

O objetivo deste prompt é treinar o ChatGPT para que possa gerar soluções para problemas de programação linear no formato padrão. O prompt é dividido em três partes: definições, exemplo e desafio. As definições é uma lista de regras que o ChatGPT deve seguir para gerar a solução do problema de programação linear. O exemplo é um problema de programação linear e a solução do problema de programação linear no formato padrão. O desafio é um problema de programação linear que o ChatGPT deve resolver seguindo as definições e o exemplo.

---

## Definição

1. ChatGPT, ao final deste prompt, você receberá um texto com um desafio que é um problema de programação linear.
2. Sua tarefa é identificar no texto do desafio os componentes do problema de programaçao linear e os componentes da formulação, como Variáveis de Decisão, Função Objetivo e Restrições e elaborar uma formulação dos termos matemáticos precisos de programação linear.
3. A formulação deve ser organizado em markdown e ser exibido em bloco de código, seguindo o padrão de variáveis de decisão, função o objetivo e restrições.
4. As variáveis de decisão devem estar no padrão X_1, X_2, X_3, ..., X_n, e ser tratadas em toda formulação da mesma forma. Os tokens das variáveis X_i deve estar formatado como código em markdown. Exemplo: `X_1`.
5. A função objetivo deve estar no padrão FO [Max|Min] (z) = NX_1 + NX_2 + NX_3 + ... + NX_n, onde N é o coeficiente da variável X_i e deve ser substituído pelo valor do coeficiente. A expressão deve estar formatada como código em markdown. Exemplo: `FO Max (z) = 6X_1 + 8X_2`.
6. As restrições devem estar no padrão R_i: NX_1 + NX_2 + NX_3 + ... + NX_n seguido do sinal de comparação e do valor da restrição e seguido do (tipo de restrição), onde i é o número da restrição e deve ser substituído pelo número da restrição, e N é o coeficiente da variável X_i e deve ser substituído pelo valor do coeficiente. A expressão deve estar formatada como código em markdown. Exemplo: R_1: `8X_1 + 4X_2 <= 400`.
7. A última restrição deve ser a Não Negatividade, que deve ser escrita da seguinte forma: ÑN: X_1, X_2, X_3, ..., X_n >= 0, onde i é o número da restrição e deve ser substituído pelo número da restrição. A expressão deve estar formatada como código em markdown. Exemplo: ÑN: `X_1, X_2 >= 0`.
8. O ChatGPT pode incluir breves explicações sempre entre parênteses a frente de que é explicado, como por exemplo: `FO Max (z) = 6X_1 + 8X_2` (Aqui estamos procurando maximizar o lucro total da planta de manufatura).
9. Estas são as definições, e a seguir você receberá um exemplo de problema de programação linear e um exemplo de formulação que é a respectiva resposta do ChatGPT.
10. Após o exemplo, você receberá o seu desafio que é o enunciado de um problema de programação linear para resolver seguindo as definições acima e o exemplo.

## Exemplo

### Exemplo de enunciado com um problema de programação linear

Obtenha uma mistura de produtos que contenha os nutrientes necessários e apresente o mínimo custo. Suponha que um agricultor queira adubar sua plantação e disponha de dois tipos de adubo. O adubo tipo A possui 6g de fósforo, 2g de nitrogênio e 16g de potássio para cada kg, a um custo de $20,00/kg. O adubo B possui 4g de fósforo, 6g de nitrogênio e 4g de potássio para cada kg, o custo é de $16,00/kg. Sabe-se que é necessário 1 kg de adubo para fertilizar 10 m2 de terra e que o solo em que estão as suas plantações necessita de pelo menos 6g de fósforo, 3g de nitrogénio e 8g de potássio a cada 10 m2 de terra.

### Exemplo da Resposta do ChatGPT em formato de Formulação do Problema

#### Variáveis

- `X_1`: Quantidade de adubo tipo A (kg)
- `X_2`: Quantidade de adubo tipo B (kg)

#### Função Objetivo

`FO Min (z) = 20X_1 + 16X_2`

#### Restrições

- R_1: `6X_1 + 4X_2 >= 6 (g/m2) x 10 (m2) = 60 (g)` (Restrição de fósforo)
- R_2: `2X_1 + 6X_2 >= 3 (g/m2) x 10 (m2) = 30 (g)` (Restrição de nitrogênio)
- R_3: `16X_1 + 4X_2 >= 8 (g/m2) x 10 (m2) = 80 (g)` (Restrição de potássio)
- R_4: `X_1, X_2 >= 0` (Restrição de não negatividade)

---

ChatGPT, por favor, responda o problema abaixo no formato dos exemplos fornecidos. Só aceito resposta para o problema abaixo. Não crie, nem invente nenhum problema. Apenas responda com o problema abaixo.

## Enunciado do Desafio para o ChatGPT resolver

Uma planta industrial fabrica garrafas plásticas com ou sem rótulo. As garrafas com rótulo são vendidas á $10,50 o lote, enquanto que as garrafas sem rótulo têm, preço de venda de $8,00 por lote. Para produzir um lote de garrafas com rótulo são consumidos 5kg de plástico a $1,00/kg, 0,5 m2 de papel a $2,00/m2 e 1 frasco de tinta a $1,00/frasco. Para produzir um lote de garrafas sem rótulo são consumidos 4kg de plástico a $1,00/kg. A fabricação de um lote de garrafas com rótulo exige 15 minutos da máquina de sopro, 10 minutos na operação de serigrafia, 5 minutos no recorte e 7 minutos de colagem. A produção de um lote de garrafas sem rótulo necessita de 20 minutos na máquina de sopro. A empresa opera num regime de 40 horas semanais e dispõe de 2 máquinas de sopro, 1 máquina de serigrafia e 1 máquina para recorte e colagem (na mesma máquina). Sabendo-se que no almoxarifado existe um estoque de 1200kg de plástico, 200 m de papel e 180 frascos de tinta e considerando-se que não haverá reposição antes de urna semana.

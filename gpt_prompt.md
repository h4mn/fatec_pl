# Formulação de prompt para o GPT

O objetivo deste prompt é treinar o GPT para que seja capaz de gerar uma solução para um problema de programação linear. Este prompt é dividido em três partes: Definições, Dois exemplos de problemas de programação linear e Dois exemplos de respostas do ChatGPT, e finalmente a entrada do usuário. O prompt inicia na próxima linha.

# Definição
ChatGPT, vou te passar algumas definições de como eu quero que você organize as informações para mim. Após as definições, vou te passar dois exemplos de problemas de programação linear e suas respectivas respostas de como eu espero que você organize as informações. Depois disso, você vai receber um problema de programação linear e eu quero que você me retorne a resposta organizada da mesma forma que eu te passei nos exemplos. Segue abaixo as definições:
Bom, você receberá um texto com um problema de programação linear e deverá retornar uma resposta com os dados do problema e a formulação dos termos matemáticos precisos de programação linear. O objetivo do ChatGPT é identificar os componentes da formulação, como Variáveis, Função Objetivo e Restrições. O ChatGPT deverá organizar o texto do problema em forma de mapa conceitual. A resposta deverá ter dois tópicos principais: Dados do Problema e Formulação do Problema. O tópico Dados do Problema deverá conter os dados organizados. O tópico Formulação do Problema deverá conter a formulação dos termos matemáticos precisos de programação linear, e deverá ser formulado da seguinte forma:
- Variáveis de Decisão: As variáveis do problema devem estar no padrão X_1, X_2, X_3, ..., X_n, e ser tratadas em toda formulação da mesma forma;
- Função Objetivo: Deverá estar no padrão FO [Max|Min] (z) = NX_1 + NX_2 + NX_3 + ... + NX_n, onde N é o coeficiente da variável X_i e deve ser substituído pelo valor do coeficiente;
- Restrições: As restrições do problema devem estar no padrão R_i = NX_1 + NX_2 + NX_3 + ... + NX_n seguido do sinal de comparação e do valor da restrição e seguido do `(tipo de restrição)`, onde i é o número da restrição e deve ser substituído pelo número da restrição, e N é o coeficiente da variável X_i e deve ser substituído pelo valor do coeficiente. A última restrição deverá ser a Não Negatividade, que deverá ser escrita da seguinte forma: R_i = X_1, X_2, X_3, ..., X_n >= 0, onde i é o número da restrição e deve ser substituído pelo número da restrição.

# Exemplo 1

## Exemplo de Texto com um problema de programação linear:
Considere uma planta de manufatura capaz de produzir dois produtos P e Q, cujo lucro por unidade seja $6,00 e $8,00, respectivamente. O processo produtivo envolve duas operações corte e furação. Para a operação de corte há 2 máquinas disponíveis e para a operação de furação há 3 máquinas em disponibilidade. Considerando que cada máquina opera 200horas/mês e que para produzir uma unidade do produto P sejam necessárias 8 horas de corte e 4 de furação e para a produção de uma unidade do produto Q sejam consumidas 4 horas de corte e 10 horas de furação.

## Exemplo da Resposta do ChatGPT:

### Exemplo de Dados do Problema
```
Planta de manufatura
|
|---- Produtos: P, Q
|     |---- P: lucro por unidades = $6,00
|     |---- Q: lucro por unidades = $8,00
|    
|---- Processo produtivo
      |---- Operação de corte
      |     |---- Máquinas disponíveis: 2
      |     |---- Horas de operação/mês: 200
      |     |---- Produto P
      |     |     |---- Horas de corte/unidade: 8
      |     |---- Produto Q
      |           |---- Horas de corte/unidade: 4
      |
      |---- Operação de furação
            |---- Máquinas disponíveis: 3
            |---- Horas de operação/mês: 200
            |---- Produto P
            |     |---- Horas de furação/unidade: 4
            |---- Produto Q
                  |---- Horas de furação/unidade: 10
```

### Exemplo de Formulação do Problema

#### Variáveis
- X_1: Quantidade de unidades do produto P produzidas
- X_2: Quantidade de unidades do produto Q produzidas

#### Função Objetivo
FO Max (z) = 6X_1 + 8X_2

#### Restrições
- R_1 = 8X_1 + 4X_2 <= 400 `(Restrição de horas de corte)`
- R_2 = 4X_1 + 10X_2 <= 600 `(Restrição de horas de furação)`
- R_3 = X_1, X_2 >= 0 `(Restrição de não negatividade)`

# Exemplo 2

## Exemplo de Texto com um problema de programação linear:
Obtenha uma mistura de produtos que contenha os nutrientes necessários e apresente o mínimo custo. Suponha que um agricultor queira adubar sua plantação e disponha de dois tipos de adubo. O adubo tipo A possui 6g de fósforo, 2g de nitrogênio e 16g de potássio para cada kg, a um custo de $20,00/kg. O adubo B possui 4g de fósforo, 6g de nitrogênio e 4g de potássio para cada kg, o custo é de $16,00/kg. Sabe-se que é necessário 1 kg de adubo para fertilizar 10 m2 de terra e que o solo em que estão as suas plantações necessita de pelo menos 6g de fósforo, 3g de nitrogénio e 8g de potássio a cada 10 m2 de terra. 

## Exemplo da Resposta do ChatGPT:

### Dados do Problema
```
Mistura de Produtos
|
|---- Tipos de adubo: A, B
|     |---- Características adubo tipo A:
|     |     |---- Composição (g/kg):
|     |     |     |---- 6g de fósforo
|     |     |     |---- 2g de nitrogênio
|     |     |     |---- 16g de potássio
|     |     |---- Custo: $20,00/kg
|     |
|     |---- Características adubo tipo B:
|           |---- Composição (g/kg):
|           |     |---- 4g de fósforo
|           |     |---- 6g de nitrogênio
|           |     |---- 4g de potássio
|           |---- Custo: $16,00/kg
|
|---- Necessidades:
|     |---- Adubo para fertilizar 10 (m2) de terra:
|     |     |---- 1kg
|     |
|     |---- Nutrientes necessários (pelo menos):
|           |---- 6g de fósforo
|           |---- 3g de nitrogênio
|           |---- 8g de potássio
|
|---- Mínimo custo:
|     |---- ?
```

### Formulação do Problema

#### Variáveis
- X_1: Quantidade de adubo tipo A (kg)
- X_2: Quantidade de adubo tipo B (kg)

#### Função Objetivo
FO Min (z) = 20X_1 + 16X_2

#### Restrições
- R_1 = 6X_1 + 4X_2 >= 6 (g/m2) x 10 (m2) = 60 (g) `(Restrição de fósforo)`
- R_2 = 2X_1 + 6X_2 >= 3 (g/m2) x 10 (m2) = 30 (g) `(Restrição de nitrogênio)`
- R_3 = 16X_1 + 4X_2 >= 8 (g/m2) x 10 (m2) = 80 (g) `(Restrição de potássio)`
- R_4 = X_1, X_2 >= 0 `(Restrição de não negatividade)`

ChatGPT responda baseado nas definições, e no formato dos exemplos fornecidos. Só aceito respostas que estejam no formato dos exemplos. E só aceito resposta para o problema abaixo. Não invente nenhum problema, nem responda com um problema que não seja o abaixo.

# Enunciado
Uma planta industrial fabrica garrafas plásticas com ou sem rótulo. As garrafas com rótulo são vendidas á $10,50 o lote, enquanto que as garrafas sem rótulo têm, preço de venda de $8,00 por lote. Para produzir um lote de garrafas com rótulo são consumidos 5kg de plástico a $1,00/kg, 0,5 m2 de papel a $2,00/m2 e 1 frasco de tinta a $1,00/frasco. Para produzir um lote de garrafas sem rótulo são consumidos 4kg de plástico a $1,00/kg. A fabricação de um lote de garrafas com rótulo exige 15 minutos da máquina de sopro, 10 minutos na operação de serigrafia, 5 minutos no recorte e 7 minutos de colagem. A produção de um lote de garrafas sem rótulo necessita de 20 minutos na máquina de sopro. A empresa opera num regime de 40 horas semanais e dispõe de 2 máquinas de sopro, 1 máquina de serigrafia e 1 máquina para recorte e colagem (na mesma máquina). Sabendo-se que no almoxarifado existe um estoque de 1200kg de plástico, 200 m de papel e 180 frascos de tinta e considerando-se que não haverá reposição antes de urna semana.

# Formulação de prompt para o GPT

O objetivo deste prompt é treinar o ChatGPT para que possa gerar soluções para problemas de programação linear no formato padrão. O prompt é dividido em três partes: definições, exemplo de problema de programação linear e exemplo de resposta do ChatGPT. O usuário é solicitado a resolver um problema de programação linear específico que é fornecido no prompt. Certifique-se de que o enunciado contenha tantos detalhes quanto possível sobre o problema de programação linear. O prompt inicia na próxima linha. (Ainda tem algumas falhas, mas já é um bom começo.)

# Definição
1. ChatGPT, você receberá um texto com um problema de programação linear.
2. Sua tarefa é identificar os componentes da formulação, como Variáveis de Decisão, Função Objetivo e Restrições.
3. Você deve retornar uma resposta com os dados do problema e a formulação dos termos matemáticos precisos de programação linear.
4. Para isso, é necessário criar dois tópicos principais: Dados do Problema e Formulação do Problema. E recebera o nivel de titulo 2 (##) em markdown.
5. No tópico Dados do Problema, organize as informações de forma clara e objetiva.
6. As informações do enunciado do problema devem ser organizadas em forma de mapa conceitual em markdown.
7. No tópico Formulação do Problema, formule os termos matemáticos precisos de programação linear, incluindo as variáveis de decisão, a função objetivo e as restrições. O título dos tópicos das Variáveis de Decisão, Função Objetivo e Restrições devem ter o nível de título 3 (###) em markdown.
8. As variáveis de decisão devem estar no padrão X_1, X_2, X_3, ..., X_n, e ser tratadas em toda formulação da mesma forma. Os tokens das variáveis X_i deve estar formatado como código em markdown. Exemplo: `X_1`.
9. A função objetivo deve estar no padrão FO [Max|Min] (z) = NX_1 + NX_2 + NX_3 + ... + NX_n, onde N é o coeficiente da variável X_i e deve ser substituído pelo valor do coeficiente. A expressão deve estar formatada como código em markdown. Exemplo: `FO Max (z) = 6X_1 + 8X_2`.
10. As restrições devem estar no padrão R_i: NX_1 + NX_2 + NX_3 + ... + NX_n seguido do sinal de comparação e do valor da restrição e seguido do (tipo de restrição), onde i é o número da restrição e deve ser substituído pelo número da restrição, e N é o coeficiente da variável X_i e deve ser substituído pelo valor do coeficiente. A expressão deve estar formatada como código em markdown. Exemplo: R_1: `8X_1 + 4X_2 <= 400`.
11. A última restrição deve ser a Não Negatividade, que deve ser escrita da seguinte forma: ÑN: X_1, X_2, X_3, ..., X_n >= 0, onde i é o número da restrição e deve ser substituído pelo número da restrição. A expressão deve estar formatada como código em markdown. Exemplo: ÑN: `X_1, X_2 >= 0`.
12. O ChatGPT pode incluir breves explicações sempre entre parênteses a frente de que é explicado, como por exemplo: `FO Max (z) = 6X_1 + 8X_2` (Aqui estamos procurando maximizar o lucro total da planta de manufatura).
13. Após as definições, serão apresentados dois exemplos de problemas de programação linear e suas respectivas respostas do ChatGPT, como modelo para você seguir de como organizar as informações.
14. Após o exemplo, você receberá o enunciado de um problema de programação linear para resolver seguindo as definições acima.

# Exemplo
## Enunciado com um problema de programação linear
Obtenha uma mistura de produtos que contenha os nutrientes necessários e apresente o mínimo custo. Suponha que um agricultor queira adubar sua plantação e disponha de dois tipos de adubo. O adubo tipo A possui 6g de fósforo, 2g de nitrogênio e 16g de potássio para cada kg, a um custo de $20,00/kg. O adubo B possui 4g de fósforo, 6g de nitrogênio e 4g de potássio para cada kg, o custo é de $16,00/kg. Sabe-se que é necessário 1 kg de adubo para fertilizar 10 m2 de terra e que o solo em que estão as suas plantações necessita de pelo menos 6g de fósforo, 3g de nitrogénio e 8g de potássio a cada 10 m2 de terra. 

## Exemplo da Resposta do ChatGPT
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
- `X_1`: Quantidade de adubo tipo A (kg)
- `X_2`: Quantidade de adubo tipo B (kg)

#### Função Objetivo
`FO Min (z) = 20X_1 + 16X_2`

#### Restrições
- R_1: `6X_1 + 4X_2 >= 6 (g/m2) x 10 (m2) = 60 (g)` (Restrição de fósforo)
- R_2: `2X_1 + 6X_2 >= 3 (g/m2) x 10 (m2) = 30 (g)` (Restrição de nitrogênio)
- R_3: `16X_1 + 4X_2 >= 8 (g/m2) x 10 (m2) = 80 (g)` (Restrição de potássio)
- R_4: `X_1, X_2 >= 0` (Restrição de não negatividade)

ChatGPT, por favor, responda o problema abaixo no formato dos exemplos fornecidos. Só aceito respostas que estejam no formato previamente definido e só aceito resposta para o problema abaixo. Não invente nenhum problema. Não responda com um problema que não seja o abaixo.

# Enunciado do Problema
Uma planta industrial fabrica garrafas plásticas com ou sem rótulo. As garrafas com rótulo são vendidas á $10,50 o lote, enquanto que as garrafas sem rótulo têm, preço de venda de $8,00 por lote. Para produzir um lote de garrafas com rótulo são consumidos 5kg de plástico a $1,00/kg, 0,5 m2 de papel a $2,00/m2 e 1 frasco de tinta a $1,00/frasco. Para produzir um lote de garrafas sem rótulo são consumidos 4kg de plástico a $1,00/kg. A fabricação de um lote de garrafas com rótulo exige 15 minutos da máquina de sopro, 10 minutos na operação de serigrafia, 5 minutos no recorte e 7 minutos de colagem. A produção de um lote de garrafas sem rótulo necessita de 20 minutos na máquina de sopro. A empresa opera num regime de 40 horas semanais e dispõe de 2 máquinas de sopro, 1 máquina de serigrafia e 1 máquina para recorte e colagem (na mesma máquina). Sabendo-se que no almoxarifado existe um estoque de 1200kg de plástico, 200 m de papel e 180 frascos de tinta e considerando-se que não haverá reposição antes de urna semana.

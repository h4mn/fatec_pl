# Formulação de prompt para o GPT

O objetivo deste prompt é treinar o ChatGPT para que possa gerar soluções para problemas de programação linear no formato padrão. O prompt é dividido em três partes: definições, exemplo e desafio. As definições é uma lista de regras que o ChatGPT deve seguir para gerar a solução do problema de programação linear. O exemplo é um problema de programação linear e a solução do problema de programação linear no formato padrão. O desafio é um problema de programação linear que o ChatGPT deve resolver seguindo as definições e o exemplo.

---

## Definição

1. ChatGPT, ao final deste prompt, você receberá um texto com um problema de programação linear.
2. Sua tarefa é identificar no texto os componentes do problema de programação linear e elaborar um mapa conceitual em markdown com as informações do problema.
3. O mapa conceitual deve ser organizado em markdown e ser exibido em bloco de código, seguindo o padrão de tópicos e sub-tópicos. Organize as informações de forma clara e objetiva.
4. Estas são as definições, e a seguir você receberá um exemplo de problema de programação linear e um exemplo de mapa conceintual que é a respectiva resposta do ChatGPT.
5. Após o exemplo, você receberá o seu desafio que é o enunciado de um problema de programação linear para resolver seguindo as definições acima e o exemplo.

## Exemplo

### Exemplo de enunciado com um problema de programação linear

Obtenha uma mistura de produtos que contenha os nutrientes necessários e apresente o mínimo custo. Suponha que um agricultor queira adubar sua plantação e disponha de dois tipos de adubo. O adubo tipo A possui 6g de fósforo, 2g de nitrogênio e 16g de potássio para cada kg, a um custo de $20,00/kg. O adubo B possui 4g de fósforo, 6g de nitrogênio e 4g de potássio para cada kg, o custo é de $16,00/kg. Sabe-se que é necessário 1 kg de adubo para fertilizar 10 m2 de terra e que o solo em que estão as suas plantações necessita de pelo menos 6g de fósforo, 3g de nitrogénio e 8g de potássio a cada 10 m2 de terra.

### Exemplo da Resposta do ChatGPT em formato de Mapa Conceitual em Markdown

```markdown
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

---

ChatGPT, por favor, responda o problema abaixo no formato dos exemplos fornecidos. Só aceito respostas que estejam no formato previamente definido e só aceito resposta para o problema abaixo. Não invente nenhum problema. Não responda com um problema que não seja o abaixo.

## Enunciado do Problema como Desafio para o ChatGPT resolver

Uma planta industrial fabrica garrafas plásticas com ou sem rótulo. As garrafas com rótulo são vendidas á $10,50 o lote, enquanto que as garrafas sem rótulo têm, preço de venda de $8,00 por lote. Para produzir um lote de garrafas com rótulo são consumidos 5kg de plástico a $1,00/kg, 0,5 m2 de papel a $2,00/m2 e 1 frasco de tinta a $1,00/frasco. Para produzir um lote de garrafas sem rótulo são consumidos 4kg de plástico a $1,00/kg. A fabricação de um lote de garrafas com rótulo exige 15 minutos da máquina de sopro, 10 minutos na operação de serigrafia, 5 minutos no recorte e 7 minutos de colagem. A produção de um lote de garrafas sem rótulo necessita de 20 minutos na máquina de sopro. A empresa opera num regime de 40 horas semanais e dispõe de 2 máquinas de sopro, 1 máquina de serigrafia e 1 máquina para recorte e colagem (na mesma máquina). Sabendo-se que no almoxarifado existe um estoque de 1200kg de plástico, 200 m de papel e 180 frascos de tinta e considerando-se que não haverá reposição antes de urna semana.

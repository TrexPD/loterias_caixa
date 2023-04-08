# Loterias Caixa

#### Uma biblioteca simples e fácil para receber dados de sorteio das loterias caixa!

## Bibliotecas usadas:

```functools```  ```locale```  ```requests```  ```urllib3```

## Instalação:

##### Para instalar o loterias-caixas em seu computador, basta digitar o seguinte comando no seu terminal:

```
pip install loterias-caixa
```

## Uso na prática:

##### Para receber os dados do sorteio mais recente, basta apenas instânciar a classe **'Loterias'** e dentro dela colocar a modalidade lotérica que você quiser, logo em seguida escolha o método de qual dado você quer receber, no exemplo abaixo usaremos a 'megasena' e logo em seguida queremos ver os dados do **valor arrecadado** então usamos o método "valor_arrecadado()"!

```
loteria = Loterias('megasena')
print(loto.valor_arrecadado())
```

#### Output:

```
R$ 53.208.981,00
```

##### Caso queira buscar por algum concurso em específico basta passar o argumento para o parâmetro **'concurso'**, neste exemplo usaremos o número **2572**, ele pode ser passado como **string** ou **número inteiro**!

```
loteria = Loterias('megasena', concurso=2572)
print(loto.valor_arrecadado())
```

##### Dica: caso queira ver todas as modalidades lotéricas digite o comando abaixo, isso irá lista todas!

```
print(Loterias._MODALIDADES_LOTERICAS)
```

<h2 align="center">
<strong>🌟
  Favorite este repositório
</strong>🌟
</h2>
<p align="center">
  Criado com ❤️ e Python por
<a href="https://github.com/TrexPD">Paulo Daniel (TrexPD)!</a>
</p>

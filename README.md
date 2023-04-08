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

#### Output:

```
['federal', 'diadesorte', 'duplasena', 'megasena', 'loteca', 'lotofacil', 'lotomania', 'quina', 'supersete', 'timemania']
```

#### Listando todos os métodos disponíveis!
```
loteria = Loterias('megasena', concurso=2572)

loteria.tipo_jogo()
loteria.numero()
loteria.nome_municipio_uf_sorteio()
loteria.data_de_apuracao()
loteria.valor_arrecadado()
loteria.valor_estimado_do_proximo_concurso()
loteria.valor_acumulado_do_proximo_concurso()
loteria.valor_acumulado_concurso_especial()
loteria.valor_acumulado_concurso_0_5()
loteria.acumulado()
loteria.indicador_concurso_especial()
loteria.dezenas_sorteadas_ordem_sorteio()
loteria.lista_resultado_equipe_esportiva()
loteria.numero_jogo()
loteria.nome_time_coracao_mes_sorte()
loteria.tipo_publicacao()
loteria.observacao()
loteria.local_sorteio()
loteria.data_proximo_concurso()
loteria.numero_concurso_anterior()
loteria.numero_concurso_proximo()
loteria.valor_total_premio_faixa_um()
loteria.numero_concurso_final_0_5()
loteria.lista_municipio_uf_ganhadores()
loteria.lista_rateio_premio()
loteria.lista_de_dezenas()
loteria.lista_de_dezenas_do_segundo_sorteio()
loteria.id()
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

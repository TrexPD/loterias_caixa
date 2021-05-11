# Dados de sorteios - Loterias Caixa

## Codigo para receber dados do sorteio atual

```
# -*- coding: utf-8 -*-
from loterias import *

concurso = MegaSena()

print(concurso.listaDezenas())
````
## ou use um sorteio especifico

```
# -*- coding: utf-8 -*-
from loterias import (MegaSena, LotoFacil, Quina, LotoMania, TimeMania,
                      DuplaSena, Federal, Loteca, DiadeSorte, SuperSet)

concurso = LotoFacil(2224)

print(concurso.listaDezenas())
````

## Abaixo todos os comandos

```
# -*- coding: utf-8 -*-
from loterias import MegaSena

concurso = MegaSena()

print(concurso.todosDados())
print(concurso.tipoJogo())
print(concurso.numero())
print(concurso.nomeMunicipioUFSorteio())
print(concurso.dataApuracao())
print(concurso.valorArrecadado())
print(concurso.valorEstimadoProximoConcurso())
print(concurso.valorAcumuladoProximoConcurso())
print(concurso.valorAcumuladoConcursoEspecial())
print(concurso.valorAcumuladoConcurso_0_5())
print(concurso.acumulado())
print(concurso.indicadorConcursoEspecial())
print(concurso.dezenasSorteadasOrdemSorteio())
print(concurso.listaResultadoEquipeEsportiva())
print(concurso.numeroJogo())
print(concurso.nomeTimeCoracaoMesSorte())
print(concurso.tipoPublicacao())
print(concurso.observacao())
print(concurso.localSorteio())
print(concurso.dataProximoConcurso())
print(concurso.numeroConcursoAnterior())
print(concurso.numeroConcursoProximo())
print(concurso.valorTotalPremioFaixaUm())
print(concurso.numeroConcursoFinal_0_5())
print(concurso.listaMunicipioUFGanhadores())
print(concurso.listaRateioPremio())
print(concurso.listaDezenas())
print(concurso.listaDezenasSegundoSorteio())
print(concurso.id())
```

from requests import get, ConnectionError
from functools import lru_cache
from urllib3 import disable_warnings, exceptions
from locale import setlocale, LC_ALL, currency

disable_warnings(exceptions.InsecureRequestWarning)
setlocale(LC_ALL, 'pt_BR.utf8')

@lru_cache()
class Loterias:
    __headers: dict = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'pt-br, en;q=0.9,*;q=0.8',
        'DNT': '1',  # Do Not Track Request Header
        'Connection': 'close'
    }

    _MODALIDADES_LOTERICAS: list[str] = sorted(['federal', 'diadesorte', 'duplasena', 'megasena',
                        'loteca', 'lotofacil', 'lotomania', 'quina', 'supersete', 'timemania'])

    def __init__(self, modalidade_lotérica: str, concurso: str | int = ''):
        self.m_lotérica: str = modalidade_lotérica.lower().strip()
        self.concurso: str = str(concurso)

    def _todos_os_dados(self):
        if self.m_lotérica not in Loterias._MODALIDADES_LOTERICAS:
            raise ValueError(f"Erro a modalidade '{self.m_lotérica}' não existe.\nDigite o comando \033[1m'Loterias._MODALIDADES_LOTERICAS'\033[m para ver todas as modalidades disponíveis!")
        try:
            url: str = f"https://servicebus2.caixa.gov.br/portaldeloterias/api/{self.m_lotérica}/{self.concurso}"
            requisicao = get(url, verify=False, headers=Loterias.__headers)
        except ConnectionError:
            raise ConnectionError('Aparentemente você está sem internet! :(')
        except:
            raise Exception
        else:
            return requisicao.json()

    def tipo_jogo(self) -> str:
        return self._todos_os_dados()['tipoJogo']

    def numero(self) -> int:
        return self._todos_os_dados()['numero']

    def nome_municipio_uf_sorteio(self) -> str:
        return self._todos_os_dados()['nomeMunicipioUFSorteio']

    def data_de_apuracao(self) -> str:
        return self._todos_os_dados()['dataApuracao']

    def valor_arrecadado(self) -> str:
        return currency(self._todos_os_dados()['valorArrecadado'], grouping=True)

    def valor_estimado_do_proximo_concurso(self) -> str:
        return currency(self._todos_os_dados()['valorEstimadoProximoConcurso'], grouping=True)

    def valor_acumulado_do_proximo_concurso(self) -> str:
        return currency(self._todos_os_dados()['valorAcumuladoProximoConcurso'], grouping=True)

    def valor_acumulado_concurso_especial(self) -> str:
        return currency(self._todos_os_dados()['valorAcumuladoConcursoEspecial'], grouping=True)

    def valor_acumulado_concurso_0_5(self) -> str:
        return currency(self._todos_os_dados()['valorAcumuladoConcurso_0_5'], grouping=True)

    def acumulado(self) -> bool:
        return self._todos_os_dados()['acumulado']

    def indicador_concurso_especial(self) -> int:
        return self._todos_os_dados()['indicadorConcursoEspecial']

    def dezenas_sorteadas_ordem_sorteio(self) -> list:
        return self._todos_os_dados()['dezenasSorteadasOrdemSorteio']

    def lista_resultado_equipe_esportiva(self) -> list | None:
        return self._todos_os_dados()['listaResultadoEquipeEsportiva']

    def numero_jogo(self) -> int:
        return self._todos_os_dados()['numeroJogo']

    def nome_time_coracao_mes_sorte(self) -> str:
        return self._todos_os_dados()['nomeTimeCoracaoMesSorte']

    def tipo_publicacao(self) -> int:
        return self._todos_os_dados()['tipoPublicacao']

    def observacao(self) -> str:
        return self._todos_os_dados()['observacao']

    def local_sorteio(self) -> str:
        return self._todos_os_dados()['localSorteio']

    def data_proximo_concurso(self) -> str:
        return self._todos_os_dados()['dataProximoConcurso']

    def numero_concurso_anterior(self) -> int:
        return self._todos_os_dados()['numeroConcursoAnterior']

    def numero_concurso_proximo(self) -> int:
        return self._todos_os_dados()['numeroConcursoProximo']

    def valor_total_premio_faixa_um(self) -> str:
        return self._todos_os_dados()['valorTotalPremioFaixaUm']

    def numero_concurso_final_0_5(self) -> int:
        return self._todos_os_dados()['numeroConcursoFinal_0_5']

    def lista_municipio_uf_ganhadores(self) -> list | None:
        return self._todos_os_dados()['listaMunicipioUFGanhadores']

    def lista_rateio_premio(self) -> list | None:
        return self._todos_os_dados()['listaRateioPremio']

    def lista_de_dezenas(self) -> list | None:
        return self._todos_os_dados()['listaDezenas']

    def lista_de_dezenas_do_segundo_sorteio(self) -> list | None:
        return self._todos_os_dados()['listaDezenasSegundoSorteio']

    def id(self) -> int | None:
        return self._todos_os_dados()['id']


loto = Loterias('lotofacil')
print(loto.valor_arrecadado())

# Mostrara todas as modalidades!
# print(Loterias._MODALIDADES_LOTERICAS)
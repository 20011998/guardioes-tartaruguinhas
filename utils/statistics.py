from typing import List, Dict, Any, Tuple

def contar_total_ninhos(ninhos: List[Dict[str, Any]]) -> int:
    """Retorna o número total de ninhos registrados."""
    return len(ninhos)

def media_ovos_por_risco(ninhos: List[Dict[str, Any]]) -> Dict[str, float]:
    """
    Calcula a média de ovos por ninho para cada categoria de risco.
    Retorna um dicionário com o risco como chave e a média de ovos como valor.
    """
    total_ovos_por_risco = {}
    contagem_ninhos_por_risco = {}

    for ninho in ninhos:
        risco = ninho["risco"]
        quantidade_ovos = ninho["quantidade_ovos"]

        if risco not in total_ovos_por_risco:
            total_ovos_por_risco[risco] = 0
            contagem_ninhos_por_risco[risco] = 0

        total_ovos_por_risco[risco] += quantidade_ovos
        contagem_ninhos_por_risco[risco] += 1

    medias = {}
    for risco, total_ovos in total_ovos_por_risco.items():
        if contagem_ninhos_por_risco[risco] > 0:
            medias[risco] = total_ovos / contagem_ninhos_por_risco[risco]
        else:
            medias[risco] = 0
    return medias

def ninhos_prestes_a_eclodir(ninhos: List[Dict[str, Any]], dias_limite: int = 5) -> int:
    """Conta quantos ninhos estão prestes a eclodir (dias_para_eclosao menor ou igual ao limite)."""
    ninhos_proximos = 0
    for ninho in ninhos:
        if ninho["dias_para_eclosao"] <= dias_limite:
            ninhos_proximos += 1
    return ninhos_proximos

def regiao_com_mais_ninhos_sob_risco(ninhos: List[Dict[str, Any]]) -> Tuple[str, int]:
    """
    Identifica a região com o maior número de ninhos em risco '🟡' ou '🔴'.
    Retorna a região e a contagem de ninhos sob risco.
    """
    contagem_risco_por_regiao = {}

    for ninho in ninhos:
        regiao = ninho["regiao"]
        risco = ninho["risco"]

        if risco == "🟡" or risco == "🔴":
            if regiao not in contagem_risco_por_regiao:
                contagem_risco_por_regiao[regiao] = 0
            contagem_risco_por_regiao[regiao] += 1

    if not contagem_risco_por_regiao:
        return "Nenhuma região com ninhos sob risco", 0

    regiao_mais_risco = ""
    max_ninhos_risco = 0
    for regiao, contagem in contagem_risco_por_regiao.items():
        if contagem > max_ninhos_risco:
            max_ninhos_risco = contagem
            regiao_mais_risco = regiao

    return regiao_mais_risco, max_ninhos_risco

def ninhos_com_predadores_e_danificados(ninhos: List[Dict[str, Any]]) -> int:
    """Conta quantos ninhos têm a presença de predadores e estão em status 'danificado'."""
    ninhos_afetados = 0
    for ninho in ninhos:
        if ninho["predadores"] and ninho["status"] == "danificado":
            ninhos_afetados += 1
    return ninhos_afetados

def contar_ninhos_por_status(ninhos: List[Dict[str, Any]]) -> Dict[str, int]:
    """Conta ninhos por status"""
    contagem = {"intacto": 0, "ameacado": 0, "danificado": 0}
    for ninho in ninhos:
        status = ninho["status"]
        if status in contagem:
            contagem[status] += 1
    return contagem

def contar_ninhos_por_regiao(ninhos: List[Dict[str, Any]]) -> Dict[str, int]:
    """Conta ninhos por região"""
    contagem = {}
    for ninho in ninhos:
        regiao = ninho["regiao"]
        contagem[regiao] = contagem.get(regiao, 0) + 1
    return contagem

def get_total_ovos(ninhos: List[Dict[str, Any]]) -> int:
    """Retorna o total de ovos em todos os ninhos"""
    return sum(ninho["quantidade_ovos"] for ninho in ninhos)

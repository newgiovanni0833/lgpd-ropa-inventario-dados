"""Validador de completude e risco de um ROPA em CSV.

Uso:
    python scripts/validar_ropa.py dados_exemplo/ropa_exemplo.csv [relatorio.md]

Saída: resumo no terminal e relatório em Markdown.
Código de saída 1 se houver apontamento crítico (útil em CI).
"""
from __future__ import annotations

import csv
import sys
from collections import Counter, defaultdict
from pathlib import Path

OBRIGATORIOS = [
    "id_operacao", "area_responsavel", "responsavel", "nome_atividade",
    "finalidade", "categorias_titulares", "categorias_dados",
    "hipotese_tratamento", "sistemas_e_locais", "prazo_guarda",
]

HIPOTESES = {
    "consentimento",
    "obrigação legal ou regulatória",
    "execução de políticas públicas",
    "estudos por órgão de pesquisa",
    "execução de contrato",
    "exercício regular de direitos",
    "proteção da vida",
    "tutela da saúde",
    "legítimo interesse",
    "proteção do crédito",
}

PRAZO_INDEFINIDO = {"indeterminado", "a definir", "indefinido", "não definido", "sem prazo"}

CRITICO, ATENCAO = "Crítico", "Atenção"


def sim(valor: str) -> bool:
    return valor.strip().lower() in {"sim", "s", "yes", "true", "1"}


def validar_linha(linha: dict[str, str]) -> list[tuple[str, str]]:
    """Devolve a lista de (severidade, mensagem) de uma operação."""
    v = {k: (linha.get(k) or "").strip() for k in linha}
    achados: list[tuple[str, str]] = []

    for campo in OBRIGATORIOS:
        if not v.get(campo):
            achados.append((CRITICO, f"Campo obrigatório vazio: `{campo}`"))

    tem_seguranca = bool(v.get("medidas_seguranca"))
    if sim(v.get("dados_sensiveis", "")) and not tem_seguranca:
        achados.append((CRITICO, "Dado sensível sem medida de segurança descrita"))
    if sim(v.get("dados_criancas_adolescentes", "")) and not tem_seguranca:
        achados.append((CRITICO, "Dado de criança ou adolescente sem medida de segurança descrita"))

    if sim(v.get("compartilhamento_externo", "")) and not v.get("destinatarios_operadores"):
        achados.append((CRITICO, "Compartilhamento externo sem destinatário ou operador identificado"))

    if v.get("prazo_guarda", "").lower() in PRAZO_INDEFINIDO:
        achados.append((ATENCAO, "Prazo de guarda indefinido"))

    if not v.get("forma_descarte"):
        achados.append((ATENCAO, "Forma de descarte não informada"))

    if sim(v.get("transferencia_internacional", "")) and not v.get("pais_destino"):
        achados.append((ATENCAO, "Transferência internacional sem país de destino"))

    hip = v.get("hipotese_tratamento", "")
    if hip and hip.lower() not in HIPOTESES:
        achados.append((ATENCAO, f"Hipótese de tratamento fora da lista padronizada: \"{hip}\""))

    return achados


def validar_arquivo(caminho: Path) -> tuple[list[dict[str, str]], dict[str, list[tuple[str, str]]]]:
    with caminho.open(encoding="utf-8-sig", newline="") as f:
        linhas = list(csv.DictReader(f, delimiter=";"))
    resultado = {l.get("id_operacao") or f"linha {i + 2}": validar_linha(l) for i, l in enumerate(linhas)}
    return linhas, resultado


def gerar_relatorio(linhas, resultado) -> str:
    total = len(linhas)
    sev = Counter(s for achados in resultado.values() for s, _ in achados)
    sem_apontamento = sum(1 for a in resultado.values() if not a)
    por_area: dict[str, Counter] = defaultdict(Counter)
    nomes = {}
    for l in linhas:
        ido = l.get("id_operacao", "")
        nomes[ido] = l.get("nome_atividade", "")
        for s, _ in resultado.get(ido, []):
            por_area[l.get("area_responsavel", "?")][s] += 1

    out = ["# Relatório de validação do ROPA", ""]
    out += [
        f"- Operações analisadas: **{total}**",
        f"- Operações sem apontamento: **{sem_apontamento}** ({sem_apontamento / total:.0%})" if total else "",
        f"- Apontamentos críticos: **{sev[CRITICO]}**",
        f"- Apontamentos de atenção: **{sev[ATENCAO]}**",
        f"- Operações com dado sensível: **{sum(sim(l.get('dados_sensiveis', '')) for l in linhas)}**",
        f"- Operações com compartilhamento externo: **{sum(sim(l.get('compartilhamento_externo', '')) for l in linhas)}**",
        "",
        "## Apontamentos por área", "",
        "| Área | Críticos | Atenção |", "|---|---:|---:|",
    ]
    for area in sorted(por_area):
        out.append(f"| {area} | {por_area[area][CRITICO]} | {por_area[area][ATENCAO]} |")
    out += ["", "## Apontamentos por operação", ""]
    for ido, achados in resultado.items():
        if not achados:
            continue
        out.append(f"### {ido} — {nomes.get(ido, '')}")
        for s, msg in sorted(achados):
            out.append(f"- **{s}:** {msg}")
        out.append("")
    return "\n".join(out) + "\n"


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print(__doc__)
        return 2
    entrada = Path(argv[1])
    saida = Path(argv[2]) if len(argv) > 2 else Path("relatorio_validacao.md")
    linhas, resultado = validar_arquivo(entrada)
    relatorio = gerar_relatorio(linhas, resultado)
    saida.write_text(relatorio, encoding="utf-8")

    criticos = sum(1 for a in resultado.values() for s, _ in a if s == CRITICO)
    atencao = sum(1 for a in resultado.values() for s, _ in a if s == ATENCAO)
    print(f"Operações: {len(linhas)} | críticos: {criticos} | atenção: {atencao}")
    print(f"Relatório gravado em {saida}")
    return 1 if criticos else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))

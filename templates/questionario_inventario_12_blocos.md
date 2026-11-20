# Questionário de Inventário de Dados — 12 blocos

Roteiro para levantar, com cada área, as operações de tratamento de dados pessoais. Responda **uma vez para cada atividade** (por exemplo: "inscrição em cursos", "folha de pagamento", "painel de indicadores de RH").

> Dica de preenchimento: descreva o que realmente acontece hoje, e não o que deveria acontecer. Lacunas são o resultado esperado de um primeiro inventário.

| Bloco | Tema | Perguntas-guia | Campo no ROPA |
|---|---|---|---|
| 1 | **Identificação** | Qual é a área? Quem responde pela atividade? | `area_responsavel`, `responsavel` |
| 2 | **Atividade** | Como a atividade se chama e o que ela faz, do início ao fim? | `nome_atividade`, `descricao` |
| 3 | **Finalidade** | Para que os dados são usados? O que deixaria de funcionar sem eles? | `finalidade` |
| 4 | **Titulares** | De quem são os dados? (clientes, alunos, colaboradores, fornecedores, visitantes) | `categorias_titulares` |
| 5 | **Dados tratados** | Quais dados são coletados? (identificação, contato, financeiros, profissionais, acadêmicos) | `categorias_dados` |
| 6 | **Dados sensíveis e de menores** | Há dados de saúde, biometria, origem racial, religião, filiação sindical? Há dados de crianças ou adolescentes? | `dados_sensiveis`, `dados_criancas_adolescentes` |
| 7 | **Origem** | Como os dados chegam? (formulário, sistema, planilha, terceiro, API) | `origem_dos_dados` |
| 8 | **Hipótese de tratamento** | Qual hipótese da LGPD sustenta o tratamento? Use a lista padronizada abaixo. | `hipotese_tratamento` |
| 9 | **Compartilhamento** | Os dados saem da organização? Para quem? Há fornecedor que os processa? | `compartilhamento_externo`, `destinatarios_operadores` |
| 10 | **Transferência internacional** | Algum sistema ou fornecedor armazena os dados fora do Brasil? Em que país? | `transferencia_internacional`, `pais_destino` |
| 11 | **Armazenamento, guarda e descarte** | Em quais sistemas, pastas ou arquivos físicos ficam? Por quanto tempo? Como são eliminados? | `sistemas_e_locais`, `prazo_guarda`, `forma_descarte` |
| 12 | **Segurança e acesso** | Quem acessa? Há controle por perfil, log, criptografia, backup? | `medidas_seguranca`, `perfis_com_acesso` |

## Lista padronizada de hipóteses de tratamento

Use exatamente um destes valores no campo `hipotese_tratamento`:

- Consentimento
- Obrigação legal ou regulatória
- Execução de políticas públicas
- Estudos por órgão de pesquisa
- Execução de contrato
- Exercício regular de direitos
- Proteção da vida
- Tutela da saúde
- Legítimo interesse
- Proteção do crédito

## Painéis de BI também entram no inventário

Um dashboard é uma operação de tratamento: ele copia, cruza e expõe dados. Para cada painel, registre uma linha própria, com atenção especial aos blocos 5 (quais dados aparecem na tela), 11 (onde o conjunto de dados fica publicado) e 12 (quem tem acesso e com qual perfil).

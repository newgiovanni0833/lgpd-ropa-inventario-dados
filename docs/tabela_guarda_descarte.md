# Tabela de guarda e descarte por macroprocesso (exemplo fictício)

Modelo de manual para orientar os gestores. Os prazos abaixo são **ilustrativos**: cada organização deve confirmá-los com base na legislação aplicável ao seu setor antes de adotá-los.

| Macroprocesso | Conjunto de dados | Prazo de guarda | Gatilho de contagem | Forma de descarte | Responsável |
|---|---|---|---|---|---|
| Educação | Cadastro e matrícula de alunos | 5 anos | Conclusão do curso | Exclusão lógica e anonimização para fins estatísticos | Coordenação de Cursos |
| Educação | Histórico e certificados | Permanente | — | Não se aplica | Secretaria |
| Pessoas | Folha e dados previdenciários | 30 anos | Desligamento | Exclusão lógica | Gerência de Pessoas |
| Pessoas | Registros de ponto | 5 anos | Fim do exercício | Exclusão lógica; template biométrico eliminado no desligamento | Gerência de Pessoas |
| Pessoas | Prontuário de saúde ocupacional | 20 anos | Desligamento | Exclusão lógica e destruição do físico | Medicina do trabalho |
| Pessoas | Currículos de candidatos não contratados | 1 ano | Encerramento da vaga | Exclusão da caixa de e-mail e da pasta de rede | Gerência de Pessoas |
| Comunicação | Base de newsletter | Até a revogação | Pedido do titular | Exclusão da plataforma | Comunicação |
| Financeiro | Cadastro de fornecedores | 10 anos | Fim do contrato | Exclusão lógica | Gerência Financeira |
| Tecnologia | Logs de autenticação | 6 meses | Data do registro | Rotação automática | Infraestrutura |
| Tecnologia | Conjuntos de dados de BI | Igual ao dado de origem | Descontinuação do painel | Remoção do conjunto de dados e do workspace | Equipe de Dados |

## Regras gerais

1. **Guardar pelo menor prazo que atenda à finalidade.** "Para sempre" só quando houver motivo documentado.
2. **Descarte é um processo, não um evento.** Deve ter responsável, periodicidade e registro de execução.
3. **Cópias contam.** Planilhas exportadas, anexos de e-mail e conjuntos de dados de BI seguem o prazo do dado de origem.
4. **Anonimizar é alternativa ao descarte** quando o dado agregado continua útil para planejamento.

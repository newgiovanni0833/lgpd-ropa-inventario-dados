# Mapa de fluxo de dados pessoais (exemplo fictício)

O mapa mostra por onde o dado pessoal entra, onde fica armazenado, quem o consome e por onde sai da organização. Ele é desenhado a partir dos blocos 7, 9, 10 e 11 do questionário.

```mermaid
flowchart LR
    subgraph Entrada
        F1[Formulário web]
        F2[Lista física]
        F3[Relógio de ponto]
        F4[Clínica credenciada]
    end

    subgraph Sistemas internos
        S1[(Sistema de Gestão<br/>de Eventos)]
        S2[(ERP corporativo)]
        S3[(Sistema de ponto)]
        S4[(Saúde ocupacional)]
        R[(Repositório de dados<br/>SQL Server)]
    end

    subgraph Consumo
        B1[Painel de Cursos<br/>dados agregados]
        B2[Painel de Pessoas<br/>segurança por linha]
    end

    subgraph Saída externa
        E1[Plataforma de certificados<br/>🌎 fora do Brasil]
        E2[Banco pagador]
        E3[Contabilidade]
    end

    F1 --> S1
    F2 --> S1
    F3 --> S3 --> S2
    F4 --> S4
    S1 --> R
    S2 --> R
    R --> B1
    R --> B2
    S1 --> E1
    S2 --> E2
    S2 --> E3

    classDef sensivel fill:#fde2e2,stroke:#c0392b,color:#000
    classDef externo fill:#fff3cd,stroke:#b7791f,color:#000
    class S3,S4,F3,F4 sensivel
    class E1,E2,E3 externo
```

**Legenda:** vermelho indica fluxo com dado sensível (biometria e saúde); amarelo indica saída para terceiros.

## Pontos de controle identificados

| Ponto | Risco | Controle recomendado |
|---|---|---|
| Sistema de ponto → ERP | Biometria trafegando entre sistemas | Integrar apenas o identificador e a marcação; o template biométrico não sai do sistema de origem |
| Saúde ocupacional | Dado de saúde acessível fora da equipe técnica | Base isolada do repositório analítico; BI recebe somente indicadores agregados |
| Repositório → Painel de Pessoas | Exposição de dados individuais a gestores | Segurança em nível de linha e termo de confidencialidade por usuário |
| Sistema de eventos → Plataforma de certificados | Transferência internacional | Contrato com cláusulas de proteção de dados e envio do mínimo necessário (nome, curso, data) |
| Lista física | Perda ou acesso indevido | Digitalização, guarda em armário com chave e fragmentação ao fim do prazo |

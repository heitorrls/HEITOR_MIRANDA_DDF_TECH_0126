# Case Técnico Dadosfera: E-commerce Analytics & IA

##  Visão Geral do Projeto
Este projeto foi desenvolvido como parte do processo seletivo da **Dadosfera**. O objetivo é demonstrar a aplicação do ciclo de vida de dados em uma base de E-commerce com mais de 10.000 registros, integrando gestão de projetos (PMBOK), engenharia de dados e inteligência artificial generativa.

O desafio foca em transformar dados brutos de transações em insights estratégicos para otimização de faturamento e análise de comportamento do consumidor.

---
## Análise de Riscos e Mitigação
Seguindo as diretrizes de gerenciamento de projetos (PMBOK), foram mapeados os seguintes riscos críticos para a execução do ciclo de vida de dados:

Risco de Qualidade de Dados: Presença de registros nulos na coluna Category e possíveis inconsistências (outliers) na coluna Price (Rs.).

Mitigação: Desenvolvimento de um pipeline de tratamento via Python utilizando a biblioteca Pandas para imputação de dados e validação de ranges estatísticos.

Risco Técnico de Infraestrutura: Dificuldade técnica na ingestão de dados via interface gráfica da plataforma.

Mitigação: Adoção de uma estratégia de "Data as Code", centralizando o processamento no ecossistema GitHub e Streamlit Cloud para garantir que o projeto seja 100% reprodutível.

Risco de Alucinação em IA: Geração de insights incorretos pelo modelo de linguagem (LLM).

Mitigação: Aplicação de técnicas de Prompt Engineering para limitar as respostas da IA aos dados factuais presentes no dataset de 10.005 registros.

## Estimativa de Recursos
A alocação de recursos foi planejada para otimizar a entrega técnica dentro do prazo estipulado:

Recursos Humanos: 1 Analista de Dados (focado em Engenharia, BI e implementação de IA).

Recursos Tecnológicos:

Processamento: Google Colab com ambiente Python 3.10+ para manipulação de grandes volumes de dados.

Visualização e App: Streamlit Community Cloud para hospedagem da interface interativa.

IA Generativa: Integração com APIs de modelos de linguagem (OpenAI/Gemini) para análise avançada de dados.

Governança: GitHub para versionamento de código e documentação.


##  Planejamento e Gestão (PMBOK)
Seguindo as melhores práticas de gestão de projetos, o desenvolvimento foi dividido nas seguintes fases:

### Cronograma de Execução 
OBS: Quadro Kanban feito aqui nesse repositório github na guia de Projects
```mermaid
gantt
    title Planejamento do Projeto
    dateFormat  YYYY-MM-DD
    section Iniciação
    Definição do Escopo e Dataset    :done, 2025-01-01, 1d
    section Planejamento
    Criação da Arquitetura e Riscos :done, 2025-01-02, 1d
    section Execução
    Ingestão e Catálogo (Dadosfera) :done, 2025-01-03, 2d
    Tratamento e Qualidade de Dados  :done, 2025-01-05, 2d
    Desenvolvimento do Data App      :done, 2026-01-07, 3d
    section Encerramento
    Documentação e Vídeo             :done, 2026-01-10, 1d


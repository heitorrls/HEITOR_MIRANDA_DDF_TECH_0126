# Case Técnico Dadosfera: E-commerce Analytics & IA

##  Visão Geral do Projeto
Este projeto foi desenvolvido como parte do processo seletivo da **Dadosfera**. O objetivo é demonstrar a aplicação do ciclo de vida de dados em uma base de E-commerce com mais de 10.000 registros, integrando gestão de projetos (PMBOK), engenharia de dados e inteligência artificial generativa.

O desafio foca em transformar dados brutos de transações em insights estratégicos para otimização de faturamento e análise de comportamento do consumidor.

---
##  Dicionário de Dados

A base de dados utilizada contém 10.005 registros transacionais com as seguintes características:

| Coluna | Tipo | Descrição | Exemplo |
| :--- | :--- | :--- | :--- |
| `User_ID` | String | Identificador único do cliente. | `337c166f` |
| `Product_ID` | String | Identificador único do produto. | `f414122f-e` |
| `Category` | Categórico | Categoria do item (contém valores nulos para fins de teste de qualidade). | `Sports` |
| `Price (Rs.)` | Float | Preço original do produto em Rúpias. | `3653` |
| `Discount (%)` | Inteiro | Percentual de desconto aplicado à venda. | `15` |
| `Final_Price(Rs.)` | Float | Valor líquido da transação após o desconto. | `3105` |
| `Payment_Method` | Categórico | Meio de pagamento utilizado na transação. | `Net Banking` |
| `Purchase_Date` | Data | Data da compra no formato DD/MM/YYYY. | `12/11/2024` |

---

##  Análise de Riscos e Mitigação

Seguindo as diretrizes do PMBOK, foram mapeados os seguintes riscos para o ciclo de vida dos dados:

* **Risco de Qualidade de Dados**: Presença de registros nulos na coluna `Category` e possíveis inconsistências nos preços.
    * **Mitigação**: Implementação de pipeline de limpeza em Python (Pandas) para imputação de valores e validação estatística.
* **Risco Técnico**: Dificuldade de ingestão via interface da plataforma.
    * **Mitigação**: Centralização da solução no ecossistema GitHub e Streamlit Cloud, garantindo a reprodutibilidade via código.
* **Risco de Alucinação em IA**: Geração de insights incorretos pelo modelo de linguagem.
    * **Mitigação**: Uso de *Prompt Engineering* para ancorar as respostas do LLM estritamente nos dados do dataset.

---

##  Estimativa de Recursos

* **Pessoas**: 1 Analista de Dados (Engenharia, BI e IA).
* **Processamento**: Google Colab (Python 3.10+).
* **Hospedagem**: Streamlit Community Cloud para o Data App.
* **Modelos de IA**: API de LLM (OpenAI/Gemini) para análise de linguagem natural.

---

##  Arquitetura da Solução

O projeto foi estruturado seguindo as fases do ciclo de vida de dados da plataforma Dadosfera:

1. **Integrar**: Ingestão do dataset de 10.005 registros no repositório GitHub.
2. **Explorar**: Catalogação de metadados e criação do Dicionário de Dados detalhado.
3. **Processar**: Limpeza de valores nulos (coluna `Category`) e normalização de tipos via Python e Pandas.
4. **Qualidade**: Auditoria de dados para garantir integridade dos KPIs e tratamento de outliers de preço.
5. **Analisar**: Desenvolvimento de dashboards interativos no Streamlit.
6. **IA**: Implementação de um assistente inteligente (LLM) para geração de insights de negócio.

---

##  Entregáveis

* **Data App (Streamlit)**: https://heitormirandaddftech0126-mbmkbkizbxgclkwuppj95m.streamlit.app
* **Notebook de Desenvolvimento**: https://colab.research.google.com/drive/1OaO7lp0ZPODgw0AK56qjeGlvm2E5P2aC?usp=sharing
* **Vídeo de Apresentação**: [Link do YouTube - Não Listado]

##  Planejamento e Gestão (PMBOK)
Seguindo as melhores práticas de gestão de projetos, o desenvolvimento foi dividido nas seguintes fases:

### Cronograma de Execução 
OBS: Quadro Kanban feito aqui nesse repositório github na guia de Projects
```mermaid
gantt
    title Planejamento do Projeto 
    dateFormat  YYYY-MM-DD
    section Iniciação
    Definição do Escopo e Dataset    :done, 2026-01-01, 1d
    section Planejamento
    Criação da Arquitetura e Riscos :done, 2026-01-02, 1d
    section Execução
    Ingestão e Catálogo (GitHub)    :done, 2026-01-03, 2d
    Tratamento e Qualidade de Dados  :done, 2026-01-04, 2d
    Desenvolvimento do Data App      :done, 2026-01-04, 3d
    section Encerramento
    Documentação e Vídeo             :done, 2026-01-04, 1d


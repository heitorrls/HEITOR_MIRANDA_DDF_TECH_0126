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


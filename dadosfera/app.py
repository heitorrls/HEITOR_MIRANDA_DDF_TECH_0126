import streamlit as st
import pandas as pd
import plotly.express as px
import google.generativeai as genai

# 1. Configuração da Página
st.set_page_config(page_title="Dadosfera | E-commerce Analytics", layout="wide")

# 2. Configuração da IA (Google Gemini)
# O código tenta primeiro usar os Secrets do Streamlit (para o Deploy)
# Caso não encontre, utiliza a chave configurada como fallback
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    # Esta chave permite que o teste funcione localmente caso o secrets.toml não seja encontrado
    genai.configure(api_key="AIzaSyDW6i7cgDcqtKbOtPxoLW4woda-wXjRdxo")

model = genai.GenerativeModel('gemini-2.5-flash')
# 3. Carregamento dos Dados (Camada Silver)
@st.cache_data
def load_data():
    # Carrega o dataset limpo gerado na etapa de engenharia
    df = pd.read_csv('ecommerce_limpo.csv', sep=';')
    # Padroniza a coluna de data para facilitar análises temporais
    df['Purchase_Date'] = pd.to_datetime(df['Purchase_Date'])
    return df

df = load_data()

# 4. Cabeçalho do Dashboard
st.title("Dadosfera: E-commerce Analytics & IA")
st.markdown(f"Análise de **{len(df)}** transações processadas com sucesso.")

# 5. KPIs Principais (Métricas Estratégicas)
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Volume de Vendas", f"{len(df):,}")
with col2:
    faturamento = df['Final_Price(Rs.)'].sum()
    st.metric("Faturamento Total (Rs.)", f"{faturamento:,.2f}")
with col3:
    ticket_medio = df['Final_Price(Rs.)'].mean()
    st.metric("Ticket Médio (Rs.)", f"{ticket_medio:,.2f}")

# 6. Dashboards Interativos (Visualização de Dados)
st.divider()
col_left, col_right = st.columns(2)

with col_left:
    # Gráfico de barras com a contagem de vendas por categoria
    vendas_cat = df['Category'].value_counts().reset_index()
    fig_cat = px.bar(vendas_cat, x='Category', y='count', 
                     title="Volume de Vendas por Categoria",
                     labels={'count': 'Vendas', 'Category': 'Categoria'})
    st.plotly_chart(fig_cat, use_container_width=True)

with col_right:
    # Gráfico de pizza para visualizar a preferência por métodos de pagamento
    fig_pay = px.pie(df, names='Payment_Method', 
                     title="Distribuição por Método de Pagamento",
                     hole=0.4)
    st.plotly_chart(fig_pay, use_container_width=True)

# 7. Assistente de IA (Integração com Gemini Pro)
st.divider()
st.subheader("🤖 Assistente Inteligente Dadosfera")
st.info("Pergunte à IA sobre tendências, categorias ou métricas do dataset.")

user_question = st.text_input("Exemplo: Qual categoria tem o maior ticket médio?")

if user_question:
    estatisticas_gerais = df.describe(include='all').to_string()
    resumo_categorias = df.groupby('Category')[['Price (Rs.)', 'Discount (%)', 'Final_Price(Rs.)']].mean().to_string()
    
    contexto = f"""
    Você é o Analista Especialista do Case Dadosfera.
    Você tem acesso a uma base de {len(df)} vendas de e-commerce.
    
    ESTATÍSTICAS GERAIS DA BASE:
    {estatisticas_gerais}
    
    MÉDIAS POR CATEGORIA (Preço, Desconto e Valor Final):
    {resumo_categorias}
    
    PERGUNTA DO USUÁRIO: {user_question}
    
    INSTRUÇÃO: Use os dados acima para responder de forma precisa. Se a pergunta for sobre descontos, 
    consulte a tabela de 'MÉDIAS POR CATEGORIA' que eu te enviei.
    """
    
    with st.spinner('A IA está analisando os 10.005 registros...'):
        try:
            model = genai.GenerativeModel('gemini-2.5-flash')
            response = model.generate_content(contexto)
            st.markdown("### 🤖 Resposta da IA Baseada nos Dados:")
            st.success(response.text)
        except Exception as e:
            st.error(f"Erro na análise: {e}")
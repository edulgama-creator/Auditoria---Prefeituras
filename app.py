import streamlit as st
import pandas as pd

# Configuração da página
st.set_page_config(page_title="Transparência Praia Grande", layout="wide")

st.title("📊 Painel de Transparência - Praia Grande")
st.write("Esta ferramenta analisa os gastos da Câmara Municipal para identificar possíveis riscos.")

# Carregar dados
@st.cache_data
def carregar_dados():
    df = pd.read_csv("despesas_praia_grande.csv", sep=";")
    df['vl_despesa'] = pd.to_numeric(df['vl_despesa'].astype(str).str.replace(',', '.'), errors='coerce')
    return df

dados = carregar_dados()

# Sidebar para filtros
st.sidebar.header("Filtros")
empresa_filtro = st.sidebar.text_input("Procurar por empresa:")

# Aplicar filtros
if empresa_filtro:
    dados_exibicao = dados[dados['nm_fornecedor'].str.contains(empresa_filtro, case=False, na=False)]
else:
    dados_exibicao = dados

# Exibir tabela
st.subheader("Lista de Despesas")
st.dataframe(dados_exibicao.sort_values(by="vl_despesa", ascending=False))

# Estatísticas Rápidas
st.subheader("Estatísticas Gerais")
col1, col2 = st.columns(2)
col1.metric("Total de Registos", len(dados))
col2.metric("Valor Total Auditado", f"R$ {dados['vl_despesa'].sum():,.2f}")

# Botão de Auditoria IA (chamada ao seu motor)
if st.button("Executar Auditoria de IA"):
    st.info("O motor de auditoria está a analisar os dados... aguarde.")
    # Aqui você chamaria o seu detetive_final.py ou a função de IA
    st.success("Auditoria concluída! (Integre aqui a lógica do seu motor)")
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Dashboard Deputados 2018", layout="wide")

st.title("Dashboard - Deputados 2018")
st.markdown("Análise visual dos dados do arquivo CSV utilizando Streamlit.")

# Upload do arquivo
uploaded_file = st.file_uploader("Envie o arquivo CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.success("Arquivo carregado com sucesso!")

    st.subheader("Pré-visualização dos dados")
    st.dataframe(df.head())

    # Informações gerais
    st.subheader("Informações Gerais")
    col1, col2, col3 = st.columns(3)

    col1.metric("Total de Deputados", len(df))

    if "partido" in df.columns:
        col2.metric("Quantidade de Partidos", df["partido"].nunique())

    if "UF" in df.columns:
        col3.metric("Quantidade de Estados", df["UF"].nunique())

    # -----------------------------
    # Gráfico 1 - Deputados por partido
    # -----------------------------
    if "partido" in df.columns:
        st.subheader("Deputados por Partido")

        partido_count = df["partido"].value_counts().head(10)

        fig, ax = plt.subplots(figsize=(10, 5))
        partido_count.plot(kind="bar", ax=ax)

        ax.set_xlabel("Partido")
        ax.set_ylabel("Quantidade")
        ax.set_title("Top 10 Partidos com Mais Deputados")

        st.pyplot(fig)

    # -----------------------------
    # Gráfico 2 - Deputados por UF
    # -----------------------------
    if "UF" in df.columns:
        st.subheader("Deputados por Estado")

        uf_count = df["UF"].value_counts()

        fig, ax = plt.subplots(figsize=(12, 5))
        uf_count.plot(kind="bar", ax=ax)

        ax.set_xlabel("UF")
        ax.set_ylabel("Quantidade")
        ax.set_title("Quantidade de Deputados por Estado")

        st.pyplot(fig)

    # -----------------------------
    # Gráfico 3 - Receita Total
    # -----------------------------
    if "total_receita" in df.columns:
        st.subheader("Distribuição da Receita Total")

        fig, ax = plt.subplots(figsize=(10, 5))
        ax.hist(df["total_receita"].dropna(), bins=20)

        ax.set_xlabel("Receita Total")
        ax.set_ylabel("Frequência")
        ax.set_title("Distribuição da Receita Total")

        st.pyplot(fig)

    # -----------------------------
    # Gráfico 4 - Eleitos x Não Eleitos
    # -----------------------------
    if "eleito" in df.columns:
        st.subheader("🗳️ Eleitos x Não Eleitos")

        eleito_count = df["eleito"].value_counts()

        fig, ax = plt.subplots(figsize=(6, 6))
        ax.pie(eleito_count, labels=["Não Eleito", "Eleito"], autopct="%1.1f%%")
        ax.set_title("Resultado das Eleições")

        st.pyplot(fig)

    # -----------------------------
    # Filtro interativo
    # -----------------------------
    st.subheader("Filtro por Partido")

    if "partido" in df.columns:
        partidos = sorted(df["partido"].dropna().unique())
        partido_escolhido = st.selectbox("Selecione um partido", partidos)

        df_filtrado = df[df["partido"] == partido_escolhido]

        st.write(f"Quantidade de deputados do partido {partido_escolhido}: {len(df_filtrado)}")
        st.dataframe(df_filtrado)

else:
    st.info("Faça upload do arquivo CSV para visualizar os gráficos.")

st.markdown("---")
st.caption("Projeto desenvolvido com Python + Streamlit")


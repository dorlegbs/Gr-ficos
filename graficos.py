import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Dashboard Eleições 2018",
    layout="wide"
)

st.title("Eleições 2018")

df = pd.read_csv("deputados_2018.csv")

col1, col2 = st.columns(2)

# Gráfico 1 - Deputados por partido

with col1:

    if "partido" in df.columns:

        st.subheader("Deputados por Categoria")

        partido_count = df["partido"].value_counts().head(10)

        fig, ax = plt.subplots(figsize=(8, 5))

        ax.bar(
            partido_count.index,
            partido_count.values,
            color="royalblue"
        )

        ax.set_xlabel("Partido")
        ax.set_ylabel("Quantidade")

        ax.grid(axis="y", linestyle="--", alpha=0.5)

        plt.xticks(rotation=45)

        st.pyplot(fig)

# Gráfico 2 - Homens x Mulheres

with col2:

    if "sexo" in df.columns:

        st.subheader("Homens x Mulheres")

        sexo_count = df["sexo"].value_counts()

        fig, ax = plt.subplots(figsize=(6, 6))

        cores = ["dodgerblue", "deeppink"]

        ax.pie(
            sexo_count.values,
            labels=sexo_count.index,
            autopct="%1.1f%%",
            colors=cores
        )

        st.pyplot(fig)

# Gráfico 3 - Direita x Centro x Esquerda

if "categoria" in df.columns:

    st.subheader("Direita x Centro x Esquerda")

    categoria_count = df["categoria"].value_counts()

    fig, ax = plt.subplots(figsize=(10, 5))

    cores = ["blue", "orange", "green"]

    ax.bar(
        categoria_count.index,
        categoria_count.values,
        color=cores
    )

    ax.set_xlabel("Categoria")
    ax.set_ylabel("Número de Deputados")

    ax.grid(axis="y", linestyle="--", alpha=0.5)

    st.pyplot(fig)

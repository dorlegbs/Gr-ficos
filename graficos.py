import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.set_page_config(page_title="Dashboard Eleições 2018", layout="wide")

st.title("Eleições 2018")
st.markdown("Visualização simples dos dados dos deputados de 2018.")

df = pd.read_csv("deputados_2018.csv")


# Gráfico 1 - Deputados por partido

if "partido" in df.columns:
    st.subheader("Deputados por Partido")

partido_count = df["partido"].value_counts().head(10)

fig, ax = plt.subplots(figsize=(10, 5))
partido_count.plot(kind="bar", ax=ax)

# Gráfico 2 - Homens x Mulheres

if "sexo" in df.columns:
    st.subheader("Deputados Homens x Mulheres")

    sexo_count = df["sexo"].value_counts()

    fig, ax = plt.subplots(figsize=(6, 6))
    ax.pie(sexo_count.values, labels=sexo_count.index, autopct="%1.1f%%")
    ax.set_title("Distribuição por Sexo")

    st.pyplot(fig)


# Gráfico 3 - Direita x Centro x Esquerda

if "ideologia" in df.columns:
    st.subheader("Comparação Direita x Centro x Esquerda")

    ideologia_count = df["ideologia"].value_counts()

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(ideologia_count.index, ideologia_count.values, marker="o")

    ax.set_xlabel("Posicionamento")
    ax.set_ylabel("Quantidade")
    ax.set_title("Direita, Centro e Esquerda")

    st.pyplot(fig)

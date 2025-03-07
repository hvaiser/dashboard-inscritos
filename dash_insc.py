import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados
file_path = "/mnt/data/Inscritos CINASE POA ATUALIZADO 070325.xlsx"
df = pd.read_excel(file_path, sheet_name="ListaParticipante")

# Converter a coluna de data para datetime
df["Data Inscrição"] = pd.to_datetime(df["Data Inscrição"], errors="coerce")

# Calcular métricas
num_inscritos = df.shape[0]
categoria_counts = df["Categoria"].value_counts()
cargo_counts = df["Cargo"].value_counts().head(10)
empresa_counts = df["Empresa"].value_counts().head(10)
inscricoes_por_dia = df.groupby(df["Data Inscrição"].dt.date).size()

# Criar o dashboard
st.title("Dashboard de Inscrições - CINASE POA")

st.metric(label="Total de Inscritos", value=num_inscritos)

# Gráfico de distribuição por categoria
st.subheader("Distribuição de Inscritos por Categoria")
fig, ax = plt.subplots()
categoria_counts.plot(kind='bar', color=['blue', 'orange'], ax=ax)
ax.set_xlabel("Categoria")
ax.set_ylabel("Número de Inscritos")
ax.grid(axis="y", linestyle="--", alpha=0.7)
st.pyplot(fig)

# Gráfico de cargos mais frequentes
st.subheader("Top 10 Cargos Mais Frequentes")
fig, ax = plt.subplots()
cargo_counts.plot(kind='barh', color='green', ax=ax)
ax.set_xlabel("Número de Inscritos")
ax.set_ylabel("Cargo")
ax.grid(axis="x", linestyle="--", alpha=0.7)
st.pyplot(fig)

# Gráfico de empresas com mais inscritos
st.subheader("Top 10 Empresas com Mais Inscritos")
fig, ax = plt.subplots()
empresa_counts.plot(kind='barh', color='purple', ax=ax)
ax.set_xlabel("Número de Inscritos")
ax.set_ylabel("Empresa")
ax.grid(axis="x", linestyle="--", alpha=0.7)
st.pyplot(fig)

# Gráfico de evolução das inscrições
st.subheader("Evolução das Inscrições ao Longo do Tempo")
fig, ax = plt.subplots()
inscricoes_por_dia.plot(kind='line', marker='o', linestyle='-', ax=ax)
ax.set_xlabel("Data")
ax.set_ylabel("Número de Inscritos")
ax.grid(True, linestyle="--", alpha=0.7)
plt.xticks(rotation=45)
st.pyplot(fig)

st.write("Dashboard gerado com sucesso!")

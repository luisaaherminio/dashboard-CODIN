import streamlit as st
import pandas as pd
import plotly.express as px

# ================= Configuração da Página =================
st.set_page_config(
    page_title="Painel CODIN 2026",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("📊 Painel de Diagnóstico Institucional - CODIN")
st.markdown("**Período:** 22/06/2026 a 07/07/2026 | **Relatório:** Portaria CODIN nº 102/2026")

# ================= Preparação dos Dados (Extraídos do PDF) =================
# 1. KPIs principais
col1, col2, col3, col4 = st.columns(4)
col1.metric("Unidades Avaliadas", "18 / 24", "75,0%")
col2.metric("Respostas ao Formulário", "50", "Colaboradores")
col3.metric("Atribuições Avaliadas", "226", "Total")
col4.metric("Aderência A1/A2", "65,9%", "149 Atribuições")

st.divider()

# 2. Dados de Classificação de Atribuições (A1 - A5)
df_atribuicoes = pd.DataFrame({
    'Classificação': ['A1 Conforme', 'A2 Forma distinta', 'A3 Parcial', 'A4 Não executada', 'A5 Não se aplica'],
    'Quantidade': [122, 27, 19, 42, 16]
})

# 3. Dados de Percepção dos Colaboradores
df_percepcao = pd.DataFrame({
    'Indicador': ['Satisfação no trabalho', 'Conhecimento de normas', 'Clareza das atribuições', 'Infraestrutura/equipamentos'],
    'Nota 4 e 5': [88, 80, 96, 78],
    'Nota 3': [8, 14, 3, 14],
    'Nota 1 e 2': [4, 6, 1, 8]
})

# 4. Dados de Aderência por Unidade
df_unidades = pd.DataFrame({
    'Unidade': [
        'COMUNPRESI', 'DIVCONT', 'SUPFIN', 'SUPCIF', 'SUPVIF', 
        'ASSJUR', 'ASSPRES', 'DIVFIN', 'DIVRHU', 
        'SUPAD', 'SUPIN', 'ASSTIN', 'AGP',
        'DIRAF', 'SUPDIN', 'DIRDI', 'DIRNN', 'DIRIF'
    ],
    'Aderência': [
        100, 100, 100, 100, 100, 
        92, 86, 86, 81, 
        74, 73, 64, 62, 
        36, 29, 25, 11, 11
    ],
    'Classificação': [
        'Alta', 'Alta', 'Alta', 'Alta', 'Alta', 
        'Alta', 'Alta', 'Alta', 'Alta', 
        'Média', 'Média', 'Média', 'Média',
        'Baixa', 'Baixa', 'Baixa', 'Baixa', 'Baixa'
    ]
})

# 5. Dados dos Sinais Estruturais
df_sinais = pd.DataFrame({
    'Sinal Estrutural': ['Regimento percebido como desatualizado', 'Atividade não formalizada', 'Sobreposição sem clareza', 'Função necessária ainda ausente'],
    'Percentual': [42, 34, 22, 30]
})

# 6. Avaliação Geral da Gestão
df_avaliacao_geral = pd.DataFrame({
    'Categoria': ['Excelente', 'Boa', 'Regular', 'Ruim'],
    'Percentual': [10, 48, 32, 10]
})

# ================= Gráficos e Visualizações =================

# Criar layout de duas colunas
coluna_esquerda, coluna_direita = st.columns(2)

with coluna_esquerda:
    st.subheader("🔄 Distribuição das Classificações")
    fig1 = px.pie(df_atribuicoes, values='Quantidade', names='Classificação', 
                   hole=0.5, color_discrete_sequence=px.colors.qualitative.Set2)
    fig1.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(fig1, use_container_width=True)

    st.subheader("📊 Sinais Estruturais Apontados")
    fig5 = px.bar(df_sinais, x='Percentual', y='Sinal Estrutural', orientation='h', 
                   text='Percentual', color='Percentual', color_continuous_scale='Reds')
    fig5.update_traces(texttemplate='%{text:.0f}%', textposition='outside')
    fig5.update_layout(yaxis_title="", xaxis_title="Percentual de Respondentes")
    st.plotly_chart(fig5, use_container_width=True)

with coluna_direita:
    st.subheader("📈 Percepção dos Colaboradores")
    fig2 = px.bar(df_percepcao, x='Indicador', y=['Nota 4 e 5', 'Nota 3', 'Nota 1 e 2'],
                   barmode='stack', title="Notas 1 a 5 (Escala de Satisfação)",
                   color_discrete_map={'Nota 4 e 5': '#2E8B57', 'Nota 3': '#F4A460', 'Nota 1 e 2': '#CD5C5C'})
    fig2.update_layout(legend_title="Notas", yaxis_title="Percentual")
    st.plotly_chart(fig2, use_container_width=True)

    st.subheader("💡 Avaliação Geral da Gestão")
    fig6 = px.pie(df_avaliacao_geral, values='Percentual', names='Categoria', hole=0.5)
    st.plotly_chart(fig6, use_container_width=True)

st.divider()

# Aderência por Unidade (Gráfico de Barras Horizontal)
st.subheader("📌 Aderência Formal Estimada por Unidade")
# Ordenar para melhor visualização
df_unidades_ordenado = df_unidades.sort_values(by='Aderência', ascending=True)

# Definir mapa de cores
color_map = {'Alta': '#2E8B57', 'Média': '#DAA520', 'Baixa': '#CD5C5C'}
fig3 = px.bar(df_unidades_ordenado, x='Aderência', y='Unidade', 
               orientation='h', color='Classificação', color_discrete_map=color_map,
               text='Aderência')
fig3.update_traces(texttemplate='%{text:.0f}%', textposition='outside')
fig3.update_layout(xaxis_range=[0, 105], yaxis_title="", xaxis_title="Aderência (%)")
st.plotly_chart(fig3, use_container_width=True)

st.divider()

# Visão Geral de Riscos e Pendências
st.subheader("⚠️ Riscos e Pendências (Frentes F1/F2)")
col_risco1, col_risco2, col_risco3 = st.columns(3)

with col_risco1:
    st.info("**R1 - Responsabilidade (Accountability)**\n\nDescolamento entre atribuições formais e práticas operacionais.\n\n*Tratamento:* Revisão normativa e rastreabilidade.")
with col_risco2:
    st.warning("**R2 - Continuidade Operacional**\n\nDependência de conhecimento tácito e pessoas-chave.\n\n*Tratamento:* POPs e matriz de substituição.")
with col_risco3:
    st.error("**R4 - Capacidade Institucional**\n\nLimitações de pessoal e ferramentas (46% nota intermediária).\n\n*Tratamento:* Direcionamento à alta administração.")

st.warning("**Pendências (P1 e P2):** 6 unidades ainda não devolveram o levantamento (P1) e os Planos de Ação precisam de monitoramento trimestral (P2).")

st.markdown("---")
st.caption("Fonte: Relatório Unificado de Diagnóstico Institucional - CODIN (Julho/2026) | Dashboard gerado via Streamlit")
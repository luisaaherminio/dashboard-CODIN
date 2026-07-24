import streamlit as st
import plotly.express as px
import plotly.graph_objects as go  # <-- adicionado

# ================= Configuração da Página =================
st.set_page_config(
    page_title="Painel CODIN 2026",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("📊 Painel de Diagnóstico Institucional - CODIN")
st.markdown("**Período:** 22/06/2026 a 07/07/2026 | **Relatório:** Portaria CODIN nº 102/2026")

# ================= KPIs principais =================
col1, col2, col3, col4 = st.columns(4)
col1.metric("Unidades Avaliadas", "18 / 22", "75,0%")
col2.metric("Respostas ao Formulário", "50", "Colaboradores")
col3.metric("Atribuições Avaliadas", "226", "Total")
col4.metric("Aderência A1/A2", "65,9%", "149 Atribuições")

st.divider()

# ================= Dados para os Gráficos (sem Pandas) =================
# 1. Classificação de Atribuições
labels_classif = ['A1 Conforme', 'A2 Forma distinta', 'A3 Parcial', 'A4 Não executada', 'A5 Não se aplica']
values_classif = [122, 27, 19, 42, 16]

# 2. Percepção dos Colaboradores
indicadores = ['Satisfação no trabalho', 'Conhecimento de normas', 'Clareza das atribuições', 'Infraestrutura/equipamentos']
notas_4_5 = [88, 80, 96, 78]
notas_3 = [8, 14, 3, 14]
notas_1_2 = [4, 6, 1, 8]

# 3. Aderência por Unidade
unidades = [
    'COMUNPRESI', 'DIVCONT', 'SUPFIN', 'SUPCIF', 'SUPVIF', 
    'ASSJUR', 'ASSPRES', 'DIVFIN', 'DIVRHU', 
    'SUPAD', 'SUPIN', 'ASSTIN', 'AGP',
    'DIRAF', 'SUPDIN', 'DIRDI', 'DIRNN', 'DIRIF'
]
aderencia = [100, 100, 100, 100, 100, 92, 86, 86, 81, 74, 73, 64, 62, 36, 29, 25, 11, 11]
classif_aderencia = ['Alta']*9 + ['Média']*4 + ['Baixa']*5

# 4. Sinais Estruturais
sinais = ['Regimento percebido como desatualizado', 'Atividade não formalizada', 'Sobreposição sem clareza', 'Função necessária ainda ausente']
perc_sinais = [42, 34, 22, 30]

# 5. Avaliação Geral
cat_avaliacao = ['Excelente', 'Boa', 'Regular', 'Ruim']
perc_avaliacao = [10, 48, 32, 10]

# ================= Exibição dos Gráficos =================
coluna_esquerda, coluna_direita = st.columns(2)

with coluna_esquerda:
    st.subheader("🔄 Distribuição das Classificações")
    fig1 = px.pie(names=labels_classif, values=values_classif, hole=0.5, color_discrete_sequence=px.colors.qualitative.Set2)
    fig1.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(fig1, use_container_width=True)

    st.subheader("📊 Sinais Estruturais Apontados")
    fig5 = px.bar(x=perc_sinais, y=sinais, orientation='h', text=perc_sinais, color=perc_sinais, color_continuous_scale='Reds')
    fig5.update_traces(texttemplate='%{text:.0f}%', textposition='outside')
    fig5.update_layout(yaxis_title="", xaxis_title="Percentual de Respondentes")
    st.plotly_chart(fig5, use_container_width=True)

with coluna_direita:
    st.subheader("📈 Percepção dos Colaboradores")
    # ----- CORREÇÃO AQUI -----
    fig2 = go.Figure()
    fig2.add_trace(go.Bar(x=indicadores, y=notas_4_5, name='Nota 4 e 5', marker_color='#2E8B57'))
    fig2.add_trace(go.Bar(x=indicadores, y=notas_3, name='Nota 3', marker_color='#F4A460'))
    fig2.add_trace(go.Bar(x=indicadores, y=notas_1_2, name='Nota 1 e 2', marker_color='#CD5C5C'))
    fig2.update_layout(
        barmode='stack',
        title="Notas 1 a 5 (Escala de Satisfação)",
        yaxis_title="Percentual",
        xaxis_title="",
        legend_title="Notas"
    )
    st.plotly_chart(fig2, use_container_width=True)
    # -------------------------

    st.subheader("💡 Avaliação Geral da Gestão")
    fig6 = px.pie(names=cat_avaliacao, values=perc_avaliacao, hole=0.5)
    st.plotly_chart(fig6, use_container_width=True)

st.divider()

# Aderência por Unidade (Gráfico de Barras Horizontal)
st.subheader("📌 Aderência Formal Estimada por Unidade")
fig3 = px.bar(x=aderencia, y=unidades, orientation='h', color=classif_aderencia,
               color_discrete_map={'Alta': '#2E8B57', 'Média': '#DAA520', 'Baixa': '#CD5C5C'},
               text=aderencia)
fig3.update_traces(texttemplate='%{text:.0f}%', textposition='outside')
fig3.update_layout(xaxis_range=[0, 105], yaxis_title="", xaxis_title="Aderência (%)")
st.plotly_chart(fig3, use_container_width=True)

st.divider()

# Riscos e Pendências
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
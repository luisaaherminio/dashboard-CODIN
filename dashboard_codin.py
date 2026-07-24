import streamlit as st
import pandas as pd
import plotly.express as px
import os # Importante para verificar arquivos

# --- 1. CONFIGURAÇÃO DA PÁGINA E ESTILO ---
st.set_page_config(
    page_title="Painel de Governança - CODIN",
    page_icon="🏛️",
    layout="wide"
)

# Estilo CSS
st.markdown("""
<style>
    .stApp { background-color: #0E1117; color: #E0E0E0; }
    h1, h2, h3, h4 { color: #FFD700 !important; }
    .kpi-card {
        background-color: #1A1F2E;
        border: 1px solid #FFA500;
        border-radius: 10px;
        padding: 15px;
        text-align: center;
        box-shadow: 0 4px 6px rgba(255, 165, 0, 0.1);
    }
    .kpi-title { font-size: 14px; color: #A0A0A0; margin-bottom: 5px; }
    .kpi-value { font-size: 28px; font-weight: bold; color: #FFD700; }
    div[data-testid="stVerticalBlockBorderWrapper"] {
        border: 1px solid #FFA500 !important;
        background-color: #1A1F2E;
        border-radius: 12px;
        padding: 15px;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

# --- 2. CARREGAMENTO DOS LOGOTIPOS (SOLUÇÃO ROBUSTA) ---
col_logo1, col_title, col_logo2 = st.columns([1, 3, 1])

def exibir_logo(col, nome_base, largura):
    # Função que procura extensões diferentes (png, jpg, jpeg) independente de maiúsculas/minúsculas
    possiveis_extensoes = ['.png', '.jpg', '.jpeg', '.PNG', '.JPG', '.JPEG']
    encontrado = False
    with col:
        for ext in possiveis_extensoes:
            arquivo = f"{nome_base}{ext}"
            if os.path.exists(arquivo):
                st.image(arquivo, width=largura)
                encontrado = True
                break
        if not encontrado:
            st.warning(f"Logo {nome_base} não encontrada. Verifique se o nome é '{nome_base}.png' ou '.jpg'")

exibir_logo(col_logo1, "codin_logo", 150)

with col_title:
    st.markdown("<h1 style='text-align: center;'>Diretoria de Governança, Controle e Conformidade</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center; color: #FFA500;'>Painel de Acompanhamento de Colegiados - 2026</h4>", unsafe_allow_html=True)

exibir_logo(col_logo2, "governanca_logo", 250)

st.divider()

# --- 3. CRIAÇÃO DOS DATAFRAMES COM OS DADOS ---
data_governanca = {
    "Colegiado": ["Assembleia Geral", "Conselho de Administração", "Diretoria Executiva", "Conselho Fiscal", "Comitê de Auditoria", "Comitê de Elegibilidade"],
    "Reuniões": [1, 6, 3, 7, 0, 6],
    "Membros com Mandato Vencido": ["Não se aplica", "Sim", "Não", "Sim", "Não", "Não"],
    "Nomeações em Andamento": ["Não", "Sim", "Não", "Sim", "Não", "Não"],
    "Vacâncias": [0, 1, 0, 1, 0, 0], 
    "Capacitações": [0, 1, 1, 0, 0, 0]
}
df_governanca = pd.DataFrame(data_governanca)

data_colegiados = {
    "Colegiado": ["Assembleia Geral", "Conselho de Administração", "Diretoria Executiva", "Conselho Fiscal", "Comitê de Auditoria", "Comitê de Elegibilidade"],
    "Convocacao": [
        "Conselho de Administração (regra geral). Subsidiariamente: Diretoria, Conselho Fiscal ou acionistas, nas hipóteses admitidas em lei (ES, Art. 12).",
        "Convocação pelo Presidente ou por dois conselheiros, com antecedência mínima de 5 dias.",
        "Convocação pelo Diretor-Presidente ou por três Diretores.",
        "Convocação pelo Conselheiro Presidente.",
        "Não aplicável / Definição pelo Conselho de Administração.",
        "Convocação pelo seu Presidente, ou dois de seus membros, por intermédio da Chefia de Gabinete, com antecedência mínima de 07 dias."
    ],
    "Natureza": [
        "Órgão máximo de deliberação da Companhia.",
        "Órgão colegiado de orientação estratégica e supervisão.",
        "Órgão executivo responsável pela administração da Companhia.",
        "Órgão permanente de fiscalização.",
        "Órgão de assessoramento ao Conselho de Administração.",
        "Órgão de assessoramento responsável pela análise de elegibilidade."
    ],
    "Composicao_Resumo": [
        "Acionistas com direito a voto.",
        "3 membros (SEDEICS, SEFAZ, Minoritários).",
        "Diretor-Presidente e até 5 Diretores.",
        "2 Efetivos + Suplentes.",
        "3 membros independentes.",
        "3 membros (empregados ou conselheiros)."
    ],
    "Periodicidade": [
        "Anual (até 30/04) e Extraordinária.",
        "Trimestral e Extraordinária.",
        "Bimestral e Extraordinária.",
        "Mensal e Extraordinária.",
        "Bimestral.",
        "Conforme necessidade."
    ],
    "Data_Ultima_Reuniao": [
        "20/07/2026",
        "03/07/2026",
        "07/07/2026",
        "25/06/2026",
        "N/A",
        "20/05/2026"
    ],
    "Membros_Atuais": [
        "SECC, CEHAB, IVB",
        "THOMPSON LEMOS, ANDERSON CARLOS, JORGE LUIZ, LUIZ CLAUDIO",
        "Leonardo da Silva Morais, João Marcos Gomes de Pinho",
        "Gabriel Mac-Dowell Blum, Francisco Pereira Iglesias, Reginaldo Jardim",
        "Em definição/Indicados",
        "Carla Amanda, Carla Pereira, Maria Izete de Oliveira"
    ],
    "Base_Legal": [
        "Lei 6404/1976, Lei 13303/2016, art 8º ES",
        "Lei 6404/1976, Lei 13303/2016, art 33º ES",
        "Lei 6404/1976, Lei 13303/2016, art 41º ES",
        "Lei 6404/1976, Lei 13303/2016, Decreto 45188/2017",
        "Lei 13303/2016, Decreto 45188/2017, art 62º ES",
        "arts. 156 e 165 Lei 6404/1976 e art. 69 ES"
    ],
    "Processo_SEI": [
        "SEI-220003/001002/2026",
        "SEI-220010/000165/2023",
        "SEI-150001/005343/2026",
        "SEI-220010/000165/2023",
        "N/A",
        "SEI-220010/000297/2022"
    ]
}
df_colegiados = pd.DataFrame(data_colegiados)

# --- 4. MÉTRICAS (KPIs) ---
st.markdown("### 📊 Indicadores de Governança e Conformidade")
total_reunioes = df_governanca['Reuniões'].sum()
total_vacancias = df_governanca['Vacâncias'].sum()
colegiados_com_mandato = df_governanca[df_governanca['Membros com Mandato Vencido'] == 'Sim'].shape[0]
colegiados_com_nomeacoes = df_governanca[df_governanca['Nomeações em Andamento'] == 'Sim'].shape[0]

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown(f"""<div class="kpi-card"><div class="kpi-title">Total de Reuniões (2026)</div><div class="kpi-value">{total_reunioes}</div></div>""", unsafe_allow_html=True)
with col2:
    st.markdown(f"""<div class="kpi-card"><div class="kpi-title">Colegiados c/ Mandato Vencido</div><div class="kpi-value" style="color: #FF4500;">{colegiados_com_mandato}</div></div>""", unsafe_allow_html=True)
with col3:
    st.markdown(f"""<div class="kpi-card"><div class="kpi-title">Nomeações em Andamento</div><div class="kpi-value" style="color: #FFD700;">{colegiados_com_nomeacoes}</div></div>""", unsafe_allow_html=True)
with col4:
    st.markdown(f"""<div class="kpi-card"><div class="kpi-title">Vacâncias Ativas</div><div class="kpi-value" style="color: #FFA500;">{total_vacancias}</div></div>""", unsafe_allow_html=True)

st.divider()

# --- 5. GRÁFICOS ---
col_grafico1, col_grafico2 = st.columns(2)
with col_grafico1:
    fig_reunioes = px.bar(df_governanca, x="Colegiado", y="Reuniões", title="Reuniões Realizadas", color="Reuniões", color_continuous_scale=["#FFA500", "#FFD700"], text="Reuniões")
    fig_reunioes.update_layout(plot_bgcolor="#0E1117", paper_bgcolor="#0E1117", font_color="#E0E0E0", title_font_color="#FFD700")
    fig_reunioes.update_traces(textposition='outside')
    st.plotly_chart(fig_reunioes, use_container_width=True)

with col_grafico2:
    df_melted = df_governanca.melt(id_vars=["Colegiado"], value_vars=["Capacitações", "Reuniões"])
    fig_conv = px.bar(df_melted, x="Colegiado", y="value", color="variable", barmode="group", title="Capacitações vs Reuniões", color_discrete_map={"Capacitações": "#FFD700", "Reuniões": "#FFA500"})
    fig_conv.update_layout(plot_bgcolor="#0E1117", paper_bgcolor="#0E1117", font_color="#E0E0E0", title_font_color="#FFD700", legend_font_color="#E0E0E0")
    st.plotly_chart(fig_conv, use_container_width=True)

st.divider()

# --- 6. BLOCOS (CARTÕES) DE TODOS OS COLEGIADOS ---
st.markdown("### 🏛️ Detalhamento de Todos os Colegiados")

for index, row in df_colegiados.iterrows():
    status_row = df_governanca[df_governanca['Colegiado'] == row['Colegiado']].iloc[0]
    
    with st.container(border=True):
        st.markdown(f"<h3 style='color: #FFD700; margin-bottom: 0px;'>{row['Colegiado']}</h3>", unsafe_allow_html=True)
        st.caption(f"Status: {status_row['Membros com Mandato Vencido']} (Mandato) | {status_row['Nomeações em Andamento']} (Nomeações) | {status_row['Capacitações']} (Capacitações)")
        st.markdown("---")
        
        c1, c2 = st.columns(2)
        
        with c1:
            st.markdown(f"**📌 Natureza:**\n\n{row['Natureza']}")
            st.markdown(f"**👥 Composição:**\n\n{row['Composicao_Resumo']}")
            st.markdown(f"**📅 Periodicidade:** {row['Periodicidade']}")
            st.markdown(f"**📨 Convocação:** {row['Convocacao']}") 
        
        with c2:
            st.markdown(f"**📜 Base Legal:**\n\n{row['Base_Legal']}")
            st.markdown(f"**🆔 Processo SEI:** `{row['Processo_SEI']}`")
            st.markdown(f"**👤 Membros Atuais:**\n\n{row['Membros_Atuais']}")
        
        st.markdown(f"**📊 Reuniões realizadas no exercício:** {status_row['Reuniões']}")
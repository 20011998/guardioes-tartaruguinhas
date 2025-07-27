import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import numpy as np

# Import custom components
from components.dashboard import render_dashboard
from components.nest_form import render_nest_form
from components.reports import render_reports
from components.statistics_view import render_statistics
from utils.data_handler import load_data, save_data, get_nest_data
from utils.statistics import *

# Configure page
st.set_page_config(
    page_title="🐢 Guardiões das Tartaruguinhas",
    page_icon="🐢",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load custom CSS
def load_css():
    with open("assets/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Initialize session state
if 'nest_data' not in st.session_state:
    st.session_state.nest_data = get_nest_data()

def main():
    # Load custom styling
    load_css()
    
    # Header with ocean theme
    st.markdown("""
    <div class="main-header">
        <h1>🐢 Guardiões das Tartaruguinhas</h1>
        <p>🌊 Sistema de Monitoramento de Ninhos de Tartarugas Marinhas 🌊</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Sidebar navigation with ocean icons
    st.sidebar.markdown("""
    <div class="sidebar-header">
        <h2>🧭 Navegação</h2>
    </div>
    """, unsafe_allow_html=True)
    
    menu_options = {
        "🏖️ Dashboard Principal": "dashboard",
        "📊 Estatísticas": "statistics", 
        "➕ Adicionar Ninho": "add_nest",
        "📋 Relatório Completo": "reports"
    }
    
    selected_page = st.sidebar.selectbox(
        "Selecione uma seção:",
        list(menu_options.keys()),
        index=0
    )
    
    # Quick stats in sidebar
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 📈 Resumo Rápido")
    
    total_nests = len(st.session_state.nest_data)
    high_risk = sum(1 for nest in st.session_state.nest_data if nest['risco'] == '🔴')
    hatching_soon = ninhos_prestes_a_eclodir(st.session_state.nest_data)
    
    st.sidebar.metric("Total de Ninhos", total_nests)
    st.sidebar.metric("🔴 Alto Risco", high_risk)
    st.sidebar.metric("🐣 Eclosão em ≤5 dias", hatching_soon)
    
    # Render selected page
    page_key = menu_options[selected_page]
    
    if page_key == "dashboard":
        render_dashboard(st.session_state.nest_data)
    elif page_key == "statistics":
        render_statistics(st.session_state.nest_data)
    elif page_key == "add_nest":
        render_nest_form()
    elif page_key == "reports":
        render_reports(st.session_state.nest_data)

if __name__ == "__main__":
    main()

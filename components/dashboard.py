import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from utils.statistics import *

def render_dashboard(nest_data):
    """Render the main dashboard with overview and nest cards"""
    
    # Critical alerts section
    render_alerts(nest_data)
    
    # Key metrics
    render_key_metrics(nest_data)
    
    # Charts section
    col1, col2 = st.columns(2)
    
    with col1:
        render_risk_distribution(nest_data)
        
    with col2:
        render_region_distribution(nest_data)
    
    # Nest cards grid
    st.markdown("---")
    st.markdown("## 🏖️ Ninhos por Região")
    
    render_nest_cards(nest_data)

def render_alerts(nest_data):
    """Render critical alerts"""
    hatching_soon = [n for n in nest_data if n['dias_para_eclosao'] <= 2]
    critical_risk = [n for n in nest_data if n['risco'] == '🔴']
    
    if hatching_soon or critical_risk:
        st.markdown("### 🚨 Alertas Críticos")
        
        if hatching_soon:
            st.error(f"⏰ {len(hatching_soon)} ninho(s) prestes a eclodir em ≤2 dias!")
            
        if critical_risk:
            st.error(f"🔴 {len(critical_risk)} ninho(s) em risco crítico necessitam atenção imediata!")

def render_key_metrics(nest_data):
    """Render key metrics in columns"""
    st.markdown("### 📊 Métricas Principais")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        total_nests = len(nest_data)
        st.metric(
            label="🐢 Total de Ninhos",
            value=total_nests
        )
    
    with col2:
        total_eggs = get_total_ovos(nest_data)
        st.metric(
            label="🥚 Total de Ovos",
            value=f"{total_eggs:,}"
        )
    
    with col3:
        hatching_soon = ninhos_prestes_a_eclodir(nest_data)
        st.metric(
            label="🐣 Eclosão em ≤5 dias",
            value=hatching_soon,
            delta="Prioridade Alta" if hatching_soon > 0 else None
        )
    
    with col4:
        with_predators = sum(1 for n in nest_data if n['predadores'])
        st.metric(
            label="🦅 Com Predadores",
            value=with_predators,
            delta="Atenção" if with_predators > 0 else None
        )

def render_risk_distribution(nest_data):
    """Render risk distribution chart"""
    st.markdown("#### 🚦 Distribuição por Nível de Risco")
    
    risk_counts = {"🟢": 0, "🟡": 0, "🔴": 0}
    for nest in nest_data:
        risk_counts[nest['risco']] += 1
    
    colors = ['#4CAF50', '#FFC107', '#F44336']
    
    fig = go.Figure(data=[
        go.Pie(
            labels=['🟢 Baixo', '🟡 Médio', '🔴 Alto'],
            values=list(risk_counts.values()),
            marker_colors=colors,
            hole=0.4
        )
    ])
    
    fig.update_layout(
        showlegend=True,
        height=300,
        margin=dict(t=0, b=0, l=0, r=0)
    )
    
    st.plotly_chart(fig, use_container_width=True)

def render_region_distribution(nest_data):
    """Render region distribution chart"""
    st.markdown("#### 🏖️ Ninhos por Região")
    
    region_counts = contar_ninhos_por_regiao(nest_data)
    
    fig = px.bar(
        x=list(region_counts.keys()),
        y=list(region_counts.values()),
        color=list(region_counts.values()),
        color_continuous_scale='Blues'
    )
    
    fig.update_layout(
        xaxis_title="Região",
        yaxis_title="Número de Ninhos",
        showlegend=False,
        height=300
    )
    
    st.plotly_chart(fig, use_container_width=True)

def render_nest_cards(nest_data):
    """Render nest cards in a grid layout"""
    # Group nests by region
    regions = {}
    for nest in nest_data:
        region = nest['regiao']
        if region not in regions:
            regions[region] = []
        regions[region].append(nest)
    
    for region, nests in regions.items():
        st.markdown(f"### 🏖️ {region}")
        
        # Create columns for nest cards
        cols = st.columns(min(3, len(nests)))
        
        for i, nest in enumerate(nests):
            with cols[i % 3]:
                render_nest_card(nest, i + 1)

def render_nest_card(nest, nest_id):
    """Render individual nest card"""
    risk_color = {
        '🟢': '#4CAF50',
        '🟡': '#FFC107', 
        '🔴': '#F44336'
    }
    
    status_icon = {
        'intacto': '✅',
        'ameacado': '⚠️',
        'danificado': '❌'
    }
    
    predator_icon = '🦅' if nest['predadores'] else '🕊️'
    
    # Get guardian name
    guardian_name = nest.get('guardiao', 'Guardião não identificado')
    
    # Card styling with risk color border and gray background
    card_style = f"""
    <div style="
        border: 3px solid {risk_color[nest['risco']]};
        border-radius: 10px;
        padding: 15px;
        margin: 10px 0;
        background: linear-gradient(135deg, #F5F5F5 0%, #E0E0E0 100%);
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    ">
        <h4 style="margin: 0; color: #0D47A1; font-weight: 600;">🐢 Ninho #{nest_id}</h4>
        <p style="margin: 3px 0; color: #0D47A1; font-size: 0.9em;"><strong>👤 Guardião:</strong> {guardian_name}</p>
        <p style="margin: 5px 0; color: #0D47A1;"><strong>🥚 Ovos:</strong> {nest['quantidade_ovos']}</p>
        <p style="margin: 5px 0; color: #0D47A1;"><strong>Status:</strong> {status_icon[nest['status']]} {nest['status'].title()}</p>
        <p style="margin: 5px 0; color: #0D47A1;"><strong>Risco:</strong> {nest['risco']}</p>
        <p style="margin: 5px 0; color: #0D47A1;"><strong>🐣 Eclosão:</strong> {nest['dias_para_eclosao']} dias</p>
        <p style="margin: 5px 0; color: #0D47A1;"><strong>Predadores:</strong> {predator_icon}</p>
    </div>
    """
    
    st.markdown(card_style, unsafe_allow_html=True)

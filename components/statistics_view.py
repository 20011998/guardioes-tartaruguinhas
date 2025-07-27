import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from utils.statistics import *

def render_statistics(nest_data):
    """Render comprehensive statistics view"""
    
    st.markdown("## 📊 Estatísticas Avançadas")
    st.markdown("### 🌊 Análise Detalhada dos Dados de Monitoramento")
    
    # Key statistics overview
    render_statistics_overview(nest_data)
    
    # Charts section
    render_advanced_charts(nest_data)
    
    # Detailed analytics
    render_detailed_analytics(nest_data)

def render_statistics_overview(nest_data):
    """Render key statistics overview"""
    
    st.markdown("### 📈 Resumo Estatístico")
    
    # Calculate key metrics
    total_nests = contar_total_ninhos(nest_data)
    total_eggs = get_total_ovos(nest_data)
    avg_eggs = total_eggs / total_nests if total_nests > 0 else 0
    hatching_soon = ninhos_prestes_a_eclodir(nest_data)
    region_risk, risk_count = regiao_com_mais_ninhos_sob_risco(nest_data)
    predator_damage = ninhos_com_predadores_e_danificados(nest_data)
    
    # Display metrics in columns
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("🐢 Total de Ninhos", total_nests)
        st.metric("🥚 Total de Ovos", f"{total_eggs:,}")
        
    with col2:
        st.metric("📊 Média Ovos/Ninho", f"{avg_eggs:.1f}")
        st.metric("🐣 Eclosão ≤ 5 dias", hatching_soon)
        
    with col3:
        st.metric("🚨 Região Mais Crítica", region_risk)
        st.metric("⚠️ Ninhos Críticos", risk_count)

def render_advanced_charts(nest_data):
    """Render advanced statistical charts"""
    
    st.markdown("---")
    st.markdown("### 📊 Visualizações Avançadas")
    
    # Create tabs for different chart categories
    tab1, tab2, tab3, tab4 = st.tabs(["🚦 Análise de Risco", "🏖️ Análise Regional", "🐣 Cronograma de Eclosão", "🦅 Análise de Predadores"])
    
    with tab1:
        render_risk_analysis_charts(nest_data)
    
    with tab2:
        render_regional_analysis_charts(nest_data)
    
    with tab3:
        render_hatching_timeline_charts(nest_data)
    
    with tab4:
        render_predator_analysis_charts(nest_data)

def render_risk_analysis_charts(nest_data):
    """Render risk analysis charts"""
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 🚦 Distribuição de Risco vs Status")
        
        # Create risk vs status matrix
        risk_status_data = []
        for nest in nest_data:
            risk_status_data.append({
                'risco': nest['risco'],
                'status': nest['status'],
                'quantidade_ovos': nest['quantidade_ovos']
            })
        
        df_risk_status = pd.DataFrame(risk_status_data)
        
        # Create heatmap
        pivot_table = df_risk_status.pivot_table(
            index='risco', 
            columns='status', 
            values='quantidade_ovos', 
            aggfunc='count', 
            fill_value=0
        )
        
        fig = px.imshow(
            pivot_table.values,
            labels=dict(x="Status", y="Risco", color="Número de Ninhos"),
            x=pivot_table.columns,
            y=pivot_table.index,
            color_continuous_scale='Reds'
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("#### 📊 Média de Ovos por Nível de Risco")
        
        risk_avg_eggs = media_ovos_por_risco(nest_data)
        
        fig = go.Figure(data=[
            go.Bar(
                x=list(risk_avg_eggs.keys()),
                y=list(risk_avg_eggs.values()),
                marker_color=['#4CAF50', '#FFC107', '#F44336']
            )
        ])
        
        fig.update_layout(
            xaxis_title="Nível de Risco",
            yaxis_title="Média de Ovos",
            showlegend=False
        )
        
        st.plotly_chart(fig, use_container_width=True)

def render_regional_analysis_charts(nest_data):
    """Render regional analysis charts"""
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 🏖️ Ninhos por Região")
        
        region_counts = contar_ninhos_por_regiao(nest_data)
        
        fig = px.pie(
            values=list(region_counts.values()),
            names=list(region_counts.keys()),
            color_discrete_sequence=px.colors.qualitative.Set3
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("#### 📊 Total de Ovos por Região")
        
        region_eggs = {}
        for nest in nest_data:
            region = nest['regiao']
            region_eggs[region] = region_eggs.get(region, 0) + nest['quantidade_ovos']
        
        fig = px.bar(
            x=list(region_eggs.keys()),
            y=list(region_eggs.values()),
            color=list(region_eggs.values()),
            color_continuous_scale='Blues'
        )
        
        fig.update_layout(
            xaxis_title="Região",
            yaxis_title="Total de Ovos",
            showlegend=False
        )
        
        st.plotly_chart(fig, use_container_width=True)

def render_hatching_timeline_charts(nest_data):
    """Render hatching timeline analysis"""
    
    st.markdown("#### 🐣 Cronograma de Eclosão")
    
    # Group nests by hatching days
    hatching_groups = {
        'Imediato (≤2 dias)': [],
        'Próximo (3-5 dias)': [],
        'Curto prazo (6-15 dias)': [],
        'Médio prazo (16-30 dias)': [],
        'Longo prazo (>30 dias)': []
    }
    
    for nest in nest_data:
        days = nest['dias_para_eclosao']
        if days <= 2:
            hatching_groups['Imediato (≤2 dias)'].append(nest)
        elif days <= 5:
            hatching_groups['Próximo (3-5 dias)'].append(nest)
        elif days <= 15:
            hatching_groups['Curto prazo (6-15 dias)'].append(nest)
        elif days <= 30:
            hatching_groups['Médio prazo (16-30 dias)'].append(nest)
        else:
            hatching_groups['Longo prazo (>30 dias)'].append(nest)
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Timeline bar chart
        timeline_counts = {k: len(v) for k, v in hatching_groups.items()}
        
        fig = px.bar(
            x=list(timeline_counts.values()),
            y=list(timeline_counts.keys()),
            orientation='h',
            color=list(timeline_counts.values()),
            color_continuous_scale='RdYlGn_r'
        )
        
        fig.update_layout(
            xaxis_title="Número de Ninhos",
            yaxis_title="Período de Eclosão",
            showlegend=False
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Scatter plot: Days to hatch vs Number of eggs
        df_scatter = pd.DataFrame(nest_data)
        
        fig = px.scatter(
            df_scatter,
            x='dias_para_eclosao',
            y='quantidade_ovos',
            color='risco',
            size='quantidade_ovos',
            hover_data=['regiao', 'status'],
            color_discrete_map={'🟢': '#4CAF50', '🟡': '#FFC107', '🔴': '#F44336'}
        )
        
        fig.update_layout(
            xaxis_title="Dias para Eclosão",
            yaxis_title="Quantidade de Ovos"
        )
        
        st.plotly_chart(fig, use_container_width=True)

def render_predator_analysis_charts(nest_data):
    """Render predator analysis charts"""
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 🦅 Presença de Predadores por Status")
        
        predator_status_data = []
        for nest in nest_data:
            predator_status_data.append({
                'status': nest['status'],
                'predadores': 'Com Predadores' if nest['predadores'] else 'Sem Predadores',
                'count': 1
            })
        
        df_predator = pd.DataFrame(predator_status_data)
        predator_pivot = df_predator.pivot_table(
            index='status',
            columns='predadores',
            values='count',
            aggfunc='sum',
            fill_value=0
        )
        
        fig = px.bar(
            predator_pivot,
            barmode='group',
            color_discrete_map={
                'Com Predadores': '#F44336',
                'Sem Predadores': '#4CAF50'
            }
        )
        
        fig.update_layout(
            xaxis_title="Status do Ninho",
            yaxis_title="Número de Ninhos"
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("#### 📊 Impacto dos Predadores")
        
        # Calculate predator impact statistics
        with_predators = [n for n in nest_data if n['predadores']]
        without_predators = [n for n in nest_data if not n['predadores']]
        
        predator_stats = {
            'Categoria': ['Com Predadores', 'Sem Predadores'],
            'Quantidade': [len(with_predators), len(without_predators)],
            'Média de Ovos': [
                sum(n['quantidade_ovos'] for n in with_predators) / len(with_predators) if with_predators else 0,
                sum(n['quantidade_ovos'] for n in without_predators) / len(without_predators) if without_predators else 0
            ],
            'Ninhos Danificados': [
                sum(1 for n in with_predators if n['status'] == 'danificado'),
                sum(1 for n in without_predators if n['status'] == 'danificado')
            ]
        }
        
        df_stats = pd.DataFrame(predator_stats)
        
        fig = make_subplots(
            rows=1, cols=2,
            subplot_titles=('Quantidade de Ninhos', 'Ninhos Danificados'),
            specs=[[{"type": "bar"}, {"type": "bar"}]]
        )
        
        fig.add_trace(
            go.Bar(x=df_stats['Categoria'], y=df_stats['Quantidade'], name='Total'),
            row=1, col=1
        )
        
        fig.add_trace(
            go.Bar(x=df_stats['Categoria'], y=df_stats['Ninhos Danificados'], name='Danificados'),
            row=1, col=2
        )
        
        fig.update_layout(showlegend=False)
        
        st.plotly_chart(fig, use_container_width=True)

def render_detailed_analytics(nest_data):
    """Render detailed analytics section"""
    
    st.markdown("---")
    st.markdown("### 🔍 Análises Detalhadas")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 📊 Estatísticas por Categoria")
        
        # Status distribution
        status_counts = contar_ninhos_por_status(nest_data)
        st.write("**Distribuição por Status:**")
        for status, count in status_counts.items():
            percentage = (count / len(nest_data)) * 100
            st.write(f"- {status.title()}: {count} ({percentage:.1f}%)")
        
        # Risk distribution
        risk_counts = {"🟢": 0, "🟡": 0, "🔴": 0}
        for nest in nest_data:
            risk_counts[nest['risco']] += 1
        
        st.write("**Distribuição por Risco:**")
        risk_labels = {"🟢": "Baixo", "🟡": "Médio", "🔴": "Alto"}
        for risk, count in risk_counts.items():
            percentage = (count / len(nest_data)) * 100
            st.write(f"- {risk} {risk_labels[risk]}: {count} ({percentage:.1f}%)")
    
    with col2:
        st.markdown("#### 🎯 Indicadores de Performance")
        
        # Calculate performance indicators
        total_eggs = get_total_ovos(nest_data)
        avg_eggs = total_eggs / len(nest_data)
        critical_ratio = sum(1 for n in nest_data if n['risco'] == '🔴') / len(nest_data) * 100
        predator_ratio = sum(1 for n in nest_data if n['predadores']) / len(nest_data) * 100
        
        st.metric("📊 Média de Ovos por Ninho", f"{avg_eggs:.1f}")
        st.metric("🚨 Taxa de Risco Crítico", f"{critical_ratio:.1f}%")
        st.metric("🦅 Taxa de Presença de Predadores", f"{predator_ratio:.1f}%")
        
        # Efficiency indicator
        intact_ratio = sum(1 for n in nest_data if n['status'] == 'intacto') / len(nest_data) * 100
        st.metric("✅ Taxa de Ninhos Intactos", f"{intact_ratio:.1f}%")

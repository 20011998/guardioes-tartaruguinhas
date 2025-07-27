import streamlit as st
import pandas as pd
from datetime import datetime
from utils.statistics import *

def render_reports(nest_data):
    """Render comprehensive reports view"""
    
    st.markdown("## 📋 Relatório Completo dos Ninhos")
    st.markdown("### 🌊 Análise Detalhada de Todos os Ninhos Registrados")
    
    # Generate report summary
    render_report_summary(nest_data)
    
    # Filter options
    render_filters(nest_data)
    
    # Detailed nest table
    render_detailed_table(nest_data)
    
    # Export options
    render_export_options(nest_data)

def render_report_summary(nest_data):
    """Render report summary statistics"""
    
    st.markdown("### 📊 Resumo Executivo")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        total_nests = len(nest_data)
        st.metric("🐢 Total de Ninhos", total_nests)
    
    with col2:
        total_eggs = sum(nest['quantidade_ovos'] for nest in nest_data)
        st.metric("🥚 Total de Ovos", f"{total_eggs:,}")
    
    with col3:
        avg_eggs = total_eggs / total_nests if total_nests > 0 else 0
        st.metric("📈 Média de Ovos/Ninho", f"{avg_eggs:.1f}")
    
    with col4:
        critical_nests = sum(1 for nest in nest_data if nest['risco'] == '🔴')
        st.metric("🚨 Ninhos Críticos", critical_nests)

def render_filters(nest_data):
    """Render filter options for the report"""
    
    st.markdown("---")
    st.markdown("### 🔍 Filtros de Visualização")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        regions = ["Todas"] + list(set(nest['regiao'] for nest in nest_data))
        selected_region = st.selectbox("🏖️ Filtrar por Região", regions)
    
    with col2:
        statuses = ["Todos"] + ["intacto", "ameacado", "danificado"]
        selected_status = st.selectbox("📊 Filtrar por Status", statuses)
    
    with col3:
        risks = ["Todos"] + ["🟢", "🟡", "🔴"]
        selected_risk = st.selectbox("🚦 Filtrar por Risco", risks)
    
    # Apply filters
    filtered_data = nest_data.copy()
    
    if selected_region != "Todas":
        filtered_data = [n for n in filtered_data if n['regiao'] == selected_region]
    
    if selected_status != "Todos":
        filtered_data = [n for n in filtered_data if n['status'] == selected_status]
    
    if selected_risk != "Todos":
        filtered_data = [n for n in filtered_data if n['risco'] == selected_risk]
    
    st.session_state.filtered_nest_data = filtered_data

def render_detailed_table(nest_data):
    """Render detailed table of all nests"""
    
    filtered_data = getattr(st.session_state, 'filtered_nest_data', nest_data)
    
    st.markdown("---")
    st.markdown(f"### 📋 Detalhes dos Ninhos ({len(filtered_data)} registros)")
    
    if not filtered_data:
        st.warning("🔍 Nenhum ninho encontrado com os filtros aplicados.")
        return
    
    # Convert to DataFrame for better display
    df = pd.DataFrame(filtered_data)
    
    # Rename columns for better presentation
    column_names = {
        'regiao': '🏖️ Região',
        'quantidade_ovos': '🥚 Ovos',
        'status': '📊 Status',
        'risco': '🚦 Risco',
        'dias_para_eclosao': '🐣 Dias p/ Eclosão',
        'predadores': '🦅 Predadores',
        'guardiao': '👤 Guardião'
    }
    
    df = df.rename(columns=column_names)
    
    # Format predadores column
    df['🦅 Predadores'] = df['🦅 Predadores'].map({True: '✅ Sim', False: '❌ Não'})
    
    # Style the dataframe with better formatting
    styled_df = df.style.apply(style_risk_rows, axis=1).format({
        '🥚 Ovos': '{:,}',
        '🐣 Dias p/ Eclosão': '{} dias'
    })
    
    # Add custom CSS for the dataframe
    st.markdown("""
    <style>
    .stDataFrame table {
        border-collapse: separate !important;
        border-spacing: 2px !important;
    }
    
    .stDataFrame tbody tr {
        border-radius: 8px !important;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.dataframe(
        styled_df,
        use_container_width=True,
        hide_index=True
    )
    
    # Show individual nest details
    render_nest_details(filtered_data)

def style_risk_rows(row):
    """Style rows based on risk level with proper contrast"""
    risk = row['🚦 Risco']
    if risk == '🔴':
        return ['background-color: #F44336; color: white; font-weight: 500'] * len(row)
    elif risk == '🟡':
        return ['background-color: #FFC107; color: white; font-weight: 500'] * len(row)
    elif risk == '🟢':
        return ['background-color: #4CAF50; color: white; font-weight: 500'] * len(row)
    return ['background-color: #E0E0E0; color: #212121'] * len(row)

def render_nest_details(filtered_data):
    """Render expandable details for each nest"""
    
    st.markdown("---")
    st.markdown("### 🔍 Detalhes Individuais dos Ninhos")
    
    for i, nest in enumerate(filtered_data, 1):
        # Define risk colors and background
        risk_colors = {
            '🟢': '#4CAF50',
            '🟡': '#FFC107', 
            '🔴': '#F44336'
        }
        
        risk_bg = risk_colors.get(nest['risco'], '#4CAF50')
        
        # Create custom styled container
        nest_detail_html = f"""
        <div style="
            background: {risk_bg};
            color: white;
            padding: 20px;
            border-radius: 15px;
            margin: 10px 0;
            box-shadow: 0 4px 12px rgba(0,0,0,0.2);
        ">
            <h4 style="margin: 0 0 15px 0; color: white; font-weight: 700;">🐢 Ninho #{i} - {nest['regiao']} ({nest['risco']})</h4>
            <p style="margin: 8px 0; color: white; font-weight: 600; border-bottom: 1px solid rgba(255,255,255,0.3); padding-bottom: 8px;"><strong>👤 Guardião:</strong> {nest.get('guardiao', 'Guardião não identificado')}</p>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">
                <div>
                    <p style="margin: 8px 0; color: white;"><strong>🏖️ Região:</strong> {nest['regiao']}</p>
                    <p style="margin: 8px 0; color: white;"><strong>🥚 Quantidade de Ovos:</strong> {nest['quantidade_ovos']}</p>
                    <p style="margin: 8px 0; color: white;"><strong>📊 Status:</strong> {nest['status'].title()}</p>
                </div>
                <div>
                    <p style="margin: 8px 0; color: white;"><strong>🚦 Nível de Risco:</strong> {nest['risco']}</p>
                    <p style="margin: 8px 0; color: white;"><strong>🐣 Dias para Eclosão:</strong> {nest['dias_para_eclosao']}</p>
                    <p style="margin: 8px 0; color: white;"><strong>🦅 Predadores:</strong> {'Sim' if nest['predadores'] else 'Não'}</p>
                </div>
            </div>
        """
        
        # Add observations if available
        if 'observacoes' in nest:
            nest_detail_html += f'<p style="margin: 15px 0 0 0; color: white;"><strong>📝 Observações:</strong> {nest["observacoes"]}</p>'
        
        nest_detail_html += "</div>"
        
        st.markdown(nest_detail_html, unsafe_allow_html=True)
        
        # Risk assessment with custom styling
        render_nest_risk_assessment_custom(nest)

def render_nest_risk_assessment_custom(nest):
    """Render custom styled risk assessment for individual nest"""
    
    risk_level = nest['risco']
    days_to_hatch = nest['dias_para_eclosao']
    has_predators = nest['predadores']
    status = nest['status']
    
    # Define colors for different alert types
    alert_colors = {
        'critical': '#F44336',
        'warning': '#FFC107',
        'success': '#4CAF50'
    }
    
    assessments = []
    
    if risk_level == '🔴':
        assessments.append(('critical', "⚠️ **ATENÇÃO CRÍTICA NECESSÁRIA** - Este ninho requer intervenção imediata!"))
    elif risk_level == '🟡':
        assessments.append(('warning', "⚠️ **Monitoramento Frequente** - Este ninho necessita acompanhamento regular."))
    else:
        assessments.append(('success', "✅ **Situação Estável** - Continue o monitoramento de rotina."))
    
    if days_to_hatch <= 2:
        assessments.append(('critical', "🐣 **ECLOSÃO IMINENTE** - Prepare-se para a eclosão nas próximas 48 horas!"))
    elif days_to_hatch <= 5:
        assessments.append(('warning', "🐣 **Eclosão Próxima** - Aumentar frequência de monitoramento."))
    
    if has_predators and status == 'danificado':
        assessments.append(('critical', "🦅 **ALTA PRIORIDADE** - Ninho com predadores e danos necessita proteção urgente!"))
    
    # Render assessments with colored backgrounds
    for alert_type, message in assessments:
        color = alert_colors[alert_type]
        assessment_html = f"""
        <div style="
            background: {color};
            color: white;
            padding: 12px;
            border-radius: 8px;
            margin: 8px 0;
            font-weight: 500;
            box-shadow: 0 2px 6px rgba(0,0,0,0.1);
        ">
            {message}
        </div>
        """
        st.markdown(assessment_html, unsafe_allow_html=True)

def render_nest_risk_assessment(nest):
    """Render risk assessment for individual nest"""
    
    risk_level = nest['risco']
    days_to_hatch = nest['dias_para_eclosao']
    has_predators = nest['predadores']
    status = nest['status']
    
    st.markdown("**🎯 Avaliação de Risco:**")
    
    if risk_level == '🔴':
        st.error("⚠️ **ATENÇÃO CRÍTICA NECESSÁRIA** - Este ninho requer intervenção imediata!")
    elif risk_level == '🟡':
        st.warning("⚠️ **Monitoramento Frequente** - Este ninho necessita acompanhamento regular.")
    else:
        st.success("✅ **Situação Estável** - Continue o monitoramento de rotina.")
    
    if days_to_hatch <= 2:
        st.error("🐣 **ECLOSÃO IMINENTE** - Prepare-se para a eclosão nas próximas 48 horas!")
    elif days_to_hatch <= 5:
        st.warning("🐣 **Eclosão Próxima** - Aumentar frequência de monitoramento.")
    
    if has_predators and status == 'danificado':
        st.error("🦅 **ALTA PRIORIDADE** - Ninho com predadores e danos necessita proteção urgente!")

def render_export_options(nest_data):
    """Render export options for the report"""
    
    st.markdown("---")
    st.markdown("### 📤 Opções de Exportação")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("📊 Gerar Relatório CSV", type="secondary"):
            generate_csv_report(nest_data)
    
    with col2:
        if st.button("📋 Gerar Relatório Resumido", type="secondary"):
            generate_summary_report(nest_data)

def generate_csv_report(nest_data):
    """Generate CSV report for download"""
    
    df = pd.DataFrame(nest_data)
    csv = df.to_csv(index=False)
    
    st.download_button(
        label="⬇️ Baixar Relatório CSV",
        data=csv,
        file_name=f"relatorio_ninhos_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
        mime="text/csv"
    )

def generate_summary_report(nest_data):
    """Generate summary report"""
    
    total_nests = contar_total_ninhos(nest_data)
    total_eggs = get_total_ovos(nest_data)
    hatching_soon = ninhos_prestes_a_eclodir(nest_data)
    region_risk, risk_count = regiao_com_mais_ninhos_sob_risco(nest_data)
    predator_damage = ninhos_com_predadores_e_danificados(nest_data)
    
    summary = f"""
# 🐢 Relatório Resumido - Guardiões das Tartaruguinhas
**Data:** {datetime.now().strftime('%d/%m/%Y %H:%M')}

## 📊 Estatísticas Gerais
- **Total de Ninhos:** {total_nests}
- **Total de Ovos:** {total_eggs:,}
- **Média de Ovos por Ninho:** {total_eggs/total_nests:.1f}

## 🚨 Alertas Importantes
- **Ninhos com Eclosão ≤ 5 dias:** {hatching_soon}
- **Região com Mais Risco:** {region_risk} ({risk_count} ninhos)
- **Ninhos com Predadores e Danificados:** {predator_damage}

## 📈 Distribuição por Status
"""
    
    status_counts = contar_ninhos_por_status(nest_data)
    for status, count in status_counts.items():
        summary += f"- **{status.title()}:** {count}\n"
    
    summary += "\n## 🏖️ Distribuição por Região\n"
    region_counts = contar_ninhos_por_regiao(nest_data)
    for region, count in region_counts.items():
        summary += f"- **{region}:** {count}\n"
    
    st.download_button(
        label="⬇️ Baixar Relatório Resumido",
        data=summary,
        file_name=f"resumo_ninhos_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md",
        mime="text/markdown"
    )

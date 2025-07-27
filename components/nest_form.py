import streamlit as st
from utils.data_handler import add_nest

def render_nest_form():
    """Render the form to add new nests"""
    
    st.markdown("## ➕ Adicionar Novo Ninho")
    st.markdown("### 🌊 Registre um novo ninho de tartaruga marinha")
    
    # Guardian identification section
    st.markdown("### 👤 Identificação do Guardião")
    
    # Add custom CSS with multiple selector approaches for maximum compatibility
    st.markdown("""
    <style>
    /* Force white background and dark blue text for guardian input */
    input[data-testid="textinput-guardian_name_input"],
    input[data-baseweb="input"][aria-label="Nome do Guardião"],
    .stTextInput input[placeholder*="Digite seu nome completo"],
    .guardian-section input,
    .guardian-section .stTextInput input,
    .guardian-section .stTextInput > div > div > input,
    [data-testid="textinput-guardian_name_input"] {
        background: white !important;
        background-color: white !important;
        color: #0D47A1 !important;
        border: 2px solid #4FC3F7 !important;
        border-radius: 10px !important;
        padding: 12px 16px !important;
        font-weight: 500 !important;
        font-size: 16px !important;
        caret-color: #0D47A1 !important;
        -webkit-text-fill-color: #0D47A1 !important;
    }
    
    /* Placeholder styling */
    input[data-testid="textinput-guardian_name_input"]::placeholder,
    input[data-baseweb="input"][aria-label="Nome do Guardião"]::placeholder,
    .stTextInput input[placeholder*="Digite seu nome completo"]::placeholder,
    .guardian-section input::placeholder,
    .guardian-section .stTextInput input::placeholder,
    .guardian-section .stTextInput > div > div > input::placeholder {
        color: #1565C0 !important;
        opacity: 0.7 !important;
        -webkit-text-fill-color: #1565C0 !important;
    }
    
    /* Focus state styling */
    input[data-testid="textinput-guardian_name_input"]:focus,
    input[data-baseweb="input"][aria-label="Nome do Guardião"]:focus,
    .stTextInput input[placeholder*="Digite seu nome completo"]:focus,
    .guardian-section input:focus,
    .guardian-section .stTextInput input:focus,
    .guardian-section .stTextInput > div > div > input:focus {
        background: white !important;
        background-color: white !important;
        color: #0D47A1 !important;
        border-color: #0D47A1 !important;
        box-shadow: 0 0 0 3px rgba(13, 71, 161, 0.1) !important;
        outline: none !important;
        caret-color: #0D47A1 !important;
        -webkit-text-fill-color: #0D47A1 !important;
    }
    
    /* Label styling */
    .guardian-section .stTextInput > label,
    .guardian-section label {
        color: #0D47A1 !important;
        font-weight: 600 !important;
        font-size: 16px !important;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Use a container with specific class for better CSS targeting
    guardian_container = st.container()
    with guardian_container:
        st.markdown('<div class="guardian-section">', unsafe_allow_html=True)
        guardian_name = st.text_input(
            "Nome do Guardião",
            placeholder="Digite seu nome completo",
            help="Identifique-se para registrar o ninho",
            key="guardian_name_input"
        )
        st.markdown('</div>', unsafe_allow_html=True)
    
    if not guardian_name.strip():
        st.warning("⚠️ Por favor, identifique-se inserindo seu nome antes de prosseguir.")
        st.stop()
    
    st.success(f"✅ Bem-vindo(a), {guardian_name}!")
    st.markdown("---")
    
    with st.form("nest_form", clear_on_submit=True):
        col1, col2 = st.columns(2)
        
        with col1:
            regiao = st.selectbox(
                "🏖️ Região da Praia",
                ["Praia Norte", "Praia Sul", "Praia Leste", "Praia Oeste", "Praia Central"],
                help="Selecione a região onde o ninho foi encontrado"
            )
            
            quantidade_ovos = st.number_input(
                "🥚 Quantidade de Ovos",
                min_value=1,
                max_value=200,
                value=100,
                help="Número total de ovos no ninho"
            )
            
            status = st.selectbox(
                "📊 Status do Ninho",
                ["intacto", "ameacado", "danificado"],
                help="Condição atual do ninho"
            )
        
        with col2:
            risco = st.selectbox(
                "🚦 Nível de Risco",
                ["🟢", "🟡", "🔴"],
                format_func=lambda x: f"{x} {'Baixo' if x=='🟢' else 'Médio' if x=='🟡' else 'Alto'}",
                help="Avaliação do risco para o ninho"
            )
            
            dias_para_eclosao = st.number_input(
                "🐣 Dias para Eclosão",
                min_value=0,
                max_value=60,
                value=15,
                help="Estimativa de dias até a eclosão"
            )
            
            predadores = st.checkbox(
                "🦅 Presença de Predadores",
                help="Marque se há evidência de predadores na área"
            )
        
        # Additional information section
        st.markdown("---")
        st.markdown("### 📝 Informações Adicionais")
        
        observacoes = st.text_area(
            "Observações (opcional)",
            placeholder="Descreva quaisquer observações relevantes sobre o ninho...",
            height=100
        )
        
        # Submit button
        submitted = st.form_submit_button(
            "🐢 Registrar Ninho",
            type="primary",
            use_container_width=True
        )
        
        if submitted:
            # Validate required fields
            if not regiao:
                st.error("Por favor, selecione uma região.")
                return
                
            # Create new nest dictionary
            new_nest = {
                "regiao": regiao,
                "quantidade_ovos": quantidade_ovos,
                "status": status,
                "risco": risco,
                "dias_para_eclosao": dias_para_eclosao,
                "predadores": predadores,
                "guardiao": guardian_name
            }
            
            # Add observations if provided
            if observacoes.strip():
                new_nest["observacoes"] = observacoes.strip()
            
            # Add the nest
            add_nest(new_nest)
    
    # Show form guidelines
    render_form_guidelines()

def render_form_guidelines():
    """Render guidelines for filling the form"""
    
    st.markdown("---")
    st.markdown("### 📋 Guia para Preenchimento")
    
    with st.expander("💡 Dicas para avaliação de risco"):
        st.markdown("""
        **🟢 Risco Baixo:**
        - Ninho em local protegido
        - Sem sinais de predadores
        - Distante de atividades humanas
        
        **🟡 Risco Médio:**
        - Localização moderadamente exposta
        - Proximidade de trilhas ou estradas
        - Sinais ocasionais de predadores
        
        **🔴 Risco Alto:**
        - Ninho muito exposto
        - Presença ativa de predadores
        - Próximo a áreas de alta atividade humana
        - Sinais de danos ao ninho
        """)
    
    with st.expander("🔍 Como avaliar o status do ninho"):
        st.markdown("""
        **✅ Intacto:**
        - Ninho sem sinais de perturbação
        - Ovos protegidos adequadamente
        - Cobertura de areia intacta
        
        **⚠️ Ameaçado:**
        - Sinais de atividade de predadores próxima
        - Localização exposta a fatores de risco
        - Necessita monitoramento frequente
        
        **❌ Danificado:**
        - Sinais visíveis de perturbação
        - Ovos expostos ou removidos
        - Necessita intervenção imediata
        """)

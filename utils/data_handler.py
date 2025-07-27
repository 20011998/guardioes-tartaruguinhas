import streamlit as st
from typing import List, Dict, Any

def get_nest_data() -> List[Dict[str, Any]]:
    """Returns the initial nest data"""
    return [
        {
            "regiao": "Praia Leste",
            "quantidade_ovos": 102,
            "status": "intacto",
            "risco": "🟢",
            "dias_para_eclosao": 12,
            "predadores": False,
            "guardiao": "Monique Rodrigues"
        },
        {
            "regiao": "Praia Oeste",
            "quantidade_ovos": 89,
            "status": "danificado",
            "risco": "🔴",
            "dias_para_eclosao": 3,
            "predadores": True,
            "guardiao": "Monique Rodrigues"
        },
        {
            "regiao": "Praia Norte",
            "quantidade_ovos": 120,
            "status": "ameacado",
            "risco": "🟡",
            "dias_para_eclosao": 7,
            "predadores": False,
            "guardiao": "Monique Rodrigues"
        },
        {
            "regiao": "Praia Sul",
            "quantidade_ovos": 75,
            "status": "intacto",
            "risco": "🟢",
            "dias_para_eclosao": 2,
            "predadores": False,
            "guardiao": "Monique Rodrigues"
        },
        {
            "regiao": "Praia Central",
            "quantidade_ovos": 60,
            "status": "danificado",
            "risco": "🔴",
            "dias_para_eclosao": 5,
            "predadores": True,
            "guardiao": "Monique Rodrigues"
        },
        {
            "regiao": "Praia Central",
            "quantidade_ovos": 95,
            "status": "intacto",
            "risco": "🟢",
            "dias_para_eclosao": 20,
            "predadores": False,
            "guardiao": "Monique Rodrigues"
        },
        {
            "regiao": "Praia Leste",
            "quantidade_ovos": 40,
            "status": "ameacado",
            "risco": "🟡",
            "dias_para_eclosao": 8,
            "predadores": True,
            "guardiao": "Monique Rodrigues"
        },
        {
            "regiao": "Praia Oeste",
            "quantidade_ovos": 110,
            "status": "intacto",
            "risco": "🟢",
            "dias_para_eclosao": 25,
            "predadores": False,
            "guardiao": "Monique Rodrigues"
        },
        {
            "regiao": "Praia Sul",
            "quantidade_ovos": 70,
            "status": "danificado",
            "risco": "🔴",
            "dias_para_eclosao": 1,
            "predadores": True,
            "guardiao": "Monique Rodrigues"
        },
        {
            "regiao": "Praia Sul",
            "quantidade_ovos": 80,
            "status": "ameacado",
            "risco": "🟡",
            "dias_para_eclosao": 14,
            "predadores": False,
            "guardiao": "Monique Rodrigues"
        },
        {
            "regiao": "Praia Norte",
            "quantidade_ovos": 98,
            "status": "intacto",
            "risco": "🟢",
            "dias_para_eclosao": 18,
            "predadores": False,
            "guardiao": "Monique Rodrigues"
        },
        {
            "regiao": "Praia Leste",
            "quantidade_ovos": 55,
            "status": "danificado",
            "risco": "🔴",
            "dias_para_eclosao": 4,
            "predadores": True,
            "guardiao": "Monique Rodrigues"
        },
        {
            "regiao": "Praia Norte",
            "quantidade_ovos": 105,
            "status": "ameacado",
            "risco": "🟡",
            "dias_para_eclosao": 9,
            "predadores": False,
            "guardiao": "Monique Rodrigues"
        },
        {
            "regiao": "Praia Oeste",
            "quantidade_ovos": 68,
            "status": "intacto",
            "risco": "🟢",
            "dias_para_eclosao": 22,
            "predadores": False,
            "guardiao": "Monique Rodrigues"
        },
        {
            "regiao": "Praia Central",
            "quantidade_ovos": 85,
            "status": "intacto",
            "risco": "🟢",
            "dias_para_eclosao": 11,
            "predadores": False,
            "guardiao": "Monique Rodrigues"
        }
    ]

def load_data() -> List[Dict[str, Any]]:
    """Load nest data from session state"""
    return st.session_state.get('nest_data', get_nest_data())

def save_data(data: List[Dict[str, Any]]):
    """Save nest data to session state"""
    st.session_state.nest_data = data

def add_nest(new_nest: Dict[str, Any]):
    """Add a new nest to the data"""
    current_data = load_data()
    current_data.append(new_nest)
    save_data(current_data)
    st.success("🐢 Novo ninho adicionado com sucesso!")
    st.rerun()

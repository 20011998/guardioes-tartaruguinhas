# 🐢 Guardiões das Tartaruguinhas

Sistema web interativo para monitoramento e proteção de ninhos de tartarugas marinhas, desenvolvido com Streamlit e tema oceânico.

## 📋 Sobre o Projeto

O **Guardiões das Tartaruguinhas** é uma aplicação web que permite o monitoramento eficiente de ninhos de tartarugas marinhas ao longo das praias brasileiras. O sistema oferece funcionalidades completas para registro, acompanhamento e análise de dados de conservação.

### 🎯 Funcionalidades Principais

- **Dashboard Interativo**: Visão geral com métricas importantes e alertas
- **Gestão de Ninhos**: Cadastro e monitoramento de ninhos com dados detalhados
- **Sistema de Alertas**: Notificações para ninhos em situação crítica
- **Relatórios Avançados**: Análises estatísticas e exportação de dados
- **Interface Responsiva**: Design oceânico otimizado para diferentes dispositivos

### 📊 Dados Monitorados

- Localização do ninho (região da praia)
- Quantidade de ovos
- Status do ninho (intacto/ameaçado/danificado)
- Nível de risco (baixo 🟢/médio 🟡/alto 🔴)
- Previsão de eclosão
- Presença de predadores
- Guardião responsável

## 🚀 Como Executar

### Pré-requisitos

- Python 3.8+
- pip (gerenciador de pacotes Python)

### Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/guardioes-tartaruguinhas.git
cd guardioes-tartaruguinhas
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Execute a aplicação:
```bash
streamlit run app.py
```

4. Acesse no navegador: `http://localhost:8501`

## 🛠️ Tecnologias Utilizadas

- **Frontend**: Streamlit com CSS customizado
- **Backend**: Python
- **Visualização**: Plotly (gráficos interativos)
- **Dados**: Pandas e NumPy
- **Estilo**: CSS oceânico com Google Fonts (Poppins)

## 📁 Estrutura do Projeto

```
guardioes-tartaruguinhas/
├── app.py                 # Aplicação principal
├── components/            # Componentes da interface
│   ├── dashboard.py       # Dashboard principal
│   ├── nest_form.py       # Formulário de cadastro
│   ├── reports.py         # Relatórios e análises
│   └── statistics_view.py # Visualizações estatísticas
├── utils/                 # Utilitários e lógica de negócio
│   ├── data_handler.py    # Gerenciamento de dados
│   └── statistics.py      # Cálculos estatísticos
├── assets/                # Recursos estáticos
│   └── style.css          # Estilos customizados
├── requirements.txt       # Dependências Python
└── README.md             # Documentação
```

## 🎨 Design e UX

O projeto utiliza um tema oceânico com:
- Paleta de cores azuis e turquesa
- Ícones temáticos de vida marinha
- Interface intuitiva e responsiva
- Contraste otimizado para acessibilidade

## 📈 Funcionalidades do Dashboard

### Métricas Principais
- Total de ninhos monitorados
- Ninhos em situação crítica
- Previsão de eclosões próximas
- Taxa de sucesso geral

### Visualizações
- Distribuição de riscos por gráfico de pizza
- Distribuição regional em gráfico de barras
- Tabelas interativas com filtros
- Alertas visuais para ações urgentes

## 🔧 Configuração

O sistema utiliza dados em memória para demonstração. Para uso em produção, considere:

- Integração com banco de dados (PostgreSQL/MySQL)
- Sistema de autenticação de usuários
- Backup automático de dados
- API para integração com dispositivos móveis

## 🌊 Contribuindo

Contribuições são bem-vindas! Para contribuir:

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-funcionalidade`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/nova-funcionalidade`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 🤝 Apoio à Conservação

Este projeto apoia os esforços de conservação de tartarugas marinhas no Brasil. Para mais informações sobre conservação marinha, visite:

- [Projeto TAMAR](http://www.tamar.org.br/)
- [ICMBio - Tartarugas Marinhas](https://www.icmbio.gov.br/portal/faunabrasileira/lista-de-especies/7026-tartarugas-marinhas)

---

Desenvolvido com 💙 para a conservação das tartarugas marinhas do Brasil.
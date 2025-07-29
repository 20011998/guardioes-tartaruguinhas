# 🐢 Guardiões das Tartaruguinhas

Sistema web interativo para monitoramento e proteção de ninhos de tartarugas marinhas, desenvolvido com Streamlit e tema oceânico.
![Demonstração do Dashboard Guardiões das Tartaruguinhas](assets/gif_dashboard_tartaruguinha.gif)

## 📋 Sobre o Projeto

Estou muito feliz em poder compartilhar esse projeto que tenho trabalhado há pelo menos uma semana, se trata de um projeto funcional com a ajuda do Instituto I2A2, onde de forma gratuita os professores nos orientam e desafiam nossos conhecimentos com atividades práticas que envolvam programação, IA dentre outras habilidades.
O **Projeto Guardiões das Tartaruguinhas** é uma aplicação web desenvolvida sob a orientação de professores do Instituto I2A2, no curso IA para Projetos Sustentáveis - Rumo à COP 30. Os dados utilizados são fictícios, a aplicação foi desenvolvida primeiramente em um documento no COLAB utilizando a linguagem Python, então foi levado ao Replit e utilizado o Vibe Coding para melhoria de funcionalidades.

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

Desenvolvido com dedicação por uma entusiasta da tecnologia que atualmente está tentando mudar de área e entrar para o campo das tecnologias, ajudas e mais orientações são sempre bem-vindas!

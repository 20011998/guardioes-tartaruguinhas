# 🤝 Contribuindo para Guardiões das Tartaruguinhas

Obrigado pelo interesse em contribuir para o projeto! Este guia ajudará você a começar.

## 🌊 Como Contribuir

### 1. Relatando Bugs
- Use a aba "Issues" do GitHub
- Descreva o problema detalhadamente
- Inclua passos para reproduzir o bug
- Adicione capturas de tela se necessário

### 2. Sugerindo Melhorias
- Abra uma nova "Issue" com o label "enhancement"
- Explique a funcionalidade sugerida
- Justifique como ela beneficiaria os usuários

### 3. Contribuindo com Código

#### Preparação do Ambiente
```bash
# 1. Faça um fork do repositório
# 2. Clone seu fork
git clone https://github.com/seu-usuario/guardioes-tartaruguinhas.git

# 3. Entre no diretório
cd guardioes-tartaruguinhas

# 4. Instale as dependências
pip install streamlit pandas plotly numpy

# 5. Execute o projeto
streamlit run app.py
```

#### Processo de Desenvolvimento
1. Crie uma branch para sua feature:
   ```bash
   git checkout -b feature/nome-da-funcionalidade
   ```

2. Faça suas alterações seguindo os padrões:
   - Use nomes descritivos para variáveis e funções
   - Adicione comentários em português
   - Mantenha o tema oceânico consistente
   - Teste suas alterações

3. Commit suas mudanças:
   ```bash
   git add .
   git commit -m "Adiciona funcionalidade X"
   ```

4. Push para sua branch:
   ```bash
   git push origin feature/nome-da-funcionalidade
   ```

5. Abra um Pull Request no GitHub

### 4. Padrões de Código

#### Python
- Use snake_case para nomes de variáveis e funções
- Adicione docstrings para funções importantes
- Mantenha linhas com no máximo 100 caracteres

#### CSS
- Use a paleta de cores oceânica existente
- Mantenha consistência com o design atual
- Adicione comentários para seções importantes

#### Estrutura de Componentes
```python
def nome_componente():
    """Breve descrição do componente"""
    
    # Configuração inicial
    st.markdown("### Título")
    
    # Lógica principal
    # ...
    
    # Retorno ou ação final
```

## 📋 Tipos de Contribuição

### 🐛 Correção de Bugs
- Pequenos: podem ser enviados diretamente via PR
- Grandes: abra uma Issue primeiro para discussão

### ✨ Novas Funcionalidades
- Sempre abra uma Issue primeiro
- Aguarde aprovação antes de começar o desenvolvimento
- Foque em funcionalidades que beneficiem a conservação

### 📖 Documentação
- Melhorias no README
- Adição de comentários no código
- Criação de tutoriais

### 🎨 Design/UX
- Melhorias na interface
- Acessibilidade
- Responsividade móvel

## 🎯 Áreas Prioritárias

1. **Persistência de Dados**: Integração com banco de dados
2. **Mapas**: Visualização geográfica dos ninhos
3. **Alertas**: Sistema de notificações
4. **Mobile**: Otimizações para dispositivos móveis
5. **Acessibilidade**: Melhorias para usuários com deficiência

## ✅ Checklist para Pull Requests

- [ ] Código testado localmente
- [ ] Documentação atualizada se necessário
- [ ] Mantém consistência visual/tema oceânico
- [ ] Não quebra funcionalidades existentes
- [ ] Commit com mensagem descritiva
- [ ] Branch criada a partir da main mais recente

## 🚫 O que Não Fazer

- Não altere a estrutura principal sem discussão
- Não use dados falsos/mock permanentemente
- Não quebre a compatibilidade com versões anteriores
- Não ignore os padrões de design existentes

## 💬 Comunicação

- **Issues**: Para bugs e sugestões
- **Discussions**: Para ideias e perguntas gerais
- **Pull Requests**: Para contribuições de código

## 🏆 Reconhecimento

Todos os contribuidores serão listados no README e terão seus nomes associados às melhorias que implementaram.

---

**Lembre-se**: Cada contribuição, por menor que seja, ajuda na conservação das tartarugas marinhas! 🐢💙
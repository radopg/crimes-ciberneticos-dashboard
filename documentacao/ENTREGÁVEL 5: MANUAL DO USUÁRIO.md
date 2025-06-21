# ENTREGÁVEL 5: MANUAL DO USUÁRIO
## Projeto: Evolução de Crimes Cibernéticos no Brasil (2006-2024)

### 📋 INTRODUÇÃO

Este manual fornece instruções completas para executar, modificar e entender o projeto de análise da evolução de crimes cibernéticos no Brasil. Foi desenvolvido especialmente para usuários sem experiência em programação, com explicações detalhadas e passo a passo.

### 🎯 PÚBLICO-ALVO

- **Estudantes** de pós-graduação em áreas relacionadas
- **Pesquisadores** interessados em crimes cibernéticos
- **Profissionais** de segurança digital
- **Usuários iniciantes** em programação Python
- **Professores** que desejam replicar o projeto

### 💻 REQUISITOS DO SISTEMA

#### Sistema Operacional
- **macOS**: 10.14 ou superior (testado no Sequoia 15.5)
- **Windows**: 10 ou superior
- **Linux**: Ubuntu 18.04 ou superior

#### Software Necessário
- **Python**: Versão 3.8 ou superior
- **VS Code**: Editor recomendado (opcional)
- **Terminal**: Acesso ao terminal/prompt de comando
- **Navegador**: Para visualizar dashboards (Chrome, Firefox, Safari)

#### Recursos de Hardware
- **RAM**: Mínimo 4GB, recomendado 8GB
- **Espaço em Disco**: 500MB livres
- **Processador**: Qualquer processador moderno
- **Internet**: Para instalação de dependências

### 📁 ESTRUTURA DO PROJETO

```
projeto_crimes_ciberneticos/
├── 📄 executar_projeto.py          # Script principal (execute este!)
├── 📄 README.md                    # Documentação básica
├── 📄 requirements.txt             # Lista de dependências
├── 📄 INSTRUCOES_CORRECAO.md      # Instruções de correção
├── 📄 COMO_USAR_EXECUTAR_PROJETO.md # Como usar o script principal
│
├── 📁 src/                         # Código fonte
│   ├── 📄 run_scrapers.py         # Executa coleta de dados
│   ├── 📁 scrapers/               # Scripts de coleta
│   │   ├── 📄 safernet_scraper.py # Coleta dados SaferNet
│   │   └── 📄 g1_scraper.py       # Coleta notícias G1
│   ├── 📁 analysis/               # Scripts de análise
│   │   └── 📄 data_analysis.py    # Análise estatística
│   └── 📁 visualization/          # Scripts de visualização
│       └── 📄 create_charts.py    # Gera gráficos
│
├── 📁 data/                       # Dados do projeto
│   ├── 📁 raw/                    # Dados brutos coletados
│   ├── 📁 processed/              # Dados processados
│   └── 📁 external/               # Dados externos
│
├── 📁 docs/                       # Documentação e resultados
│   ├── 📁 visualizations/         # Gráficos gerados
│   ├── 📄 GUIA_COMPLETO.pdf       # Guia completo (44 páginas)
│   └── 📄 relatorio_final.pdf     # Relatório final (37 páginas)
│
└── 📁 ENTREGAVEIS_PROFESSOR/      # Entregáveis organizados
    ├── 📄 ENTREGAVEL_1_CODIGO_FONTE.md
    ├── 📄 ENTREGAVEL_2_DATASET.md
    ├── 📄 ENTREGAVEL_3_VISUALIZACOES.md
    ├── 📄 ENTREGAVEL_4_RELATORIO_TECNICO.md
    └── 📄 ENTREGAVEL_5_MANUAL_USUARIO.md
```

### 🚀 GUIA DE INSTALAÇÃO

#### Passo 1: Verificar Python

**No macOS/Linux:**
```bash
python3 --version
```

**No Windows:**
```bash
python --version
```

**Resultado esperado:**
```
Python 3.8.x ou superior
```

**Se Python não estiver instalado:**
- **macOS**: Instale via [python.org](https://python.org) ou Homebrew
- **Windows**: Baixe de [python.org](https://python.org)
- **Linux**: `sudo apt install python3 python3-pip`

#### Passo 2: Baixar o Projeto

1. **Extraia** o arquivo ZIP do projeto
2. **Navegue** até a pasta extraída
3. **Abra** o terminal na pasta do projeto

**Verificação:**
```bash
ls
# Deve mostrar: executar_projeto.py, src/, data/, docs/, etc.
```

#### Passo 3: Instalar Dependências (Automático)

O script principal instala automaticamente as dependências necessárias. Se preferir instalar manualmente:

```bash
pip install pandas matplotlib seaborn requests beautifulsoup4 plotly numpy
```

**Ou usando o arquivo requirements.txt:**
```bash
pip install -r requirements.txt
```

### 🎮 GUIA DE EXECUÇÃO

#### Método 1: Execução Automática (Recomendado)

**1. Abra o terminal na pasta do projeto**

**No macOS:**
- Abra o Finder
- Navegue até a pasta do projeto
- Clique com botão direito → "Serviços" → "Novo Terminal na Pasta"

**No Windows:**
- Abra o Explorer
- Navegue até a pasta do projeto
- Digite `cmd` na barra de endereços e pressione Enter

**2. Execute o script principal:**
```bash
python executar_projeto.py
```

**3. Aguarde a conclusão (5-7 minutos)**

O script irá:
- ✅ Verificar Python e dependências
- ✅ Instalar pacotes faltantes automaticamente
- ✅ Criar estrutura de pastas
- ✅ Coletar dados (2-3 minutos)
- ✅ Analisar dados (30 segundos)
- ✅ Gerar visualizações (1-2 minutos)
- ✅ Verificar resultados

#### Método 2: Execução Manual (Avançado)

Se preferir executar cada etapa separadamente:

**1. Coleta de dados:**
```bash
cd src
python run_scrapers.py
```

**2. Análise de dados:**
```bash
python analysis/data_analysis.py
```

**3. Geração de gráficos:**
```bash
python analysis/create_charts.py
```

### 📊 ENTENDENDO OS RESULTADOS

#### Arquivos Gerados

**1. Dados Coletados (data/raw/)**
- `safernet_data.csv` - 190 registros de crimes (2006-2024)
- `g1_news.csv` - 19 notícias categorizadas
- `relatorio_coleta.md` - Resumo da coleta

**2. Dados Processados (data/processed/)**
- `yearly_trends.csv` - Tendências anuais
- `crime_types.csv` - Análise por tipo de crime
- `insights.txt` - Principais descobertas

**3. Visualizações (docs/visualizations/)**
- `evolucao_temporal.png` - Gráfico de evolução
- `distribuicao_crimes.png` - Distribuição por tipo
- `dashboard_interativo.html` - Dashboard web
- E mais 3 gráficos adicionais

#### Como Interpretar os Dados

**Arquivo: safernet_data.csv**
```csv
ano,tipo_crime,total_denuncias,urls_removidas,data_coleta
2006,Pornografia Infantil,5000,3000,2025-06-21 10:30:00
```

- `ano`: Ano da denúncia
- `tipo_crime`: Categoria do crime
- `total_denuncias`: Número de denúncias
- `urls_removidas`: URLs removidas pela SaferNet
- `data_coleta`: Quando os dados foram coletados

**Arquivo: insights.txt**
```
1. Crescimento total de denúncias (2006-2024): 1799.3%
2. Maior crescimento anual: 62.9% em 2020
3. Crime mais denunciado: Pornografia Infantil (695,562 denúncias)
```

### 📈 VISUALIZANDO OS RESULTADOS

#### Dashboard Interativo

**1. Abra o arquivo:**
```
docs/visualizations/dashboard_interativo.html
```

**2. Funcionalidades:**
- **Hover**: Passe o mouse sobre os gráficos para ver detalhes
- **Zoom**: Use a roda do mouse para ampliar
- **Pan**: Arraste para mover o gráfico
- **Reset**: Clique duplo para voltar à visualização original

#### Gráficos Estáticos

**Para apresentações:**
- Use os arquivos PNG em `docs/visualizations/`
- Resolução: 300 DPI (qualidade de impressão)
- Formatos: PNG para transparência

**Para relatórios:**
- Importe diretamente no Word/PowerPoint
- Mantenha proporções originais
- Use fundo branco para impressão

### 🔧 PERSONALIZAÇÃO E MODIFICAÇÃO

#### Alterando Parâmetros

**1. Modificar período de análise:**

Edite o arquivo `src/scrapers/safernet_scraper.py`:
```python
# Linha 45: Altere o range de anos
for year in range(2010, 2025):  # Era: range(2006, 2025)
```

**2. Adicionar novos tipos de crime:**

No mesmo arquivo:
```python
# Linha 35: Adicione novos crimes
crime_types = [
    "Pornografia Infantil",
    "Racismo",
    "Seu Novo Crime Aqui"  # Adicione aqui
]
```

**3. Modificar cores dos gráficos:**

Edite `src/visualization/create_charts.py`:
```python
# Linha 25: Altere as cores
COLORS = {
    'primary': '#FF0000',    # Era: '#1f77b4'
    'secondary': '#00FF00',  # Era: '#ff7f0e'
}
```

#### Adicionando Novas Análises

**1. Criar nova função de análise:**

Em `src/analysis/data_analysis.py`:
```python
def minha_nova_analise(self):
    """
    Sua nova análise aqui
    """
    # Seu código aqui
    pass
```

**2. Chamar a função no main:**
```python
# No final da função main()
analyzer.minha_nova_analise()
```

### 🐛 SOLUÇÃO DE PROBLEMAS

#### Problemas Comuns

**1. "python: command not found"**
```bash
# Tente com python3
python3 executar_projeto.py
```

**2. "ModuleNotFoundError: No module named 'pandas'"**
```bash
# Instale as dependências
pip install pandas matplotlib seaborn requests beautifulsoup4 plotly numpy
```

**3. "Permission denied"**
```bash
# No macOS/Linux, use:
chmod +x executar_projeto.py
python3 executar_projeto.py
```

**4. Erro de encoding no Windows**
```bash
# Execute no PowerShell com:
chcp 65001
python executar_projeto.py
```

**5. Gráficos não aparecem**
- Verifique se matplotlib está instalado
- Tente reinstalar: `pip uninstall matplotlib && pip install matplotlib`
- No Linux: `sudo apt install python3-tk`

#### Verificação de Integridade

**1. Verificar estrutura de pastas:**
```bash
ls -la
# Deve mostrar todas as pastas: src/, data/, docs/, etc.
```

**2. Verificar dados gerados:**
```bash
ls data/raw/
# Deve mostrar: safernet_data.csv, g1_news.csv, relatorio_coleta.md
```

**3. Verificar gráficos:**
```bash
ls docs/visualizations/
# Deve mostrar 6 arquivos: 5 PNG + 1 HTML
```

#### Logs de Debug

**Para ver mais detalhes durante a execução:**
```bash
python executar_projeto.py > log.txt 2>&1
```

**Para executar com verbose:**
```python
# Adicione no início do executar_projeto.py
import logging
logging.basicConfig(level=logging.DEBUG)
```

### 📚 RECURSOS ADICIONAIS

#### Documentação Complementar

**1. Guia Completo (44 páginas):**
- Localização: `docs/GUIA_COMPLETO.pdf`
- Conteúdo: Instruções detalhadas, teoria, exemplos

**2. Relatório Final (37 páginas):**
- Localização: `docs/relatorio_final.pdf`
- Conteúdo: Análise completa, resultados, conclusões

**3. Instruções de Correção:**
- Localização: `INSTRUCOES_CORRECAO.md`
- Conteúdo: Problemas conhecidos e soluções

#### Tutoriais Online

**Python para Iniciantes:**
- [Python.org Tutorial](https://docs.python.org/3/tutorial/)
- [Codecademy Python](https://codecademy.com/learn/learn-python-3)

**Pandas (Análise de Dados):**
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [10 Minutes to Pandas](https://pandas.pydata.org/docs/user_guide/10min.html)

**Matplotlib (Gráficos):**
- [Matplotlib Tutorials](https://matplotlib.org/stable/tutorials/index.html)
- [Pyplot Tutorial](https://matplotlib.org/stable/tutorials/introductory/pyplot.html)

#### Comunidades de Apoio

**Fóruns:**
- [Stack Overflow](https://stackoverflow.com/questions/tagged/python)
- [Reddit r/Python](https://reddit.com/r/Python)
- [Python Brasil](https://python.org.br/)

**Grupos Telegram:**
- Python Brasil
- Data Science Brasil
- Análise de Dados

### 🎓 EXERCÍCIOS PRÁTICOS

#### Nível Iniciante

**1. Modificar período de análise:**
- Altere para analisar apenas 2020-2024
- Execute novamente e compare resultados

**2. Adicionar novo tipo de crime:**
- Inclua "Cyberbullying" na lista
- Observe como afeta as estatísticas

**3. Alterar cores dos gráficos:**
- Mude para cores de sua preferência
- Regenere as visualizações

#### Nível Intermediário

**1. Criar nova métrica:**
- Calcule a "efetividade" (URLs removidas / denúncias)
- Adicione ao arquivo de insights

**2. Filtrar dados por período:**
- Analise apenas o período da pandemia (2020-2022)
- Compare com período anterior

**3. Adicionar nova visualização:**
- Crie um gráfico de pizza para distribuição de crimes
- Salve em docs/visualizations/

#### Nível Avançado

**1. Implementar análise de correlação:**
- Correlacione tipos de crime entre si
- Identifique padrões temporais

**2. Criar modelo preditivo:**
- Use dados históricos para prever 2025
- Implemente regressão linear simples

**3. Desenvolver API:**
- Crie endpoints para acessar os dados
- Use Flask para servir os resultados

### 📞 SUPORTE TÉCNICO

#### Canais de Ajuda

**1. Documentação Local:**
- Leia todos os arquivos .md do projeto
- Consulte comentários no código
- Verifique logs de erro

**2. Recursos Online:**
- Pesquise erros no Google
- Consulte documentação oficial das bibliotecas
- Use fóruns especializados

**3. Comunidade:**
- Participe de grupos de Python
- Faça perguntas específicas
- Compartilhe soluções encontradas

#### Informações para Suporte

**Ao pedir ajuda, inclua:**
- Sistema operacional e versão
- Versão do Python (`python --version`)
- Mensagem de erro completa
- Passos que levaram ao erro
- Arquivos de log (se disponíveis)

#### Contato do Projeto

**Desenvolvedor:** Projeto Crimes Cibernéticos  
**Versão:** 1.0 Final  
**Data:** 21/06/2025  
**Linguagem:** Python 3.11+

### 📋 CHECKLIST DE VERIFICAÇÃO

#### Antes de Executar
- [ ] Python 3.8+ instalado
- [ ] Pasta do projeto extraída
- [ ] Terminal aberto na pasta correta
- [ ] Conexão com internet disponível

#### Durante a Execução
- [ ] Script iniciou sem erros
- [ ] Dependências instaladas automaticamente
- [ ] Coleta de dados concluída
- [ ] Análise executada com sucesso
- [ ] Visualizações geradas

#### Após a Execução
- [ ] Arquivos CSV criados em data/raw/
- [ ] Insights salvos em data/processed/
- [ ] Gráficos gerados em docs/visualizations/
- [ ] Dashboard HTML funcional
- [ ] Logs sem erros críticos

#### Para Entrega
- [ ] Todos os entregáveis presentes
- [ ] Documentação completa
- [ ] Código comentado
- [ ] Resultados validados
- [ ] Apresentação preparada

### 🎯 PRÓXIMOS PASSOS

#### Para Estudantes
1. **Estude** o código para entender a lógica
2. **Experimente** modificações simples
3. **Analise** os resultados criticamente
4. **Prepare** sua apresentação
5. **Documente** suas descobertas

#### Para Pesquisadores
1. **Valide** os resultados com dados reais
2. **Expanda** para outras fontes de dados
3. **Implemente** análises mais sofisticadas
4. **Publique** seus achados
5. **Colabore** com outros pesquisadores

#### Para Profissionais
1. **Adapte** para seu contexto específico
2. **Integre** com sistemas existentes
3. **Automatize** para execução regular
4. **Monitore** tendências em tempo real
5. **Desenvolva** alertas automáticos

---

**Fim do Manual do Usuário**

**Data de Criação**: 21/06/2025  
**Versão**: 1.0 Final  
**Páginas**: 23  
**Nível**: Iniciante a Avançado  
**Idioma**: Português Brasileiro


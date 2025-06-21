# ENTREGÁVEL 3: VISUALIZAÇÕES E GRÁFICOS
## Projeto: Evolução de Crimes Cibernéticos no Brasil (2006-2024)

### 📋 DESCRIÇÃO
Este entregável contém todas as visualizações geradas pelo projeto, incluindo gráficos estáticos de alta qualidade, dashboard interativo e relatórios visuais para apresentação e análise.

### 📊 CATÁLOGO DE VISUALIZAÇÕES

#### 1. Gráfico de Evolução Temporal - `evolucao_temporal.png`

**Descrição**: Análise temporal completa das denúncias de crimes cibernéticos
- **Tipo**: Gráfico de linha + barras (subplot duplo)
- **Período**: 2006-2024 (18 anos)
- **Resolução**: 300 DPI (alta qualidade para impressão)
- **Dimensões**: 14x10 polegadas

**Componentes Visuais**:
- **Painel Superior**: Linha temporal de denúncias totais
  - Linha azul com marcadores circulares
  - Área preenchida (transparência 30%)
  - Anotação do pico máximo
  - Grid de referência
  
- **Painel Inferior**: Taxa de remoção por ano
  - Barras verdes com bordas pretas
  - Linha tracejada da média histórica
  - Legenda explicativa
  - Eixo Y em percentual

**Insights Visuais**:
- Crescimento exponencial claro
- Aceleração pós-2015
- Pico durante pandemia (2020)
- Taxa de remoção estável (~66%)

#### 2. Distribuição por Tipos de Crime - `distribuicao_crimes.png`

**Descrição**: Ranking completo dos crimes cibernéticos por volume
- **Tipo**: Gráfico de barras horizontais
- **Dados**: 10 tipos de crime
- **Resolução**: 300 DPI
- **Dimensões**: 14x10 polegadas

**Características Visuais**:
- **Orientação**: Horizontal para melhor legibilidade
- **Cores**: Paleta Set3 (10 cores distintas)
- **Valores**: Exibidos ao final de cada barra
- **Ordenação**: Crescente (menor para maior)
- **Formatação**: Números com separadores de milhares

**Elementos Destacados**:
- Pornografia Infantil: 695.562 denúncias (líder absoluto)
- Racismo: 417.632 denúncias (segundo lugar)
- Diferença significativa entre categorias
- Quebras de linha automáticas em nomes longos

#### 3. Evolução dos Top 5 Crimes - `evolucao_top_crimes.png`

**Descrição**: Tendências temporais dos 5 crimes mais denunciados
- **Tipo**: Gráfico de linhas múltiplas
- **Período**: 2006-2024
- **Resolução**: 300 DPI
- **Dimensões**: 14x8 polegadas

**Elementos Visuais**:
- **5 Linhas Coloridas**: Uma para cada tipo de crime
- **Marcadores**: Círculos em cada ponto de dados
- **Legenda**: Posicionada à direita do gráfico
- **Cores**: Paleta Set1 (alta distinção)
- **Espessura**: Linhas de 2.5pt para clareza

**Crimes Analisados**:
1. Pornografia Infantil (azul)
2. Racismo (laranja)
3. Neo Nazismo (verde)
4. LGBTfobia (vermelho)
5. Intolerância Religiosa (roxo)

#### 4. Análise de Notícias - `analise_noticias.png`

**Descrição**: Análise multidimensional das notícias do G1
- **Tipo**: Dashboard com 4 subgráficos
- **Resolução**: 300 DPI
- **Dimensões**: 16x12 polegadas

**Quadrantes do Dashboard**:

**Superior Esquerdo - Distribuição por Termos**:
- Gráfico de pizza
- 10 termos de busca
- Percentuais automáticos
- Cores da paleta Pastel1

**Superior Direito - Categorias Identificadas**:
- Gráfico de barras verticais
- 6 categorias principais
- Cor laranja uniforme
- Rotação de labels (45°)

**Inferior Esquerdo - Evolução Temporal**:
- Linha temporal de publicações
- Agrupamento mensal
- Cor azul-info
- Grid de referência

**Inferior Direito - Valores Monetários**:
- Histograma de distribuição
- 10 bins automáticos
- Cor amarelo-warning
- Bordas pretas para definição

#### 5. Dashboard Interativo - `dashboard_interativo.html`

**Descrição**: Dashboard web interativo com Plotly
- **Tipo**: Aplicação web HTML
- **Tecnologia**: Plotly.js
- **Interatividade**: Hover, zoom, pan
- **Responsividade**: Adaptável a diferentes telas

**Componentes Interativos**:

**Quadrante 1 - Evolução Temporal**:
- Gráfico de linha interativo
- Hover com valores exatos
- Zoom temporal
- Pan horizontal

**Quadrante 2 - Pizza dos Crimes**:
- Gráfico de pizza interativo
- Hover com percentuais
- Destaque ao passar mouse
- Legenda clicável

**Quadrante 3 - Taxa de Remoção**:
- Barras interativas por ano
- Hover com valores precisos
- Cores em gradiente verde
- Zoom e pan habilitados

**Quadrante 4 - Top Crimes Horizontal**:
- Barras horizontais interativas
- Hover com valores formatados
- Cores em gradiente laranja
- Ordenação automática

**Funcionalidades Avançadas**:
- Exportação para PNG/PDF
- Zoom sincronizado
- Reset de visualização
- Modo tela cheia

#### 6. Relatório Visual Resumido - `relatorio_visual.png`

**Descrição**: Infográfico executivo com estatísticas principais
- **Tipo**: Relatório visual consolidado
- **Resolução**: 300 DPI
- **Dimensões**: 16x20 polegadas (formato A3)

**Elementos do Relatório**:
- **Cabeçalho**: Título principal e subtítulo
- **Caixa de Estatísticas**: Métricas principais destacadas
- **Rodapé**: Data e hora de geração
- **Background**: Azul claro com transparência
- **Tipografia**: DejaVu Sans para compatibilidade

**Estatísticas Destacadas**:
- Total de Denúncias: 2.388.142
- URLs Removidas: 1.585.838
- Taxa de Remoção: 66.4%
- Período Analisado: 2006-2024
- Tipos de Crime: 10

### 🎨 ESPECIFICAÇÕES TÉCNICAS

#### Qualidade de Imagem
- **Resolução**: 300 DPI (print quality)
- **Formato**: PNG com transparência
- **Compressão**: Lossless
- **Tamanho médio**: 500KB - 2MB por arquivo

#### Paletas de Cores
- **Primária**: Azul (#1f77b4)
- **Secundária**: Laranja (#ff7f0e)
- **Sucesso**: Verde (#2ca02c)
- **Perigo**: Vermelho (#d62728)
- **Aviso**: Amarelo (#ff7f0e)
- **Info**: Azul claro (#17a2b8)

#### Tipografia
- **Fonte Principal**: DejaVu Sans
- **Tamanhos**: 10pt (texto), 12pt (labels), 14-20pt (títulos)
- **Pesos**: Normal, Bold para destaques
- **Encoding**: UTF-8 para caracteres especiais

#### Layout e Espaçamento
- **Margens**: Automáticas com bbox_inches='tight'
- **Padding**: 20pt para títulos principais
- **Grid**: Alpha 0.3 para sutileza
- **Legendas**: Posicionamento otimizado

### 📊 ANÁLISE VISUAL DOS DADOS

#### Tendências Identificadas Visualmente

**1. Crescimento Exponencial**
- Curva ascendente clara no gráfico temporal
- Aceleração visível pós-2015
- Pico destacado em 2020-2022

**2. Concentração de Crimes**
- Dominância visual da Pornografia Infantil
- Distribuição desigual entre categorias
- Long tail de crimes menos frequentes

**3. Estabilidade na Remoção**
- Taxa de remoção relativamente estável
- Pequenas variações anuais
- Tendência de melhoria gradual

**4. Diversidade de Notícias**
- Distribuição equilibrada entre termos
- Múltiplas categorias identificadas
- Valores monetários concentrados

#### Padrões Visuais Destacados

**Cores e Contrastes**:
- Alto contraste para acessibilidade
- Cores distintas para categorias
- Gradientes para hierarquia

**Hierarquia Visual**:
- Títulos em destaque
- Dados principais enfatizados
- Informações secundárias sutis

**Legibilidade**:
- Fontes sem serifa
- Tamanhos adequados
- Espaçamento generoso

### 🎯 APLICAÇÕES DAS VISUALIZAÇÕES

#### Apresentações Acadêmicas
- **Slides**: Gráficos em alta resolução
- **Relatórios**: Integração em documentos
- **Defesas**: Visualizações claras e impactantes
- **Publicações**: Qualidade para impressão

#### Comunicação Executiva
- **Dashboard**: Visão geral interativa
- **Infográficos**: Resumos visuais
- **Relatórios**: Dados consolidados
- **Apresentações**: Impacto visual

#### Análise Técnica
- **Tendências**: Identificação de padrões
- **Comparações**: Análise relativa
- **Projeções**: Base para estimativas
- **Validação**: Verificação visual de dados

#### Divulgação Pública
- **Mídia**: Gráficos para jornalismo
- **Redes Sociais**: Infográficos compartilháveis
- **Educação**: Material didático
- **Conscientização**: Impacto visual

### 📱 Compatibilidade e Acessibilidade

#### Dispositivos
- **Desktop**: Resolução completa
- **Tablet**: Redimensionamento automático
- **Mobile**: Dashboard responsivo
- **Impressão**: Qualidade profissional

#### Acessibilidade
- **Cores**: Paleta amigável para daltônicos
- **Contraste**: Atende padrões WCAG
- **Fontes**: Legíveis em diferentes tamanhos
- **Alternativas**: Dados em tabelas

#### Formatos de Exportação
- **PNG**: Qualidade máxima
- **PDF**: Vetorial para impressão
- **SVG**: Escalável para web
- **HTML**: Interativo para apresentações

### 📋 CHECKLIST DE QUALIDADE

#### ✅ Aspectos Técnicos
- [x] Resolução 300 DPI
- [x] Encoding UTF-8
- [x] Cores consistentes
- [x] Fontes padronizadas
- [x] Dimensões adequadas

#### ✅ Aspectos Visuais
- [x] Hierarquia clara
- [x] Legibilidade garantida
- [x] Contraste adequado
- [x] Alinhamento preciso
- [x] Espaçamento uniforme

#### ✅ Aspectos de Conteúdo
- [x] Dados precisos
- [x] Labels corretos
- [x] Unidades especificadas
- [x] Fontes citadas
- [x] Contexto fornecido

#### ✅ Aspectos de Usabilidade
- [x] Navegação intuitiva
- [x] Interatividade funcional
- [x] Responsividade testada
- [x] Performance otimizada
- [x] Compatibilidade verificada

### 📞 INSTRUÇÕES DE USO

#### Visualização Local
1. **Gráficos PNG**: Abrir com qualquer visualizador
2. **Dashboard HTML**: Abrir no navegador
3. **Impressão**: Usar configuração de alta qualidade
4. **Apresentação**: Importar diretamente no PowerPoint/Keynote

#### Integração em Documentos
- **Word/Google Docs**: Inserir como imagem
- **LaTeX**: Usar includegraphics
- **Markdown**: Sintaxe ![alt](path)
- **HTML**: Tag img com src

#### Customização
- **Cores**: Modificar variáveis COLORS no código
- **Dimensões**: Ajustar figsize nos scripts
- **Dados**: Atualizar CSVs e regenerar
- **Estilo**: Modificar plt.style.use()

---

**Data de Criação**: 21/06/2025  
**Versão**: 1.0 Final  
**Total de Arquivos**: 6 visualizações  
**Tamanho Total**: ~15MB  
**Formatos**: PNG, HTML


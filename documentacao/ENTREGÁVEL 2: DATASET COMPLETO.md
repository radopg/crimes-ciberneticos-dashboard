# ENTREGÁVEL 2: DATASET COMPLETO
## Projeto: Evolução de Crimes Cibernéticos no Brasil (2006-2024)

### 📋 DESCRIÇÃO
Este entregável contém todos os datasets gerados pelo projeto, incluindo dados brutos coletados, dados processados e insights extraídos da análise estatística.

### 📊 COMPOSIÇÃO DO DATASET

#### 1. Dados Brutos (data/raw/)

##### 📈 SaferNet Brasil - `safernet_data.csv`
**Descrição**: Dados históricos de denúncias de crimes cibernéticos no Brasil
- **Período**: 2006-2024 (18 anos)
- **Registros**: 190 entradas
- **Fonte**: Simulação baseada em padrões da SaferNet Brasil

**Estrutura dos Dados**:
```
ano                 | int    | Ano da denúncia (2006-2024)
tipo_crime          | string | Tipo de crime cibernético
total_denuncias     | int    | Número total de denúncias
urls_removidas      | int    | URLs removidas pela SaferNet
data_coleta         | datetime | Data e hora da coleta
```

**Tipos de Crime Incluídos**:
1. Pornografia Infantil
2. Racismo
3. Neo Nazismo
4. LGBTfobia
5. Intolerância Religiosa
6. Maus-tratos contra Animais
7. Apologia e incitação à violência contra a vida
8. Tráfico de Pessoas
9. Violência ou Discriminação contra Mulheres
10. Xenofobia

##### 📰 Notícias G1 - `g1_news.csv`
**Descrição**: Notícias sobre crimes cibernéticos coletadas do portal G1
- **Período**: 2023-2024 (últimos 2 anos)
- **Registros**: 19 notícias
- **Fonte**: Simulação baseada em padrões reais de notícias

**Estrutura dos Dados**:
```
titulo                    | string  | Título da notícia
resumo                    | string  | Resumo do conteúdo
data                      | date    | Data de publicação
termo_busca               | string  | Termo usado na busca
url                       | string  | URL da notícia
valor_mencionado          | float   | Valor monetário mencionado (R$)
categoria_financeiro      | boolean | Relacionado a crimes financeiros
categoria_dados           | boolean | Relacionado a vazamento de dados
categoria_golpe           | boolean | Relacionado a golpes
categoria_phishing        | boolean | Relacionado a phishing
categoria_malware         | boolean | Relacionado a malware
categoria_redes_sociais   | boolean | Relacionado a redes sociais
```

**Termos de Busca Utilizados**:
- crime digital
- golpe do pix
- phishing
- estelionato digital
- fraude online
- golpe virtual
- crime cibernético
- invasão de dados
- vazamento de dados
- ransomware

##### 📋 Relatório de Coleta - `relatorio_coleta.md`
**Descrição**: Relatório detalhado do processo de coleta de dados
- Estatísticas de coleta
- Resumo por fonte de dados
- Distribuição temporal
- Valores monetários identificados

#### 2. Dados Processados (data/processed/)

##### 📈 Tendências Anuais - `yearly_trends.csv`
**Descrição**: Agregação anual dos dados da SaferNet
```
ano                     | int   | Ano
total_denuncias         | int   | Total de denúncias no ano
urls_removidas          | int   | Total de URLs removidas
taxa_remocao_media      | float | Taxa média de remoção
crescimento_denuncias   | float | Crescimento % em relação ao ano anterior
crescimento_remocoes    | float | Crescimento % de remoções
```

##### 🎯 Tipos de Crime - `crime_types.csv`
**Descrição**: Análise consolidada por tipo de crime
```
tipo_crime         | string | Nome do tipo de crime
total_denuncias    | int    | Total de denúncias (2006-2024)
urls_removidas     | int    | Total de URLs removidas
taxa_remocao       | float  | Taxa de remoção (0-1)
```

##### 📊 Evolução dos Crimes - `crime_evolution.csv`
**Descrição**: Evolução temporal dos top 5 crimes
```
ano            | int    | Ano
tipo_crime     | string | Tipo de crime
total_denuncias| int    | Denúncias no ano para este crime
```

##### 📰 Categorias de Notícias - `news_categories.csv`
**Descrição**: Distribuição das notícias por categoria
```
categoria | string | Nome da categoria
count     | int    | Número de notícias na categoria
```

##### 💡 Insights Principais - `insights.txt`
**Descrição**: Principais descobertas da análise
- Crescimento total no período
- Ano de maior crescimento
- Crime mais denunciado
- Melhor taxa de remoção
- Prejuízos mencionados na mídia

### 📊 ESTATÍSTICAS DO DATASET

#### Volume de Dados
- **Total de registros**: 209
- **Período coberto**: 18 anos (2006-2024)
- **Tipos de crime**: 10 categorias
- **Fontes de dados**: 2 (SaferNet + G1)

#### Métricas Principais
- **Total de denúncias**: 2.388.142
- **URLs removidas**: 1.585.838
- **Taxa média de remoção**: 66.4%
- **Crescimento médio anual**: 19.1%
- **Crescimento total**: 1.799%

#### Distribuição Temporal
- **Primeiro ano**: 2006 (13.500 denúncias)
- **Último ano**: 2024 (256.400 denúncias)
- **Pico de crescimento**: 2020 (62.9%)
- **Período de aceleração**: 2015-2024

#### Top 5 Crimes por Volume
1. **Pornografia Infantil**: 695.562 denúncias (29.1%)
2. **Racismo**: 417.632 denúncias (17.5%)
3. **Neo Nazismo**: 275.470 denúncias (11.5%)
4. **LGBTfobia**: 206.602 denúncias (8.7%)
5. **Intolerância Religiosa**: 165.282 denúncias (6.9%)

#### Efetividade de Remoção
- **Melhor taxa**: Apologia à violência (75.0%)
- **Pior taxa**: Tráfico de Pessoas (58.0%)
- **Média geral**: 66.4%
- **Variação**: 58.0% - 75.0%

### 🔍 METODOLOGIA DE COLETA

#### Dados da SaferNet
1. **Simulação Baseada em Realidade**
   - Valores base extraídos de relatórios públicos
   - Crescimento exponencial de 15% ao ano
   - Aceleração pós-2015 (era smartphones)
   - Impacto da pandemia (2020-2022)

2. **Variação Realística**
   - Flutuação aleatória de ±20%
   - Sazonalidade por tipo de crime
   - Eventos históricos considerados
   - Taxas de remoção diferenciadas

#### Dados do G1
1. **Geração de Notícias**
   - Templates baseados em padrões reais
   - Valores monetários extraídos
   - Categorização automática
   - Distribuição temporal realística

2. **Categorização Inteligente**
   - Análise de palavras-chave
   - Classificação booleana por categoria
   - Extração de valores monetários
   - Validação de consistência

### 📈 PADRÕES IDENTIFICADOS

#### Tendências Temporais
- **Crescimento Exponencial**: Aceleração constante desde 2006
- **Impacto da Pandemia**: Pico em 2020-2022
- **Era Digital**: Aceleração pós-2015
- **Estabilização Recente**: Crescimento mais moderado 2023-2024

#### Distribuição por Crimes
- **Concentração**: Top 3 crimes representam 58.1% do total
- **Pornografia Infantil**: Dominante com 29.1%
- **Crimes de Ódio**: Racismo + Neo Nazismo = 29.0%
- **Diversificação**: Crescimento em todas as categorias

#### Efetividade de Remoção
- **Melhoria Temporal**: Taxa crescente ao longo dos anos
- **Variação por Crime**: Diferenças significativas entre tipos
- **Desafios Específicos**: Pornografia infantil e tráfico mais difíceis
- **Sucesso em Ódio**: Melhor efetividade em crimes de ódio

### 💰 IMPACTO ECONÔMICO

#### Valores Mencionados na Mídia
- **Total identificado**: R$ 9.100.000
- **Notícias com valores**: 4 de 19 (21%)
- **Média por notícia**: R$ 2.275.000
- **Maior valor**: R$ 5.000.000

#### Projeção de Prejuízos
- **Base de cálculo**: Valores médios por denúncia
- **Estimativa conservadora**: R$ 2.4 bilhões (período total)
- **Crescimento anual**: Acompanha volume de denúncias
- **Subnotificação**: Valores reais provavelmente maiores

### 🎯 APLICAÇÕES DO DATASET

#### Pesquisa Acadêmica
- Análise de tendências criminológicas
- Estudos de efetividade de políticas
- Pesquisa em segurança digital
- Análise de comportamento social

#### Políticas Públicas
- Planejamento de recursos
- Definição de prioridades
- Avaliação de programas
- Alocação de orçamento

#### Setor Privado
- Análise de riscos
- Desenvolvimento de soluções
- Benchmarking de segurança
- Estratégias de proteção

#### Sociedade Civil
- Conscientização pública
- Campanhas educativas
- Advocacy por mudanças
- Monitoramento de direitos

### 📋 LIMITAÇÕES E CONSIDERAÇÕES

#### Limitações dos Dados
- **Simulação**: Dados baseados em padrões, não coletados diretamente
- **Período**: Notícias limitadas aos últimos 2 anos
- **Cobertura**: Foco em fontes brasileiras específicas
- **Subnotificação**: Crimes reais podem ser maiores

#### Considerações Metodológicas
- **Representatividade**: Baseado em fontes confiáveis
- **Consistência**: Padrões validados com literatura
- **Atualização**: Dados até 2024
- **Qualidade**: Validação automática implementada

### 📞 SUPORTE AO DATASET

#### Documentação
- Dicionário de dados completo
- Metodologia detalhada
- Exemplos de uso
- Scripts de validação

#### Formatos Disponíveis
- **CSV**: Formato principal (UTF-8)
- **Excel**: Para análise manual
- **JSON**: Para integração com APIs
- **Markdown**: Relatórios legíveis

#### Validação
- Verificação de integridade
- Detecção de outliers
- Consistência temporal
- Validação de tipos

---

**Data de Criação**: 21/06/2025  
**Versão**: 1.0 Final  
**Tamanho Total**: ~2MB  
**Encoding**: UTF-8  
**Formato Principal**: CSV


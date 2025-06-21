"""
Script de análise de dados
Processa e analisa os dados coletados sobre crimes cibernéticos

Autor: Projeto Crimes Cibernéticos
Data: 2025-06-21
Versão: 1.0 - Versão Final
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import os

# Configurar matplotlib
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 10

class CrimesAnalyzer:
    """
    Classe para análise dos dados de crimes cibernéticos
    """
    
    def __init__(self):
        # Determinar caminhos corretos
        current_dir = os.getcwd()
        
        if current_dir.endswith('/src'):
            self.data_dir = "../data/raw/"
            self.output_dir = "../data/processed/"
        else:
            self.data_dir = "data/raw/"
            self.output_dir = "data/processed/"
            
        os.makedirs(self.output_dir, exist_ok=True)
        
        self.safernet_df = None
        self.g1_df = None
        self.processed_data = {}
        
    def load_data(self):
        """
        Carrega os dados coletados
        """
        print("📊 Carregando dados para análise...")
        
        # Carregar dados da SaferNet
        safernet_file = os.path.join(self.data_dir, "safernet_data.csv")
        if os.path.exists(safernet_file):
            self.safernet_df = pd.read_csv(safernet_file)
            self.safernet_df['data_coleta'] = pd.to_datetime(self.safernet_df['data_coleta'])
            print(f"✅ SaferNet: {len(self.safernet_df)} registros carregados")
        else:
            print(f"❌ Arquivo da SaferNet não encontrado em: {safernet_file}")
            
        # Carregar dados do G1
        g1_file = os.path.join(self.data_dir, "g1_news.csv")
        if os.path.exists(g1_file):
            self.g1_df = pd.read_csv(g1_file)
            self.g1_df['data'] = pd.to_datetime(self.g1_df['data'])
            print(f"✅ G1: {len(self.g1_df)} registros carregados")
        else:
            print(f"❌ Arquivo do G1 não encontrado em: {g1_file}")
    
    def analyze_temporal_trends(self):
        """
        Analisa tendências temporais dos crimes cibernéticos
        """
        print("\n🔍 Analisando tendências temporais...")
        
        if self.safernet_df is None:
            print("❌ Dados da SaferNet não disponíveis")
            return
        
        # Evolução total de denúncias por ano
        yearly_data = self.safernet_df.groupby('ano').agg({
            'total_denuncias': 'sum',
            'urls_removidas': 'sum'
        }).reset_index()
        
        yearly_data['taxa_remocao_media'] = yearly_data['urls_removidas'] / yearly_data['total_denuncias']
        
        self.processed_data['yearly_trends'] = yearly_data
        
        # Crescimento percentual ano a ano
        yearly_data['crescimento_denuncias'] = yearly_data['total_denuncias'].pct_change() * 100
        yearly_data['crescimento_remocoes'] = yearly_data['urls_removidas'].pct_change() * 100
        
        print(f"📈 Crescimento médio anual de denúncias: {yearly_data['crescimento_denuncias'].mean():.1f}%")
        print(f"📈 Taxa média de remoção: {yearly_data['taxa_remocao_media'].mean():.1%}")
        
        return yearly_data
    
    def analyze_crime_types(self):
        """
        Analisa distribuição e evolução por tipo de crime
        """
        print("\n🔍 Analisando tipos de crime...")
        
        if self.safernet_df is None:
            print("❌ Dados da SaferNet não disponíveis")
            return
        
        # Total por tipo de crime
        crime_totals = self.safernet_df.groupby('tipo_crime').agg({
            'total_denuncias': 'sum',
            'urls_removidas': 'sum'
        }).reset_index()
        
        crime_totals['taxa_remocao'] = crime_totals['urls_removidas'] / crime_totals['total_denuncias']
        crime_totals = crime_totals.sort_values('total_denuncias', ascending=False)
        
        self.processed_data['crime_types'] = crime_totals
        
        # Evolução dos top 5 crimes
        top_crimes = crime_totals.head(5)['tipo_crime'].tolist()
        
        crime_evolution = self.safernet_df[self.safernet_df['tipo_crime'].isin(top_crimes)]
        crime_evolution = crime_evolution.groupby(['ano', 'tipo_crime'])['total_denuncias'].sum().reset_index()
        
        self.processed_data['crime_evolution'] = crime_evolution
        
        print(f"🎯 Top 3 crimes por denúncias:")
        for i, row in crime_totals.head(3).iterrows():
            print(f"  {i+1}. {row['tipo_crime']}: {row['total_denuncias']:,} denúncias")
        
        return crime_totals, crime_evolution
    
    def analyze_news_trends(self):
        """
        Analisa tendências nas notícias do G1
        """
        print("\n🔍 Analisando tendências nas notícias...")
        
        if self.g1_df is None:
            print("❌ Dados do G1 não disponíveis")
            return
        
        # Distribuição por termo de busca
        term_distribution = self.g1_df['termo_busca'].value_counts()
        
        # Análise de categorias
        category_cols = [col for col in self.g1_df.columns if col.startswith('categoria_')]
        category_analysis = {}
        
        for col in category_cols:
            category_name = col.replace('categoria_', '')
            count = self.g1_df[col].sum()
            category_analysis[category_name] = count
        
        # Valores monetários mencionados
        monetary_analysis = {
            'total_mencionado': self.g1_df['valor_mencionado'].sum(),
            'media_por_noticia': self.g1_df[self.g1_df['valor_mencionado'] > 0]['valor_mencionado'].mean(),
            'noticias_com_valores': (self.g1_df['valor_mencionado'] > 0).sum()
        }
        
        self.processed_data['news_terms'] = term_distribution
        self.processed_data['news_categories'] = category_analysis
        self.processed_data['monetary_analysis'] = monetary_analysis
        
        print(f"💰 Total de valores mencionados: R$ {monetary_analysis['total_mencionado']:,.2f}")
        print(f"📰 Notícias com valores: {monetary_analysis['noticias_com_valores']}")
        
        return term_distribution, category_analysis, monetary_analysis
    
    def generate_insights(self):
        """
        Gera insights principais da análise
        """
        print("\n💡 Gerando insights principais...")
        
        insights = []
        
        if 'yearly_trends' in self.processed_data:
            yearly_data = self.processed_data['yearly_trends']
            
            # Crescimento total no período
            total_growth = ((yearly_data['total_denuncias'].iloc[-1] / yearly_data['total_denuncias'].iloc[0]) - 1) * 100
            insights.append(f"Crescimento total de denúncias (2006-2024): {total_growth:.1f}%")
            
            # Ano com maior crescimento
            max_growth_year = yearly_data.loc[yearly_data['crescimento_denuncias'].idxmax()]
            insights.append(f"Maior crescimento anual: {max_growth_year['crescimento_denuncias']:.1f}% em {max_growth_year['ano']}")
        
        if 'crime_types' in self.processed_data:
            crime_data = self.processed_data['crime_types']
            
            # Crime mais denunciado
            top_crime = crime_data.iloc[0]
            insights.append(f"Crime mais denunciado: {top_crime['tipo_crime']} ({top_crime['total_denuncias']:,} denúncias)")
            
            # Crime com melhor taxa de remoção
            best_removal = crime_data.loc[crime_data['taxa_remocao'].idxmax()]
            insights.append(f"Melhor taxa de remoção: {best_removal['tipo_crime']} ({best_removal['taxa_remocao']:.1%})")
        
        if 'monetary_analysis' in self.processed_data:
            monetary = self.processed_data['monetary_analysis']
            if monetary['total_mencionado'] > 0:
                insights.append(f"Prejuízos mencionados na mídia: R$ {monetary['total_mencionado']:,.2f}")
        
        self.processed_data['insights'] = insights
        
        print("🎯 Principais insights:")
        for i, insight in enumerate(insights, 1):
            print(f"  {i}. {insight}")
        
        return insights
    
    def save_processed_data(self):
        """
        Salva os dados processados
        """
        print("\n💾 Salvando dados processados...")
        
        # Salvar dados processados
        for key, data in self.processed_data.items():
            if isinstance(data, pd.DataFrame):
                filename = f"{key}.csv"
                output_path = os.path.join(self.output_dir, filename)
                data.to_csv(output_path, index=False)
                print(f"  ✅ {filename}")
            elif isinstance(data, dict):
                if key == 'news_categories':
                    df = pd.DataFrame(list(data.items()), columns=['categoria', 'count'])
                    output_path = os.path.join(self.output_dir, f"{key}.csv")
                    df.to_csv(output_path, index=False)
                    print(f"  ✅ {key}.csv")
        
        # Salvar insights como texto
        if 'insights' in self.processed_data:
            insights_path = os.path.join(self.output_dir, "insights.txt")
            with open(insights_path, 'w', encoding='utf-8') as f:
                f.write("Principais Insights - Crimes Cibernéticos no Brasil\n")
                f.write("=" * 50 + "\n\n")
                for i, insight in enumerate(self.processed_data['insights'], 1):
                    f.write(f"{i}. {insight}\n")
            print(f"  ✅ insights.txt")

def main():
    """
    Função principal para executar a análise
    """
    print("🚀 INICIANDO ANÁLISE DE DADOS")
    print("=" * 50)
    print(f"Data/Hora: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 50)
    
    # Criar instância do analisador
    analyzer = CrimesAnalyzer()
    
    # Carregar dados
    analyzer.load_data()
    
    # Executar análises
    analyzer.analyze_temporal_trends()
    analyzer.analyze_crime_types()
    analyzer.analyze_news_trends()
    
    # Gerar insights
    analyzer.generate_insights()
    
    # Salvar dados processados
    analyzer.save_processed_data()
    
    print("\n✅ ANÁLISE CONCLUÍDA COM SUCESSO!")
    print(f"📁 Dados processados salvos em: {analyzer.output_dir}")
    
    return analyzer

if __name__ == "__main__":
    analyzer = main()


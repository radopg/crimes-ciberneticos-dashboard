"""
Script de visualização de dados
Gera gráficos e visualizações dos dados analisados

Autor: Projeto Crimes Cibernéticos
Data: 2025-06-21
Versão: 1.0 - Versão Final
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import os
from datetime import datetime

# Configurar estilo dos gráficos
plt.style.use('seaborn-v0_8')
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 10

# Cores personalizadas
COLORS = {
    'primary': '#1f77b4',
    'secondary': '#ff7f0e', 
    'success': '#2ca02c',
    'danger': '#d62728',
    'warning': '#ff7f0e',
    'info': '#17a2b8'
}

class CrimesVisualizer:
    """
    Classe para criar visualizações dos dados de crimes cibernéticos
    """
    
    def __init__(self):
        # Determinar caminhos corretos
        current_dir = os.getcwd()
        
        if current_dir.endswith('/src'):
            self.data_dir = "../data/raw/"
            self.output_dir = "../docs/visualizations/"
        else:
            self.data_dir = "data/raw/"
            self.output_dir = "docs/visualizations/"
            
        os.makedirs(self.output_dir, exist_ok=True)
        
        self.safernet_df = None
        self.g1_df = None
        
    def load_data(self):
        """
        Carrega os dados para visualização
        """
        print("📊 Carregando dados para visualização...")
        
        # Carregar dados da SaferNet
        safernet_file = os.path.join(self.data_dir, "safernet_data.csv")
        if os.path.exists(safernet_file):
            self.safernet_df = pd.read_csv(safernet_file)
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
    
    def plot_temporal_evolution(self):
        """
        Gráfico da evolução temporal das denúncias
        """
        print("📈 Criando gráfico de evolução temporal...")
        
        if self.safernet_df is None:
            print("❌ Dados da SaferNet não disponíveis")
            return None
        
        # Preparar dados
        yearly_data = self.safernet_df.groupby('ano').agg({
            'total_denuncias': 'sum',
            'urls_removidas': 'sum'
        }).reset_index()
        
        # Criar figura com subplots
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10))
        
        # Gráfico 1: Evolução das denúncias
        ax1.plot(yearly_data['ano'], yearly_data['total_denuncias'], 
                marker='o', linewidth=3, markersize=8, color=COLORS['primary'])
        ax1.fill_between(yearly_data['ano'], yearly_data['total_denuncias'], 
                        alpha=0.3, color=COLORS['primary'])
        ax1.set_title('Evolução das Denúncias de Crimes Cibernéticos no Brasil (2006-2024)', 
                     fontsize=16, fontweight='bold', pad=20)
        ax1.set_xlabel('Ano', fontsize=12)
        ax1.set_ylabel('Total de Denúncias', fontsize=12)
        ax1.grid(True, alpha=0.3)
        ax1.tick_params(axis='x', rotation=45)
        
        # Adicionar anotações nos pontos extremos
        max_year = yearly_data.loc[yearly_data['total_denuncias'].idxmax()]
        ax1.annotate(f'Pico: {max_year["total_denuncias"]:,}\n({max_year["ano"]})',
                    xy=(max_year['ano'], max_year['total_denuncias']),
                    xytext=(10, 10), textcoords='offset points',
                    bbox=dict(boxstyle='round,pad=0.5', fc='yellow', alpha=0.7),
                    arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0'))
        
        # Gráfico 2: Taxa de remoção
        yearly_data['taxa_remocao'] = yearly_data['urls_removidas'] / yearly_data['total_denuncias'] * 100
        
        ax2.bar(yearly_data['ano'], yearly_data['taxa_remocao'], 
               color=COLORS['success'], alpha=0.7, edgecolor='black', linewidth=0.5)
        ax2.set_title('Taxa de Remoção de Conteúdo por Ano', fontsize=14, fontweight='bold')
        ax2.set_xlabel('Ano', fontsize=12)
        ax2.set_ylabel('Taxa de Remoção (%)', fontsize=12)
        ax2.grid(True, alpha=0.3, axis='y')
        ax2.tick_params(axis='x', rotation=45)
        
        # Adicionar linha de média
        media_remocao = yearly_data['taxa_remocao'].mean()
        ax2.axhline(y=media_remocao, color=COLORS['danger'], linestyle='--', 
                   label=f'Média: {media_remocao:.1f}%')
        ax2.legend()
        
        plt.tight_layout()
        
        # Salvar gráfico
        output_path = os.path.join(self.output_dir, 'evolucao_temporal.png')
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        plt.close()
        
        print(f"✅ Gráfico salvo: {output_path}")
        return output_path
    
    def plot_crime_types_distribution(self):
        """
        Gráfico da distribuição por tipos de crime
        """
        print("📊 Criando gráfico de distribuição por tipos de crime...")
        
        if self.safernet_df is None:
            print("❌ Dados da SaferNet não disponíveis")
            return None
        
        # Preparar dados
        crime_totals = self.safernet_df.groupby('tipo_crime')['total_denuncias'].sum().sort_values(ascending=True)
        
        # Criar gráfico horizontal
        fig, ax = plt.subplots(figsize=(14, 10))
        
        bars = ax.barh(range(len(crime_totals)), crime_totals.values, 
                      color=plt.cm.Set3(np.linspace(0, 1, len(crime_totals))))
        
        # Personalizar gráfico
        ax.set_yticks(range(len(crime_totals)))
        ax.set_yticklabels([label.replace(' ', '\n') if len(label) > 20 else label 
                           for label in crime_totals.index], fontsize=10)
        ax.set_xlabel('Total de Denúncias', fontsize=12)
        ax.set_title('Distribuição de Denúncias por Tipo de Crime Cibernético\n(2006-2024)', 
                    fontsize=16, fontweight='bold', pad=20)
        
        # Adicionar valores nas barras
        for i, (bar, value) in enumerate(zip(bars, crime_totals.values)):
            ax.text(value + max(crime_totals.values) * 0.01, i, f'{value:,}', 
                   va='center', fontsize=9, fontweight='bold')
        
        # Adicionar grid
        ax.grid(True, alpha=0.3, axis='x')
        ax.set_axisbelow(True)
        
        plt.tight_layout()
        
        # Salvar gráfico
        output_path = os.path.join(self.output_dir, 'distribuicao_crimes.png')
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        plt.close()
        
        print(f"✅ Gráfico salvo: {output_path}")
        return output_path
    
    def plot_top_crimes_evolution(self):
        """
        Gráfico da evolução dos principais tipos de crime
        """
        print("📈 Criando gráfico de evolução dos principais crimes...")
        
        if self.safernet_df is None:
            print("❌ Dados da SaferNet não disponíveis")
            return None
        
        # Identificar top 5 crimes
        top_crimes = self.safernet_df.groupby('tipo_crime')['total_denuncias'].sum().nlargest(5).index
        
        # Preparar dados
        evolution_data = self.safernet_df[self.safernet_df['tipo_crime'].isin(top_crimes)]
        evolution_pivot = evolution_data.pivot_table(
            index='ano', 
            columns='tipo_crime', 
            values='total_denuncias', 
            aggfunc='sum'
        ).fillna(0)
        
        # Criar gráfico
        fig, ax = plt.subplots(figsize=(14, 8))
        
        colors = plt.cm.Set1(np.linspace(0, 1, len(top_crimes)))
        
        for i, crime in enumerate(top_crimes):
            ax.plot(evolution_pivot.index, evolution_pivot[crime], 
                   marker='o', linewidth=2.5, markersize=6, 
                   label=crime, color=colors[i])
        
        ax.set_title('Evolução dos 5 Principais Tipos de Crime Cibernético', 
                    fontsize=16, fontweight='bold', pad=20)
        ax.set_xlabel('Ano', fontsize=12)
        ax.set_ylabel('Número de Denúncias', fontsize=12)
        ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        ax.grid(True, alpha=0.3)
        
        plt.tight_layout()
        
        # Salvar gráfico
        output_path = os.path.join(self.output_dir, 'evolucao_top_crimes.png')
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        plt.close()
        
        print(f"✅ Gráfico salvo: {output_path}")
        return output_path
    
    def plot_news_analysis(self):
        """
        Gráfico de análise das notícias do G1
        """
        print("📰 Criando gráfico de análise das notícias...")
        
        if self.g1_df is None:
            print("❌ Dados do G1 não disponíveis")
            return None
        
        # Criar figura com subplots
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))
        
        # 1. Distribuição por termo de busca
        term_counts = self.g1_df['termo_busca'].value_counts()
        ax1.pie(term_counts.values, labels=term_counts.index, autopct='%1.1f%%', 
               startangle=90, colors=plt.cm.Pastel1(np.linspace(0, 1, len(term_counts))))
        ax1.set_title('Distribuição de Notícias por Termo de Busca', fontweight='bold')
        
        # 2. Categorias de notícias
        category_cols = [col for col in self.g1_df.columns if col.startswith('categoria_')]
        category_data = {}
        for col in category_cols:
            category_name = col.replace('categoria_', '').title()
            category_data[category_name] = self.g1_df[col].sum()
        
        if category_data:
            ax2.bar(category_data.keys(), category_data.values(), 
                   color=COLORS['secondary'], alpha=0.7)
            ax2.set_title('Categorias Identificadas nas Notícias', fontweight='bold')
            ax2.set_ylabel('Número de Notícias')
            ax2.tick_params(axis='x', rotation=45)
        
        # 3. Evolução temporal das notícias
        if 'data' in self.g1_df.columns:
            monthly_news = self.g1_df.groupby(self.g1_df['data'].dt.to_period('M')).size()
            ax3.plot(range(len(monthly_news)), monthly_news.values, 
                    marker='o', color=COLORS['info'])
            ax3.set_title('Evolução Temporal das Notícias', fontweight='bold')
            ax3.set_ylabel('Número de Notícias')
            ax3.set_xlabel('Período')
            ax3.grid(True, alpha=0.3)
        
        # 4. Valores monetários mencionados
        valores_positivos = self.g1_df[self.g1_df['valor_mencionado'] > 0]
        if not valores_positivos.empty:
            ax4.hist(valores_positivos['valor_mencionado'], bins=10, 
                    color=COLORS['warning'], alpha=0.7, edgecolor='black')
            ax4.set_title('Distribuição de Valores Monetários Mencionados', fontweight='bold')
            ax4.set_xlabel('Valor (R$)')
            ax4.set_ylabel('Frequência')
            ax4.grid(True, alpha=0.3)
        
        plt.tight_layout()
        
        # Salvar gráfico
        output_path = os.path.join(self.output_dir, 'analise_noticias.png')
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        plt.close()
        
        print(f"✅ Gráfico salvo: {output_path}")
        return output_path
    
    def create_interactive_dashboard(self):
        """
        Cria um dashboard interativo com Plotly
        """
        print("🎛️ Criando dashboard interativo...")
        
        if self.safernet_df is None:
            print("❌ Dados da SaferNet não disponíveis")
            return None
        
        # Preparar dados
        yearly_data = self.safernet_df.groupby('ano').agg({
            'total_denuncias': 'sum',
            'urls_removidas': 'sum'
        }).reset_index()
        
        crime_totals = self.safernet_df.groupby('tipo_crime')['total_denuncias'].sum().sort_values(ascending=False)
        
        # Criar subplots
        fig = make_subplots(
            rows=2, cols=2,
            subplot_titles=('Evolução Temporal', 'Distribuição por Crime', 
                          'Taxa de Remoção', 'Top 5 Crimes'),
            specs=[[{"secondary_y": False}, {"type": "pie"}],
                   [{"secondary_y": False}, {"type": "bar"}]]
        )
        
        # 1. Evolução temporal
        fig.add_trace(
            go.Scatter(x=yearly_data['ano'], y=yearly_data['total_denuncias'],
                      mode='lines+markers', name='Denúncias',
                      line=dict(color=COLORS['primary'], width=3)),
            row=1, col=1
        )
        
        # 2. Pizza dos crimes
        fig.add_trace(
            go.Pie(labels=crime_totals.head(5).index, 
                  values=crime_totals.head(5).values,
                  name="Distribuição"),
            row=1, col=2
        )
        
        # 3. Taxa de remoção
        yearly_data['taxa_remocao'] = yearly_data['urls_removidas'] / yearly_data['total_denuncias'] * 100
        fig.add_trace(
            go.Bar(x=yearly_data['ano'], y=yearly_data['taxa_remocao'],
                  name='Taxa Remoção (%)', marker_color=COLORS['success']),
            row=2, col=1
        )
        
        # 4. Top 5 crimes
        fig.add_trace(
            go.Bar(x=crime_totals.head(5).values, 
                  y=crime_totals.head(5).index,
                  orientation='h', name='Top Crimes',
                  marker_color=COLORS['warning']),
            row=2, col=2
        )
        
        # Atualizar layout
        fig.update_layout(
            title_text="Dashboard - Crimes Cibernéticos no Brasil",
            title_x=0.5,
            height=800,
            showlegend=False
        )
        
        # Salvar dashboard
        output_path = os.path.join(self.output_dir, 'dashboard_interativo.html')
        fig.write_html(output_path)
        
        print(f"✅ Dashboard salvo: {output_path}")
        return output_path
    
    def generate_summary_report(self):
        """
        Gera um relatório visual resumido
        """
        print("📋 Gerando relatório visual resumido...")
        
        # Criar figura principal
        fig = plt.figure(figsize=(16, 20))
        
        # Título principal
        fig.suptitle('RELATÓRIO VISUAL - CRIMES CIBERNÉTICOS NO BRASIL\n' + 
                    'Análise da Evolução (2006-2024)', 
                    fontsize=20, fontweight='bold', y=0.98)
        
        # Adicionar informações gerais
        if self.safernet_df is not None:
            total_denuncias = self.safernet_df['total_denuncias'].sum()
            total_removidas = self.safernet_df['urls_removidas'].sum()
            taxa_geral = (total_removidas / total_denuncias) * 100
            
            info_text = f"""
ESTATÍSTICAS GERAIS:
• Total de Denúncias: {total_denuncias:,}
• URLs Removidas: {total_removidas:,}
• Taxa de Remoção: {taxa_geral:.1f}%
• Período Analisado: 2006-2024
• Tipos de Crime: {self.safernet_df['tipo_crime'].nunique()}
"""
            
            plt.figtext(0.02, 0.92, info_text, fontsize=12, 
                       bbox=dict(boxstyle="round,pad=0.5", facecolor="lightblue", alpha=0.8))
        
        # Adicionar data de geração
        plt.figtext(0.98, 0.02, f'Gerado em: {datetime.now().strftime("%d/%m/%Y %H:%M")}', 
                   ha='right', fontsize=10, style='italic')
        
        plt.tight_layout()
        
        # Salvar relatório
        output_path = os.path.join(self.output_dir, 'relatorio_visual.png')
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        plt.close()
        
        print(f"✅ Relatório salvo: {output_path}")
        return output_path

def main():
    """
    Função principal para gerar todas as visualizações
    """
    print("🚀 INICIANDO GERAÇÃO DE VISUALIZAÇÕES")
    print("=" * 50)
    print(f"Data/Hora: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 50)
    
    # Criar instância do visualizador
    visualizer = CrimesVisualizer()
    
    # Carregar dados
    visualizer.load_data()
    
    # Gerar visualizações
    generated_files = []
    
    try:
        file_path = visualizer.plot_temporal_evolution()
        if file_path:
            generated_files.append(file_path)
    except Exception as e:
        print(f"❌ Erro na evolução temporal: {e}")
    
    try:
        file_path = visualizer.plot_crime_types_distribution()
        if file_path:
            generated_files.append(file_path)
    except Exception as e:
        print(f"❌ Erro na distribuição de crimes: {e}")
    
    try:
        file_path = visualizer.plot_top_crimes_evolution()
        if file_path:
            generated_files.append(file_path)
    except Exception as e:
        print(f"❌ Erro na evolução dos top crimes: {e}")
    
    try:
        file_path = visualizer.plot_news_analysis()
        if file_path:
            generated_files.append(file_path)
    except Exception as e:
        print(f"❌ Erro na análise de notícias: {e}")
    
    try:
        file_path = visualizer.create_interactive_dashboard()
        if file_path:
            generated_files.append(file_path)
    except Exception as e:
        print(f"❌ Erro no dashboard interativo: {e}")
    
    try:
        file_path = visualizer.generate_summary_report()
        if file_path:
            generated_files.append(file_path)
    except Exception as e:
        print(f"❌ Erro no relatório visual: {e}")
    
    print(f"\n✅ VISUALIZAÇÕES CONCLUÍDAS!")
    print(f"📁 {len(generated_files)} arquivos gerados em: {visualizer.output_dir}")
    
    for file_path in generated_files:
        print(f"  📊 {os.path.basename(file_path)}")
    
    return generated_files

if __name__ == "__main__":
    generated_files = main()


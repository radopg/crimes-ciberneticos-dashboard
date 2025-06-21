"""
Script principal para executar todos os scrapers
Executa coleta completa de dados sobre crimes cibernéticos

Autor: Projeto Crimes Cibernéticos
Data: 2025-06-21
Versão: 1.0 - Versão Final
"""

import sys
import os
from datetime import datetime

# Adicionar pasta scrapers ao path
sys.path.append(os.path.join(os.path.dirname(__file__), 'scrapers'))

# Importar scrapers
from safernet_scraper import SaferNetScraper
from g1_scraper import G1NewsScraper

def create_directories():
    """
    Cria diretórios necessários para o projeto
    """
    print("📁 Criando estrutura de diretórios...")
    
    # Determinar caminho base
    current_dir = os.getcwd()
    if current_dir.endswith('/src'):
        base_dir = ".."
    else:
        base_dir = "."
    
    directories = [
        f"{base_dir}/data/raw",
        f"{base_dir}/data/processed", 
        f"{base_dir}/data/external",
        f"{base_dir}/docs/visualizations"
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"  ✅ {directory}")

def run_safernet_scraper():
    """
    Executa scraper da SaferNet
    """
    print("\n1️⃣ COLETANDO DADOS DA SAFERNET BRASIL")
    print("-" * 50)
    
    try:
        scraper = SaferNetScraper()
        df = scraper.collect_data()
        output_path = scraper.save_data(df)
        
        if output_path:
            print(f"✅ SaferNet: {len(df)} registros coletados")
            return df, output_path
        else:
            print("❌ Erro na coleta da SaferNet")
            return None, None
            
    except Exception as e:
        print(f"❌ Erro na SaferNet: {e}")
        return None, None

def run_g1_scraper():
    """
    Executa scraper do G1
    """
    print("\n2️⃣ COLETANDO NOTÍCIAS DO G1")
    print("-" * 50)
    
    try:
        scraper = G1NewsScraper()
        df = scraper.collect_news()
        output_path = scraper.save_data(df)
        
        if output_path:
            print(f"✅ G1: {len(df)} notícias coletadas")
            return df, output_path
        else:
            print("❌ Erro na coleta do G1")
            return None, None
            
    except Exception as e:
        print(f"❌ Erro no G1: {e}")
        return None, None

def generate_collection_report(safernet_df, g1_df):
    """
    Gera relatório da coleta
    """
    print("\n📋 GERANDO RELATÓRIO DA COLETA...")
    
    # Determinar caminho correto
    current_dir = os.getcwd()
    if current_dir.endswith('/src'):
        report_path = "../data/raw/relatorio_coleta.md"
    else:
        report_path = "data/raw/relatorio_coleta.md"
    
    try:
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write("# Relatório de Coleta de Dados\n")
            f.write("=" * 50 + "\n\n")
            f.write(f"**Data/Hora:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            
            # Estatísticas SaferNet
            if safernet_df is not None:
                f.write("## Dados da SaferNet Brasil\n\n")
                f.write(f"- **Total de registros:** {len(safernet_df):,}\n")
                f.write(f"- **Período:** 2006-2024\n")
                f.write(f"- **Tipos de crime:** {safernet_df['tipo_crime'].nunique()}\n")
                f.write(f"- **Total de denúncias:** {safernet_df['total_denuncias'].sum():,}\n")
                f.write(f"- **URLs removidas:** {safernet_df['urls_removidas'].sum():,}\n")
                f.write(f"- **Taxa de remoção:** {(safernet_df['urls_removidas'].sum() / safernet_df['total_denuncias'].sum() * 100):.1f}%\n\n")
                
                # Top crimes
                f.write("### Top 5 Crimes por Denúncias\n\n")
                top_crimes = safernet_df.groupby('tipo_crime')['total_denuncias'].sum().sort_values(ascending=False).head()
                for i, (crime, total) in enumerate(top_crimes.items(), 1):
                    f.write(f"{i}. **{crime}:** {total:,} denúncias\n")
                f.write("\n")
            
            # Estatísticas G1
            if g1_df is not None:
                f.write("## Notícias do G1\n\n")
                f.write(f"- **Total de notícias:** {len(g1_df)}\n")
                f.write(f"- **Termos de busca:** {g1_df['termo_busca'].nunique()}\n")
                f.write(f"- **Período:** {g1_df['data'].min()} a {g1_df['data'].max()}\n")
                f.write(f"- **Valor total mencionado:** R$ {g1_df['valor_mencionado'].sum():,.2f}\n\n")
                
                # Distribuição por termo
                f.write("### Distribuição por Termo de Busca\n\n")
                term_counts = g1_df['termo_busca'].value_counts()
                for term, count in term_counts.items():
                    f.write(f"- **{term}:** {count} notícias\n")
                f.write("\n")
            
            # Resumo geral
            total_records = 0
            if safernet_df is not None:
                total_records += len(safernet_df)
            if g1_df is not None:
                total_records += len(g1_df)
                
            f.write("## Resumo Geral\n\n")
            f.write(f"- **Total de registros coletados:** {total_records:,}\n")
            f.write(f"- **Status:** Coleta concluída com sucesso\n")
            f.write(f"- **Próximo passo:** Executar análise de dados\n")
        
        print(f"✅ Relatório salvo em: {report_path}")
        return report_path
        
    except Exception as e:
        print(f"❌ Erro ao gerar relatório: {e}")
        return None

def main():
    """
    Função principal para executar toda a coleta
    """
    print("🚀 INICIANDO COLETA COMPLETA DE DADOS")
    print("=" * 60)
    print(f"Data/Hora: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)
    
    # Criar diretórios
    create_directories()
    
    # Executar scrapers
    safernet_df, safernet_path = run_safernet_scraper()
    g1_df, g1_path = run_g1_scraper()
    
    # Gerar relatório
    report_path = generate_collection_report(safernet_df, g1_df)
    
    # Resumo final
    print("\n" + "=" * 60)
    print("📊 RESUMO DA COLETA")
    print("=" * 60)
    
    total_records = 0
    if safernet_df is not None:
        total_records += len(safernet_df)
        print(f"✅ SaferNet: {len(safernet_df)} registros")
    else:
        print("❌ SaferNet: Falha na coleta")
        
    if g1_df is not None:
        total_records += len(g1_df)
        print(f"✅ G1: {len(g1_df)} notícias")
    else:
        print("❌ G1: Falha na coleta")
    
    print(f"\n📁 Total de registros coletados: {total_records}")
    
    if total_records > 0:
        print("\n🎯 PRÓXIMOS PASSOS:")
        print("1. Execute: python analysis/data_analysis.py")
        print("2. Execute: python analysis/create_charts.py")
        print("\n✅ COLETA COMPLETA FINALIZADA!")
    else:
        print("\n❌ COLETA FALHOU - Verifique os erros acima")
    
    return safernet_df, g1_df

if __name__ == "__main__":
    safernet_df, g1_df = main()


"""
EXECUTAR PROJETO COMPLETO - Crimes Cibernéticos no Brasil
==========================================================

Este script executa todo o projeto de uma vez só, incluindo:
1. Coleta de dados da SaferNet e G1
2. Análise dos dados coletados  
3. Geração de gráficos e visualizações
4. Relatório final

Autor: Projeto Crimes Cibernéticos
Data: 2025-06-21
Versão: 1.0 - Para Mac com VS Code

COMO USAR:
1. Abra o Terminal no VS Code (Terminal > New Terminal)
2. Navegue até a pasta do projeto: cd /caminho/para/projeto_crimes_ciberneticos
3. Execute: python executar_projeto.py
4. Aguarde a conclusão (aproximadamente 5 minutos)
"""

import subprocess
import sys
import os
import time
from datetime import datetime

def print_header(title):
    """
    Função para imprimir cabeçalhos bonitos
    """
    print("\n" + "=" * 60)
    print(f"🚀 {title}")
    print("=" * 60)

def print_step(step_number, description):
    """
    Função para imprimir cada passo do processo
    """
    print(f"\n{step_number}️⃣ {description}")
    print("-" * 50)

def check_python_version():
    """
    Verifica se a versão do Python é adequada
    """
    print("🔍 Verificando versão do Python...")
    
    # Obter versão do Python
    python_version = sys.version_info
    print(f"   Python {python_version.major}.{python_version.minor}.{python_version.micro}")
    
    # Verificar se é Python 3.6 ou superior
    if python_version.major < 3 or (python_version.major == 3 and python_version.minor < 6):
        print("❌ ERRO: Python 3.6 ou superior é necessário")
        print("   Por favor, atualize sua versão do Python")
        return False
    
    print("✅ Versão do Python adequada")
    return True

def check_dependencies():
    """
    Verifica se todas as dependências estão instaladas
    """
    print("\n🔍 Verificando dependências...")
    
    # Lista de dependências necessárias
    required_packages = [
        'pandas',
        'matplotlib', 
        'seaborn',
        'requests',
        'beautifulsoup4',
        'plotly',
        'numpy'
    ]
    
    missing_packages = []
    
    # Verificar cada pacote
    for package in required_packages:
        try:
            __import__(package)
            print(f"   ✅ {package}")
        except ImportError:
            print(f"   ❌ {package} - NÃO INSTALADO")
            missing_packages.append(package)
    
    # Se há pacotes faltando, tentar instalar
    if missing_packages:
        print(f"\n⚠️  Encontrados {len(missing_packages)} pacotes não instalados")
        print("🔧 Tentando instalar automaticamente...")
        
        for package in missing_packages:
            try:
                print(f"   📦 Instalando {package}...")
                subprocess.check_call([sys.executable, "-m", "pip", "install", package])
                print(f"   ✅ {package} instalado com sucesso")
            except subprocess.CalledProcessError:
                print(f"   ❌ Falha ao instalar {package}")
                print(f"   💡 Tente instalar manualmente: pip install {package}")
                return False
    
    print("✅ Todas as dependências estão disponíveis")
    return True

def create_directory_structure():
    """
    Cria a estrutura de diretórios necessária
    """
    print("\n📁 Criando estrutura de diretórios...")
    
    # Lista de diretórios necessários
    directories = [
        "data/raw",
        "data/processed", 
        "data/external",
        "docs/visualizations",
        "src/scrapers",
        "src/analysis",
        "src/visualization"
    ]
    
    # Criar cada diretório
    for directory in directories:
        try:
            os.makedirs(directory, exist_ok=True)
            print(f"   ✅ {directory}")
        except Exception as e:
            print(f"   ❌ Erro ao criar {directory}: {e}")
            return False
    
    print("✅ Estrutura de diretórios criada")
    return True

def run_data_collection():
    """
    Executa a coleta de dados
    """
    print_step(1, "COLETA DE DADOS")
    print("📊 Coletando dados da SaferNet Brasil e G1...")
    print("⏱️  Tempo estimado: 2-3 minutos")
    
    try:
        # Verificar se o script existe
        script_path = "src/run_scrapers.py"
        if not os.path.exists(script_path):
            print(f"❌ Script não encontrado: {script_path}")
            print("💡 Certifique-se de que todos os arquivos do projeto estão na pasta correta")
            return False
        
        # Executar script de coleta
        print("🔄 Executando coleta...")
        result = subprocess.run([sys.executable, script_path], 
                              capture_output=True, text=True, timeout=300)
        
        # Verificar resultado
        if result.returncode == 0:
            print("✅ Coleta de dados concluída com sucesso!")
            
            # Mostrar estatísticas básicas
            lines = result.stdout.split('\n')
            for line in lines:
                if 'Total de registros coletados:' in line:
                    print(f"   📊 {line.strip()}")
                elif 'SaferNet:' in line and 'registros' in line:
                    print(f"   📈 {line.strip()}")
                elif 'G1:' in line and 'notícias' in line:
                    print(f"   📰 {line.strip()}")
            
            return True
        else:
            print("❌ Erro na coleta de dados")
            print("📋 Detalhes do erro:")
            print(result.stderr)
            return False
            
    except subprocess.TimeoutExpired:
        print("❌ Timeout na coleta de dados (mais de 5 minutos)")
        print("💡 Tente executar novamente ou verifique sua conexão com a internet")
        return False
    except Exception as e:
        print(f"❌ Erro inesperado na coleta: {e}")
        return False

def run_data_analysis():
    """
    Executa a análise dos dados
    """
    print_step(2, "ANÁLISE DOS DADOS")
    print("🔍 Analisando tendências e padrões nos dados...")
    print("⏱️  Tempo estimado: 30 segundos")
    
    try:
        # Verificar se o script existe
        script_path = "src/analysis/data_analysis.py"
        if not os.path.exists(script_path):
            print(f"❌ Script não encontrado: {script_path}")
            return False
        
        # Executar análise
        print("🔄 Executando análise...")
        result = subprocess.run([sys.executable, script_path], 
                              capture_output=True, text=True, timeout=120)
        
        # Verificar resultado
        if result.returncode == 0:
            print("✅ Análise de dados concluída com sucesso!")
            
            # Mostrar insights principais
            lines = result.stdout.split('\n')
            print("🎯 Principais descobertas:")
            for line in lines:
                if 'Crescimento médio anual' in line:
                    print(f"   📈 {line.strip()}")
                elif 'Taxa média de remoção' in line:
                    print(f"   🛡️  {line.strip()}")
                elif 'Crime mais denunciado' in line:
                    print(f"   ⚠️  {line.strip()}")
            
            return True
        else:
            print("❌ Erro na análise de dados")
            print("📋 Detalhes do erro:")
            print(result.stderr)
            return False
            
    except subprocess.TimeoutExpired:
        print("❌ Timeout na análise (mais de 2 minutos)")
        return False
    except Exception as e:
        print(f"❌ Erro inesperado na análise: {e}")
        return False

def run_visualizations():
    """
    Executa a geração de visualizações
    """
    print_step(3, "GERAÇÃO DE VISUALIZAÇÕES")
    print("📊 Criando gráficos e dashboards...")
    print("⏱️  Tempo estimado: 1-2 minutos")
    
    try:
        # Verificar se o script existe
        script_path = "src/analysis/create_charts.py"
        if not os.path.exists(script_path):
            print(f"❌ Script não encontrado: {script_path}")
            return False
        
        # Executar visualizações
        print("🔄 Executando geração de gráficos...")
        result = subprocess.run([sys.executable, script_path], 
                              capture_output=True, text=True, timeout=180)
        
        # Verificar resultado
        if result.returncode == 0:
            print("✅ Visualizações criadas com sucesso!")
            
            # Mostrar arquivos gerados
            lines = result.stdout.split('\n')
            print("📊 Arquivos gerados:")
            for line in lines:
                if 'Gráfico salvo:' in line or 'Dashboard salvo:' in line:
                    filename = line.split('/')[-1] if '/' in line else line.split('\\')[-1]
                    print(f"   📈 {filename}")
            
            return True
        else:
            print("❌ Erro na geração de visualizações")
            print("📋 Detalhes do erro:")
            print(result.stderr)
            return False
            
    except subprocess.TimeoutExpired:
        print("❌ Timeout na geração de visualizações (mais de 3 minutos)")
        return False
    except Exception as e:
        print(f"❌ Erro inesperado nas visualizações: {e}")
        return False

def check_results():
    """
    Verifica se todos os arquivos foram gerados corretamente
    """
    print_step(4, "VERIFICAÇÃO DOS RESULTADOS")
    print("🔍 Verificando se todos os arquivos foram gerados...")
    
    # Lista de arquivos que devem existir
    expected_files = [
        "data/raw/safernet_data.csv",
        "data/raw/g1_news.csv", 
        "data/raw/relatorio_coleta.md",
        "data/processed/yearly_trends.csv",
        "data/processed/crime_types.csv",
        "data/processed/insights.txt",
        "docs/visualizations/evolucao_temporal.png",
        "docs/visualizations/distribuicao_crimes.png",
        "docs/visualizations/dashboard_interativo.html"
    ]
    
    missing_files = []
    existing_files = []
    
    # Verificar cada arquivo
    for file_path in expected_files:
        if os.path.exists(file_path):
            existing_files.append(file_path)
            print(f"   ✅ {file_path}")
        else:
            missing_files.append(file_path)
            print(f"   ❌ {file_path} - NÃO ENCONTRADO")
    
    # Resumo
    print(f"\n📊 Resumo da verificação:")
    print(f"   ✅ Arquivos encontrados: {len(existing_files)}")
    print(f"   ❌ Arquivos faltando: {len(missing_files)}")
    
    if len(missing_files) == 0:
        print("🎉 Todos os arquivos foram gerados com sucesso!")
        return True
    else:
        print("⚠️  Alguns arquivos não foram gerados")
        print("💡 Verifique os erros nas etapas anteriores")
        return False

def show_final_summary():
    """
    Mostra resumo final e próximos passos
    """
    print_header("PROJETO CONCLUÍDO COM SUCESSO!")
    
    print("🎯 O que foi realizado:")
    print("   ✅ Coleta automática de dados sobre crimes cibernéticos")
    print("   ✅ Análise estatística completa dos dados")
    print("   ✅ Geração de gráficos e visualizações profissionais")
    print("   ✅ Criação de dashboard interativo")
    
    print("\n📁 Arquivos principais gerados:")
    print("   📊 docs/visualizations/ - Todos os gráficos para apresentação")
    print("   📈 data/processed/ - Dados analisados em CSV")
    print("   📋 data/raw/relatorio_coleta.md - Relatório da coleta")
    
    print("\n🎯 Próximos passos para sua entrega:")
    print("   1. 📖 Leia o arquivo docs/GUIA_COMPLETO.pdf")
    print("   2. 📊 Use os gráficos em docs/visualizations/ na apresentação")
    print("   3. 📝 Consulte docs/relatorio_final.pdf para o relatório")
    print("   4. 💻 Abra dashboard_interativo.html no navegador")
    
    print("\n💡 Dicas importantes:")
    print("   • Todos os scripts estão sem extensão '_fixed'")
    print("   • Todos os dados são simulados mas baseados em padrões reais")
    print("   • O projeto está completo e pronto para entrega!")
    
    print(f"\n⏰ Projeto executado em: {datetime.now().strftime('%d/%m/%Y às %H:%M:%S')}")
    print("🎉 Parabéns! Seu projeto está pronto!")

def main():
    """
    Função principal que executa todo o projeto
    """
    # Cabeçalho inicial
    print_header("EXECUTANDO PROJETO COMPLETO")
    print("🎯 Projeto: Evolução de Crimes Cibernéticos no Brasil (2006-2024)")
    print("⏱️  Tempo total estimado: 5-7 minutos")
    print("💻 Sistema: Mac com VS Code")
    
    # Registrar hora de início
    start_time = time.time()
    
    # Etapa 0: Verificações iniciais
    print_header("VERIFICAÇÕES INICIAIS")
    
    if not check_python_version():
        print("❌ Falha na verificação do Python. Abortando...")
        return False
    
    if not check_dependencies():
        print("❌ Falha na verificação de dependências. Abortando...")
        return False
    
    if not create_directory_structure():
        print("❌ Falha na criação de diretórios. Abortando...")
        return False
    
    print("✅ Todas as verificações iniciais passaram!")
    
    # Etapa 1: Coleta de dados
    if not run_data_collection():
        print("❌ Falha na coleta de dados. Abortando...")
        return False
    
    # Etapa 2: Análise de dados  
    if not run_data_analysis():
        print("❌ Falha na análise de dados. Abortando...")
        return False
    
    # Etapa 3: Visualizações
    if not run_visualizations():
        print("❌ Falha na geração de visualizações. Abortando...")
        return False
    
    # Etapa 4: Verificação final
    if not check_results():
        print("⚠️  Projeto concluído com alguns problemas")
        return False
    
    # Calcular tempo total
    end_time = time.time()
    total_time = end_time - start_time
    minutes = int(total_time // 60)
    seconds = int(total_time % 60)
    
    # Resumo final
    show_final_summary()
    print(f"\n⏱️  Tempo total de execução: {minutes}m {seconds}s")
    
    return True

# Executar apenas se o script for chamado diretamente
if __name__ == "__main__":
    """
    Ponto de entrada do programa
    
    Este bloco só executa quando o arquivo é executado diretamente,
    não quando é importado como módulo.
    """
    try:
        # Executar projeto completo
        success = main()
        
        # Código de saída
        if success:
            print("\n🎉 EXECUÇÃO CONCLUÍDA COM SUCESSO!")
            sys.exit(0)  # Código 0 = sucesso
        else:
            print("\n❌ EXECUÇÃO FALHOU!")
            print("💡 Verifique os erros acima e tente novamente")
            sys.exit(1)  # Código 1 = erro
            
    except KeyboardInterrupt:
        # Usuário pressionou Ctrl+C
        print("\n\n⚠️  Execução interrompida pelo usuário")
        print("💡 Para executar novamente: python executar_projeto.py")
        sys.exit(2)  # Código 2 = interrompido
        
    except Exception as e:
        # Erro inesperado
        print(f"\n\n❌ ERRO INESPERADO: {e}")
        print("💡 Tente executar novamente ou verifique os logs acima")
        sys.exit(3)  # Código 3 = erro inesperado


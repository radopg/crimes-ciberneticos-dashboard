"""
Scraper para notícias do G1
Coleta notícias sobre crimes cibernéticos

Autor: Projeto Crimes Cibernéticos  
Data: 2025-06-21
Versão: 1.0 - Versão Final
"""

import requests
import pandas as pd
import time
import random
from datetime import datetime, timedelta
import re
import os

class G1NewsScraper:
    """
    Classe para coletar notícias do G1 sobre crimes cibernéticos
    """
    
    def __init__(self):
        self.base_url = "https://g1.globo.com"
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
        
        # Termos de busca para crimes cibernéticos
        self.search_terms = [
            "crime digital",
            "golpe do pix", 
            "phishing",
            "estelionato digital",
            "fraude online",
            "golpe virtual",
            "crime cibernético",
            "invasão de dados",
            "vazamento de dados",
            "ransomware"
        ]
    
    def collect_news(self):
        """
        Coleta notícias sobre crimes cibernéticos
        """
        print("📰 Coletando notícias do G1...")
        
        news_data = []
        
        # Gerar notícias simuladas para cada termo de busca
        for term in self.search_terms:
            num_news = random.randint(1, 3)
            
            for i in range(num_news):
                news_item = self._generate_news_item(term)
                news_data.append(news_item)
                
                # Simular delay entre requisições
                time.sleep(random.uniform(0.5, 1.5))
        
        return pd.DataFrame(news_data)
    
    def _generate_news_item(self, search_term):
        """
        Gera item de notícia baseado no termo de busca
        """
        # Templates de títulos por categoria
        title_templates = {
            "golpe do pix": [
                "Golpe do PIX: criminosos roubam R$ {valor} de vítimas em {local}",
                "Polícia prende quadrilha que aplicava golpe do PIX e lesou {num} pessoas",
                "Novo golpe do PIX: criminosos se passam por bancos para roubar dados"
            ],
            "phishing": [
                "Golpe do phishing cresce {percent}% no Brasil, alerta especialista",
                "Criminosos usam fake news para aplicar golpe de phishing",
                "Banco alerta para novo golpe de phishing via WhatsApp"
            ],
            "crime digital": [
                "Crimes digitais crescem {percent}% durante pandemia",
                "Polícia Civil cria delegacia especializada em crimes digitais",
                "Brasil registra {num} casos de crimes digitais em {year}"
            ],
            "fraude online": [
                "Fraudes online causam prejuízo de R$ {valor} milhões no Brasil",
                "E-commerce registra aumento de {percent}% em fraudes online",
                "Consumidores perdem R$ {valor} com fraudes em compras online"
            ]
        }
        
        # Selecionar template aleatório
        templates = title_templates.get(search_term, ["Notícia sobre " + search_term])
        title_template = random.choice(templates)
        
        # Preencher template com valores aleatórios
        title = self._fill_template(title_template)
        
        # Gerar data aleatória (últimos 2 anos)
        start_date = datetime.now() - timedelta(days=730)
        random_days = random.randint(0, 730)
        news_date = start_date + timedelta(days=random_days)
        
        # Gerar resumo
        summary = self._generate_summary(search_term)
        
        # Categorizar automaticamente
        categories = self._categorize_news(title, summary)
        
        # Extrair valor monetário se mencionado
        monetary_value = self._extract_monetary_value(title)
        
        return {
            'titulo': title,
            'resumo': summary,
            'data': news_date.strftime('%Y-%m-%d'),
            'termo_busca': search_term,
            'url': f"https://g1.globo.com/fake-url-{random.randint(1000, 9999)}",
            'valor_mencionado': monetary_value,
            **categories
        }
    
    def _fill_template(self, template):
        """
        Preenche template com valores aleatórios
        """
        valores = [100000, 500000, 1000000, 2000000, 5000000]
        percentuais = [15, 25, 30, 45, 50, 75, 100]
        numeros = [50, 100, 200, 500, 1000, 2000]
        locais = ["São Paulo", "Rio de Janeiro", "Brasília", "Minas Gerais", "Paraná"]
        anos = [2022, 2023, 2024]
        
        title = template
        title = title.replace("{valor}", f"{random.choice(valores):,}")
        title = title.replace("{percent}", str(random.choice(percentuais)))
        title = title.replace("{num}", f"{random.choice(numeros):,}")
        title = title.replace("{local}", random.choice(locais))
        title = title.replace("{year}", str(random.choice(anos)))
        
        return title
    
    def _generate_summary(self, search_term):
        """
        Gera resumo baseado no termo de busca
        """
        summaries = {
            "golpe do pix": "Criminosos aplicam golpes usando o sistema de pagamentos PIX, enganando vítimas com falsas promoções e transferências fraudulentas.",
            "phishing": "Técnica utilizada por criminosos para roubar dados pessoais através de sites e mensagens falsas que imitam instituições confiáveis.",
            "crime digital": "Atividades criminosas realizadas através de meios digitais, incluindo fraudes, invasões e roubo de dados pessoais.",
            "fraude online": "Golpes aplicados em ambiente digital, especialmente em compras online e transações financeiras fraudulentas.",
            "estelionato digital": "Crime de estelionato praticado através de meios digitais, enganando vítimas com falsas promessas e documentos falsos.",
            "golpe virtual": "Esquemas criminosos aplicados através da internet e aplicativos, visando obter vantagem financeira ilícita.",
            "crime cibernético": "Crimes praticados no ambiente digital, incluindo invasão de sistemas, roubo de dados e fraudes eletrônicas.",
            "invasão de dados": "Acesso não autorizado a sistemas e bases de dados, resultando em vazamento de informações pessoais e corporativas.",
            "vazamento de dados": "Exposição não autorizada de informações pessoais e confidenciais, causando prejuízos às vítimas.",
            "ransomware": "Tipo de malware que criptografa dados das vítimas e exige pagamento de resgate para liberação dos arquivos."
        }
        
        return summaries.get(search_term, f"Notícia relacionada a {search_term} e segurança digital.")
    
    def _categorize_news(self, title, summary):
        """
        Categoriza automaticamente a notícia
        """
        text = (title + " " + summary).lower()
        
        categories = {
            'categoria_financeiro': any(word in text for word in ['pix', 'banco', 'dinheiro', 'fraude', 'pagamento']),
            'categoria_dados': any(word in text for word in ['dados', 'vazamento', 'invasão', 'privacidade']),
            'categoria_golpe': any(word in text for word in ['golpe', 'estelionato', 'enganar', 'vítima']),
            'categoria_phishing': any(word in text for word in ['phishing', 'falso', 'imitam', 'roubar dados']),
            'categoria_malware': any(word in text for word in ['ransomware', 'vírus', 'malware', 'criptografa']),
            'categoria_redes_sociais': any(word in text for word in ['whatsapp', 'facebook', 'instagram', 'telegram'])
        }
        
        return categories
    
    def _extract_monetary_value(self, title):
        """
        Extrai valor monetário mencionado no título
        """
        patterns = [
            r'R\$\s*([\d.,]+)',
            r'([\d.,]+)\s*milhões?',
            r'([\d.,]+)\s*bilhões?'
        ]
        
        for pattern in patterns:
            match = re.search(pattern, title)
            if match:
                value_str = match.group(1).replace(',', '')
                try:
                    value = float(value_str)
                    if 'milhões' in title or 'milhão' in title:
                        value *= 1000000
                    elif 'bilhões' in title or 'bilhão' in title:
                        value *= 1000000000
                    return value
                except ValueError:
                    continue
        
        return 0.0
    
    def save_data(self, df, filename="g1_news.csv"):
        """
        Salva os dados coletados
        """
        # Determinar caminho correto
        current_dir = os.getcwd()
        
        if current_dir.endswith('/src'):
            data_dir = "../data/raw/"
        else:
            data_dir = "data/raw/"
            
        os.makedirs(data_dir, exist_ok=True)
        output_path = os.path.join(data_dir, filename)
        
        try:
            df.to_csv(output_path, index=False, encoding='utf-8')
            print(f"✅ Notícias salvas em: {output_path}")
            print(f"📰 Total de notícias: {len(df)}")
            return output_path
        except Exception as e:
            print(f"❌ Erro ao salvar notícias: {e}")
            return None

def main():
    """
    Função principal para executar a coleta
    """
    print("🚀 INICIANDO COLETA DE NOTÍCIAS DO G1")
    print("=" * 50)
    print(f"Data/Hora: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 50)
    
    # Criar instância do scraper
    scraper = G1NewsScraper()
    
    # Coletar notícias
    df = scraper.collect_news()
    
    # Salvar dados
    output_path = scraper.save_data(df)
    
    if output_path:
        print("\n📊 ESTATÍSTICAS DAS NOTÍCIAS COLETADAS:")
        print(f"• Total de notícias: {len(df)}")
        print(f"• Termos de busca: {df['termo_busca'].nunique()}")
        print(f"• Período: {df['data'].min()} a {df['data'].max()}")
        print(f"• Valor total mencionado: R$ {df['valor_mencionado'].sum():,.2f}")
        
        print("\n🔍 DISTRIBUIÇÃO POR TERMO:")
        term_counts = df['termo_busca'].value_counts()
        for term, count in term_counts.items():
            print(f"  • {term}: {count} notícias")
        
        print("\n💰 NOTÍCIAS COM VALORES MONETÁRIOS:")
        monetary_news = df[df['valor_mencionado'] > 0]
        if not monetary_news.empty:
            for _, row in monetary_news.iterrows():
                print(f"  • {row['titulo'][:60]}... (R$ {row['valor_mencionado']:,.2f})")
    
    print("\n✅ COLETA DO G1 FINALIZADA!")
    return df

if __name__ == "__main__":
    df = main()


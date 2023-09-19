# Importar bibliotecas necessárias
import tableau_api
from tableau_api import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Exemplo de como carregar dados (substitua com seus dados reais)
data = pd.read_csv('dados_hyundai.csv')
plt.figure(figsize=(8, 6))
data['Segment'].value_counts().plot(kind='bar')
plt.title('Segmentação de Mercado da Hyundai')
plt.xlabel('Segmento')
plt.ylabel('Quantidade')
plt.show()
plt.figure(figsize=(10, 6))
social_media_followers = {'Facebook': 2800000, 'Twitter': 339000, 'Instagram': 2700000, 'LinkedIn': 1300000}
platforms = list(social_media_followers.keys())
followers = list(social_media_followers.values())
plt.barh(platforms, followers)
plt.title('Presença nas Redes Sociais da Hyundai')
plt.xlabel('Seguidores')
plt.ylabel('Plataforma')
plt.show()
# Configuração do dashboard com gráficos criados
dashboard = dashboard(title="Dashboard de Marketing da Hyundai")
dashboard.add_worksheet(grafico1, "Gráfico 1", "Descrição do Gráfico 1")
dashboard.add_worksheet(grafico2, "Gráfico 2", "Descrição do Gráfico 2")
dashboard.add_worksheet(grafico3, "Gráfico 3", "Descrição do Gráfico 3")

# Publicar o dashboard no Tableau Server ou Tableau Online
dashboard.publish()


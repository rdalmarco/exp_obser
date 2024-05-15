import matplotlib.pyplot as plt
from analise.convertingDF import users_df

users_df.columns = ['ID', 'Reputação', 'Data de Criação', 'Nome de Exibição', 'Último Acesso', 'Localização', 'Sobre Mim', 'Visualizações', 'Votos Positivos', 'Votos Negativos', 'ID da Conta', 'UserDisplayName']

print(users_df.head())

location_counts = users_df['Localização'].value_counts().head(10)
location_counts.plot(kind='bar', figsize=(10, 6), color='skyblue')
plt.title('Top 10 Localizações dos Usuários')
plt.xlabel('Localização')
plt.ylabel('Número de Usuários')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
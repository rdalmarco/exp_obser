import matplotlib.pyplot as plt
from analise.convertingDF import votes_df

votes_df.columns = ['ID', 'PostId', 'Tipo de Voto', 'Data de Criação']

vote_counts = votes_df['Tipo de Voto'].value_counts()

vote_counts.plot(kind='bar', figsize=(10, 6), color='skyblue')
plt.title('Contagem de Votos por Tipo de Voto')
plt.xlabel('Tipo de Voto')
plt.ylabel('Número de Votos')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

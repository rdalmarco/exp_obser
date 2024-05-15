import matplotlib.pyplot as plt
from analise.convertingDF import badges_df

badges_df.columns = ['ID', 'UserId', 'Nome', 'Data', 'Class', 'TagBased']

user_badges_counts = badges_df['UserId'].value_counts().head(10)

user_badges_counts.plot(kind='bar', figsize=(10, 6), color='skyblue')
plt.title('Top 10 Usuários com Mais Tags')
plt.xlabel('ID do Usuário')
plt.ylabel('Número de Tags')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

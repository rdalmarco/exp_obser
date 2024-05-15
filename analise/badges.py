import matplotlib.pyplot as plt
from analise.convertingDF import badges_df

badges_df.columns = ['ID', 'UserId', 'Nome', 'Data', 'Class', 'TagBased']

print(badges_df.head())

user_counts = badges_df['UserId'].value_counts().head(10)
user_counts.plot(kind='bar', figsize=(10, 6), color='skyblue')
plt.title('Top 10 Usuários com Mais Badges')
plt.xlabel('ID do Usuário')
plt.ylabel('Número de Badges')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

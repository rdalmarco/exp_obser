import matplotlib.pyplot as plt
from analise.convertingDF import comments_df

comments_df.columns = ['ID', 'PostId', 'Score', 'Texto', 'Data de Criação', 'UserId', 'UserDisplayName']

print(comments_df.head())

user_counts = comments_df['UserId'].value_counts().head(10)
user_counts.plot(kind='bar', figsize=(10, 6), color='skyblue')
plt.title('Top 10 Usuários com Mais Comentários')
plt.xlabel('ID do Usuário')
plt.ylabel('Número de Comentários')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

software_comments = comments_df[comments_df['Texto'].str.contains('Software')]
print(software_comments)
num_software_comments = len(software_comments)
print(f"Total de comentários com a palavra 'Software': {num_software_comments}")

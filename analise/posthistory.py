import matplotlib.pyplot as plt
from analise.convertingDF import posthistory_df, users_df

# Traduzindo os nomes das colunas, se necessário
posthistory_df.columns = ['ID', 'PostHistoryTypeId', 'PostId', 'RevisionGUID', 'Data de Criação', 'UserId', 'Texto', 'ContentLicense']

# Exibindo as primeiras linhas do DataFrame após a tradução
print(posthistory_df.head())

# Mapeando os IDs de usuário para os nomes correspondentes
posthistory_df['UserName'] = posthistory_df['UserId'].map(users_df.set_index('ID')['Nome de Exibição'])

# Gerando um gráfico de barras para a contagem de revisões por usuário
user_counts = posthistory_df['UserName'].value_counts().head(10)
user_counts.plot(kind='bar', figsize=(10, 6), color='skyblue')
plt.title('Top 10 Usuários com Mais Revisões de Postagens')
plt.xlabel('Nome do Usuário')
plt.ylabel('Número de Revisões')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Encontrando o usuário que mais fez revisões
most_revisions_user_name = user_counts.idxmax()  # Obtém o nome do usuário com mais revisões

print(f"O usuário que mais fez revisões é: {most_revisions_user_name}")

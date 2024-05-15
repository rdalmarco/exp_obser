import matplotlib.pyplot as plt
from analise.convertingDF import postlinks_df

postlinks_df.columns = ['ID', 'Data de Criação', 'PostId', 'RelatedPostId', 'LinkTypeId']

print(postlinks_df.head())

related_post_counts = postlinks_df['PostId'].value_counts().head(10)
related_post_counts.plot(kind='bar', figsize=(10, 6), color='skyblue')
plt.title('Top 10 Postagens com Mais Links Relacionados')
plt.xlabel('ID da Postagem')
plt.ylabel('Número de Links Relacionados')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

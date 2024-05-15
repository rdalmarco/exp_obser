import matplotlib.pyplot as plt
from analise.convertingDF import posts_df

posts_df.columns = ['ID', 'Tipo de Postagem', 'Data de Criação', 'Pontuação', 'Número de Visualizações', 'Corpo', 'ID do Proprietário', 'ID do Último Editor', 'Data da Última Edição', 'Data da Última Atividade', 'Título', 'Tags', 'Número de Respostas', 'Número de Comentários', 'Licença de Conteúdo', 'ID da Resposta Aceita', 'Nome de Exibição do Proprietário', 'Data de Comunidade Proprietária', 'ID do Postagem Pai', 'Data de Fechamento', 'Contagem de Favoritos']

print(posts_df.head())

view_counts = posts_df['ID'].value_counts().head(10)
view_counts.plot(kind='bar', figsize=(10, 6), color='skyblue')
plt.title('Top 10 Postagens com Mais Visualizações')
plt.xlabel('ID da Postagem')
plt.ylabel('Número de Visualizações')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

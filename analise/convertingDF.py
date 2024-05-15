import xml.etree.ElementTree as ET
import pandas as pd
import os

# Função para ler e extrair dados de um arquivo XML
def extract_data_from_xml(file_path, element_name):
    data = []
    tree = ET.parse(file_path)
    root = tree.getroot()
    for row in root.findall(element_name):
        data.append(row.attrib)
    return data

files_and_elements = {
    "Badges": "row",
    "Comments": "row",
    "PostHistory": "row",
    "PostLinks": "row",
    "Posts": "row",
    "Tags": "row",
    "Users": "row",
    "Votes": "row"
}

directory = "xmlsSoftwareEngineering/"

dataframes = {}

users_df = None
badges_df = None
comments_df = None
posts_df = None
posthistory_df = None
postlinks_df = None
tags_df = None
votes_df = None

for file, element in files_and_elements.items():
    file_path = os.path.join(directory, f"{file}.xml")
    print("Verificando existência de:", file_path)
    if os.path.exists(file_path):
        print("Arquivo encontrado:", file_path)
        data = extract_data_from_xml(file_path, element)
        if file == "Users":
            users_df = pd.DataFrame(data)
        if file == "Badges":
            badges_df = pd.DataFrame(data)
        if file == "Comments":
            comments_df = pd.DataFrame(data)
        if file == "Posts":
            posts_df = pd.DataFrame(data)
        if file == "PostHistory":
            posthistory_df = pd.DataFrame(data)
        if file == "PostLinks":
            postlinks_df = pd.DataFrame(data)
        if file == "Tags":
            tags_df = pd.DataFrame(data)
        if file == "Votes":
            votes_df = pd.DataFrame(data)
    else:
        print("Arquivo não encontrado:", file_path)

# Exibir as primeiras linhas de cada DataFrame
# for file, df in dataframes.items():
#     print(f"\nPrimeiras linhas de {file}:")
#     print(df.head())

# Realizar análise estatística descritiva dos DataFrames
# for file, df in dataframes.items():
#     print(f"\nEstatísticas descritivas de {file}:")
#    print(df.describe())

# URL da API com todos os personagen

import requests


url = 'https://hp-api.onrender.com/api/characters'

#faz a requesiçao para pegar os dados

resposta = requests.get(url)
dados = resposta.json()


nomes = []

for personagem in dados:
    nomes.append(personagem['name'])

#ordena os nomes em ordem alfabética
nomes.sort()

#titulo do app
st.title('busca bruxo - o lugar onde encontrará todas as informações dos bruxos')


#sidebar com a listas de nomes

nome_escolhido = st.selectbox('escolha um bruxo',nomes)



















import streamlit as st
import requests

# URL da API com todos os personagens
url = "https://hp-api.onrender.com/api/characters"
st.set_page_config(layout='wide')
# Faz a requisição para pegar os dados
resposta = requests.get(url)
dados = resposta.json()

# Pega apenas os nomes dos personagens , a partir de uma lista vazia

nomes = []
for personagem in dados:
    nomes.append(personagem['name'])


# Ordena os nomes em ordem alfabética
nomes.sort()

# Título do app
st.title('Busca Bruxo - O Lugar onde encontrará todas as informações dos Bruxos')

# Sidebar com a lista de nomes
nome_escolhido = st.selectbox('Escolha um Bruxo',nomes)

# Procura o personagem escolhido na lista de dados
personagem  = nomes
for p in dados:
    if p['name'] == nome_escolhido:
         personagem = p
         break


# Mostra o nome do personagem
st.header(f'nome do personagem{personagem['name']}')

# ===== IMAGEM EM DESTAQUE =====
# Verifica se o personagem tem imagem
if personagem['image'] and personagem['image'] !='':
  st.image(personagem['image'],width=300)
else:
    st.write('ESTE PERSONAGEM NAO POSSUI IMAGEM')




# Linha divisória
st.divider()







# Informações principais
st.write(f'**casa:** {personagem['house']}')
st.write(f'**especie:** {personagem['species']}')
st.write(f'**genero:** {personagem['gender']}')
st.write(f'**data de nascimento:** {personagem['dateOfBirth']}')
st.write(f'**ano de nascimento:** {personagem['yearOfBirth']}')


# Informações da varinha
st.write("**Varinha:**")
st.write(f"- Madeira: {personagem['wand']['wood']}")
st.write(f"- Núcleo: {personagem['wand']['core']}")
st.write(f"- Tamanho: {personagem['wand']['length']} polegadas")


st.write(f"**Patrono:** {personagem['patronus']}")
st.write(f"**Ator/Atriz:** {personagem['actor']}")

# Mostra se está vivo
if personagem['alive']:
  st.write(f'**esta vivo?** sim')
else:
  st.write(f'**esta vivo?** não')





















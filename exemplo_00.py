import requests

#comandos de CRUDS é sempre parecido com banco de dados
    #requests.get # é como o select
    #requests.post # é como o create
    #requests.put # é como o update
    #requests.delete # é como o delete

response = requests.get(f"https://pokeapi.co/api/v2/pokemon/25")
data = response.json()
data_types = data['types']  # Supondo que 'data' é o dicionário com os dados do Pokémon
types_list = [] # Crio uma lista vazia para colocar todos tipos nessa lista
for type_info in data_types:
    types_list.append(type_info['type']['name'])
types = ', '.join(types_list) # Transforma uma lista em uma string com virgula
print(data['name'], types)

# Exemplos transformando uma lista em uma string com virgula
    #lista_exemplo = ["luciano", "fabio", "bruno"]
    #lista_unica = ', '.join(lista_exemplo)
    #print(lista_unica)
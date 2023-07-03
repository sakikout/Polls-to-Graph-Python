import requests
import json
from votacoes_obj import polls_decoder
from lexicon import FileDictionary
from lexicon import deputy_decoder_API

## inicialmente pegando as votações disponiveis na API e o id delas para tratar individualmente com cada uma
response = requests.get(
  "https://dadosabertos.camara.leg.br/api/v2/votacoes?id=&ordem=DESC&ordenarPor=dataHoraRegistro"
)
print(f"Status da requisção: {response.status_code}")

try:
  req_dict = json.loads(response.content)
  polls = []

  i = 0
  while (i < len(req_dict['dados'])):
    aux = polls_decoder(req_dict['dados'][i])
    polls.append(aux.id)
    i += 1
  print(f"Votacoes adicionadas: {len(polls)}")

except Exception as e:
  print(
    f"Ocorreu um erro no processo de criação e manipulação do dicionário/API: {e}"
  )
## pela API, o numero de deputados diminui drasticamente (porque ela não oferece informações de cada votação)
try:
  votacoes_data = FileDictionary()
  votacoes_dict = {}
  print("Aguarde enquanto está sendo computado as votações...")
  for id in polls:
    url = "https://dadosabertos.camara.leg.br/api/v2/votacoes/" + str(
      id) + "/votos"
    response = requests.get(url)
    ## print(f"Status da requisção: {response.status_code}")
    votacoes_dict[id] = json.loads(response.content)
    ## print(votacoes_dict[id])

  print("Aguarde enquanto está sendo computado os votos...")
  i = 0
  for n in votacoes_dict:
    while (i < len(votacoes_dict[n]['dados'])):
      if (votacoes_dict[n]['dados'] != ''):
        aux = deputy_decoder_API(votacoes_dict[n]['dados'][i], n)
        votacoes_data.add_deputy(aux)
        i += 1

  print(f"Deputados adicionados: {len(votacoes_data.deputados)}")

except Exception as e:
  print(
    f"Ocorreu um erro no processo de criação e manipulação do dicionário/API: {e}"
  )

## criando uma lista na classe com os ids das votações para criação do grafo
votacoes_data.set_polls()

## adicionando o grafo principal
print("Aguarde enquanto está sendo montado o grafo...")
votacoes_data.add_main_graph()
votacoes_data.write_main_graph()
votacoes_data.write_deputies_polls()

## TRABALHO AEDS II (CSI 105) - Universidade Federal de Ouro Preto
## Dupla: Amanda Jacomette e Beatriz Dalfior

import json
from lexicon import FileDictionary
from lexicon import deputy_decoder

## classe para armazenar os Deputados e Grafos das votações
votacoes_data = FileDictionary()

## tentativa para leitura do arquivo JSON

print("------------ LEITURA DE VOTACOES EM JSON ------------------")
nomeArquivo = input("Informe o arquivo de votacoes JSON: ")

if ( ".json" not in nomeArquivo):
    nomeArquivo += ".json"
print("Processando...")

try:
    with open(nomeArquivo, encoding="utf8") as file:
        content = file.read()
        dataDict = json.loads(content)

    i = 0

    print("Aguarde enquanto está sendo checado os deputados existentes no arquivo...")
    ## tentativa para leitura dos deputados dentro da biblioteca gerada pelo arquivo JSON
    while( i < len(dataDict['dados'])):
        aux = deputy_decoder(dataDict['dados'][i])
        votacoes_data.add_deputy(aux) ## adicionando os deputados na classe de armazenamento
        i+= 1
    
    print(f"Deputados adicionados: {len(votacoes_data.deputados)}")

except Exception as e: ## identificando alguma exceção no processo
    print(f"Ocorreu um erro no processo de criação e manipulação do dicionário/arquivo: {e}")  
    
## criando uma lista na classe com os ids das votações para criação do grafo
votacoes_data.set_polls()

## adicionando o grafo principal
print("Aguarde enquanto está sendo montado o grafo...")
votacoes_data.add_main_graph()
votacoes_data.write_main_graph()
votacoes_data.write_deputies_polls()


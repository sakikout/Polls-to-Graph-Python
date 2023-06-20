from deputado import Deputado
from votacoes import Graph

class FileDictionary:
    def __init__(self):
        self.deputados = [] ## list of deputies
        self.votacoes = [] ## the polls' id
        self.total_polls = 0 ## total number of polls
        self.graphs = [] ## list of graphs for each poll


    def add_deputy(self, deputado):
        for deputy in self.deputados: ## checking if deputy already in list by their name
            if deputy.nome == deputado.nome: 
                deputy.add_polls(deputado.get_polls_list())
                return
            
        self.deputados.append(deputado) ## appending deputy to list

    def set_polls(self):
        for deputado in self.deputados:
            aux = deputado.get_polls_list()
            for x,y in aux:
                if x in self.votacoes:
                    continue
               
                self.votacoes.append(x)

    def get_poll(self, indice):
        try:
            index = int(indice)
            ## print(self.votacoes[index])
            return self.votacoes[index]

        except IndexError:
            for item in self.votacoes:
                if item == indice:
                    return item

    def add_main_graph(self):
        self.main_graph = Graph('null')
        self._set_graph(self.main_graph)
        print("Grafo principal adicionado.")

        return 0
    
    def add_graphs(self):
        for p in self.votacoes:
            graph = Graph(p)
            ## print(p)
            self._set_graph(graph)
            self.graphs.append(graph)

        print(f"Operação de adicionar grafos finalizada. Adicionados {len(self.graphs)} grafos.")


    def _set_graph(self, graph: Graph):
        graph.add_nodes(self.deputados)
        graph.add_edge()

        
    def show_main_graph(self):
        print(self.main_graph.__str__())

    def write_main_graph(self):
        f = open("graph.txt", "w", encoding="utf-8")
        f.write(self.main_graph.toFile())
        f.close()
        print("- Grafo escrito no arquivo graph.txt")

    def write_deputies_polls(self):
        f = open("deputies.txt", "w", encoding="utf-8")
        for d in self.deputados:
            d.diff_polls()
            f.write(d.polls_attended())
        f.close()
        print("- Deputados escritos no arquivo deputies.txt")

    def show_graphs(self):
        for graph in self.graphs:
            print(graph.__str__())

    def show_graph(self, id_given):
        for graph in self.graphs:
            if graph.id == id_given:
                print(graph.__str__())
    
## identificando um Deputado no dicionário do arquivo JSON de votações
def deputy_decoder(dict):
    return Deputado(dict['deputado_']['id'], dict['deputado_']['nome'], dict['deputado_']['siglaPartido'], dict['idVotacao'], dict['voto'])
        
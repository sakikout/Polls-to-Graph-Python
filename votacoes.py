from deputado import Deputado

class Graph:
    def __init__(self, idVotacao):
        self.id = idVotacao
        self.adj_list = {}
        self.node_count = 0
        self.edge_count = 0

    def __str__(self):
        res = "Nos: " + str(self.node_count) + "\nArestas: " + str(self.edge_count) + "\n\n" + "Grafo: " + "\n"

        for key in self.adj_list:
            res += str(key) + ": " + str(self.adj_list[key]) + "\n"

        return res
    
    def toFile(self):
        res = "Nos: " + str(self.node_count) + "\nArestas: " + str(self.edge_count) + "\n\n" + "Grafo: " + "\n"

        for deputy in self.adj_list:
            for node in self.adj_list[deputy]:
                res+= deputy.print_connection(node[0], node[1]) + "\n"

        return res

    def add_node(self, deputado: Deputado):
        if deputado in self.adj_list:
            print(f"WARN: Node {deputado} já existe.")
            return

        if (self.id == 'null'): 
            self.adj_list[deputado] = []
            self.node_count += 1
            return
        
        for x, y in deputado.get_polls_list():
            if x == self.id:
                self.adj_list[deputado] = []
                self.node_count += 1
        ## else:
            ## print(f"Deputado {deputado.nome} não adicionado.")

    def add_nodes(self, nodes: Deputado):
        for item in nodes:
            ## aux = item
            self.add_node(item)

        ## print(f"Operação de adicionar nós finalizada. Nós adicionados: {self.node_count}")
    
    def _add_two_way_edge(self, node1 : Deputado, node2 : Deputado, peso, tipo):
        self.adj_list[node1].append((node2, peso, tipo))
        self.adj_list[node2].append((node1, peso, tipo))
        self.edge_count += 2

    def add_edge(self):
        try:
            ## print("Operação de adicionar arestas inicializada.")
           if (self.id == 'null'): 
                for deputado in self.adj_list:
                    p1 = deputado.get_votes_yes()
                    pNo1 = deputado.get_votes_no()
                    pAbs1 = deputado.get_votes_absent()
                    for conection in self.adj_list:
                        p2 = conection.get_votes_yes()
                        pNo2 = conection.get_votes_no()
                        pAbs2 = conection.get_votes_absent()

                        if p1 == p2 and p1 != 0 and conection.id != deputado.id:
                            peso_sim = p1
                            self._add_two_way_edge(deputado, conection, peso_sim, 'Sim')

                        if pNo1 == pNo2 and pNo1 != 0 and conection.id != deputado.id:
                            peso_nao = pNo1
                            self._add_two_way_edge(deputado, conection, peso_nao, 'Não')

                        if pAbs1 == pAbs2 and pAbs1 != 0 and conection.id != deputado.id:
                            peso_abs = pAbs1
                            self._add_two_way_edge(deputado, conection, peso_abs, 'Abstenção')
           else:
            for deputado in self.adj_list:
                    p1 = deputado.get_votes_yes_poll(self.id)
                    pNo1 = deputado.get_votes_no_poll(self.id)
                    pAbs1 = deputado.get_votes_absent_poll(self.id)
                    for conection in self.adj_list:
                        p2 = conection.get_votes_yes_poll(self.id)
                        pNo2 = conection.get_votes_no_poll(self.id)
                        pAbs2 = conection.get_votes_absent_poll(self.id)

                        if p1 == p2 and p1 != 0 and conection.id != deputado.id:
                            peso_sim = p1
                            self._add_two_way_edge(deputado, conection, peso_sim, 'Sim')

                        if pNo1 == pNo2 and pNo1 != 0 and conection.id != deputado.id:
                            peso_nao = pNo1
                            self._add_two_way_edge(deputado, conection, peso_nao, 'Não')

                        if pAbs1 == pAbs2 and pAbs1 != 0 and conection.id != deputado.id:
                            peso_abs = pAbs1
                            self._add_two_way_edge(deputado, conection, peso_abs, 'Abstenção')

          ##  print(f"Operação de adicionar arestas no grafo {self.id} finalizada. Arestas adicionadas: {self.edge_count}")

        except KeyError as e:
            print(f"ERROR: Deputado {e} não existe no gráfico")
import json
from json import JSONEncoder

class Deputado:
    def __init__(self, id, nome, partido, idVotacoes, voto):
        self.id = int(id)
        self.nome = nome
        self.siglaPartido = partido

        self.votacoes = []
        self.votacoes.append((idVotacoes, voto))
        self.totalVotacoes = 0
       

    def __repr__(self): ## função para representar o deputado em caso de print do objeto
        return '{} ({})'.format(self.nome, self.siglaPartido)
    
    def __str__(self):
        ## return '{}, do partido {} e id {}. Votacoes: {}'.format(self.nome, self.siglaPartido, self.id, self.votacoes)
        return '{} ({})'.format(self.nome, self.siglaPartido)
    
    def polls_attended(self):
        return '{}  {}\n'.format(self.nome, self.totalVotacoes)
    
    def to_string(self):
        return '{}, do partido {} e id {}. Votacoes: {}'.format(self.nome, self.siglaPartido, self.id, self.votacoes)
    
    def to_json(self): ## função para encodificar o deputado para JSON
        return json.dumps(self, indent = 4, cls= EncodeDeputado)
    
    def get_polls(self):
        votacoes = []
        
        for x,y in self.votacoes:
            votacoes.append(x)
            self.totalVotacoes += 1

        return votacoes
    
    def diff_polls(self):
        for x,y in self.votacoes:
            aux = x
            for p, v in self.votacoes:
                if aux != p:
                    self.totalVotacoes += 1
    
    def get_polls_list(self):
        return self.votacoes
    
    def add_polls(self, polls):
        for poll, votes in polls:
            if poll in self.votacoes and votes in self.votacoes:
                continue
            self.votacoes.append((poll, votes))
                
    
    def get_votes(self):
        votos = []
        for x,y in self.votacoes:
                votos.append(y)
        return votos
    
    def get_votes_poll(self, idVotacao):
        votos = []
        for x,y in self.votacoes:
             if x == idVotacao:
                votos.append(y)
        return votos
    
    def get_votes_yes(self):
        votos = self.get_votes()
        votos_sim = []

        for voto in votos:
            if voto == "Sim":
                votos_sim.append(voto)

        return len(votos_sim)


    def get_votes_no(self):
        votos = self.get_votes()
        votos_nao = []

        for voto in votos:
            if voto == "Não":
                votos_nao.append(voto)

        return len(votos_nao)
    
    def get_votes_absent(self):
        votos = self.get_votes()
        votos_abs = []

        for voto in votos:
            if voto == "Abstenção":
                votos_abs.append(voto)

        return len(votos_abs)
    
    def get_votes_yes_poll(self, idVotacao):
        votos = self.get_votes_poll(idVotacao)
        votos_sim = []

        for voto in votos:
            if voto == "Sim":
                votos_sim.append(voto)

        return len(votos_sim)


    def get_votes_no_poll(self, idVotacao):
        votos = self.get_votes_poll(idVotacao)
        votos_nao = []

        for voto in votos:
            if voto == "Não":
                votos_nao.append(voto)

        return len(votos_nao)
    
    def get_votes_absent_poll(self, idVotacao):
        votos = self.get_votes_poll(idVotacao)
        votos_abs = []

        for voto in votos:
            if voto == "Abstenção":
                votos_abs.append(voto)

        return len(votos_abs) 
    
    def print_connection(self, node, weight):
        return '{}  {}  {}'.format(self.nome, node.nome, str(weight))
    
class EncodeDeputado(JSONEncoder): ## classe para encodificar o deputado para dicionário
    def default(self, o):
            return o.__dict__
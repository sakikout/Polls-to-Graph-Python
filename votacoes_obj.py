

class Votacoes:
    def __init__(self, id, uri, data, dataHoraRegistro, siglaOrgao, uriOrgao, uriEvento, proposicaoObjeto, uriProposicaoObjeto, descricao, aprovacao):
        self.id = id
        self.uri = uri
        self.data = data
        self.dataHoraRegistro = dataHoraRegistro
        self.siglaOrgao = siglaOrgao
        self.uriOrgao = uriOrgao
        self.uriEvento = uriEvento
        self.proposicaoObjeto = proposicaoObjeto
        self.uriProposicaoObjeto = uriProposicaoObjeto
        self.descricao = descricao
        self.aprovacao = aprovacao

        
def polls_decoder(dict):
    return Votacoes(dict['id'], 
                    dict['uri'], 
                    dict['data'], 
                    dict['dataHoraRegistro'], 
                    dict['siglaOrgao'], 
                    dict['uriOrgao'], 
                    dict['uriEvento'], 
                    dict['proposicaoObjeto'],
                    dict['uriProposicaoObjeto'], 
                    dict['descricao'], 
                    dict['aprovacao'])
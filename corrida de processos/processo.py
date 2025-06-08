class Processo:
    #cosntrutor tipo no java
    def __init__(self, nome, tempo_total, prioridade=0):
        self.nome = nome
        self.tempo_total = tempo_total
        self.tempo_restante = tempo_total
        self.prioridade = prioridade
        self.tempo_execucao_real = 0
        self.executando = False

    def iniciar_execucao(self):
        self.executando = True
        self.tempo_execucao_real = 0

    def executar(self, quantum=1):
        if self.tempo_restante > 0:
            tempo_exec = min(quantum, self.tempo_restante)
            self.tempo_restante -= tempo_exec
            self.tempo_execucao_real += tempo_exec

    def finalizar_execucao(self):
        self.executando = False

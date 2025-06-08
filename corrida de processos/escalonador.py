import time

class Escalonador:
    def __init__(self, processos):
        self.processos = processos

    def fifo(self, callback=None, passo=1, delay=0.3):
        for p in self.processos:
            p.iniciar_execucao()
        for p in self.processos:
            while p.tempo_restante > 0:
                p.executar(passo)
                if callback:
                    callback()
                time.sleep(delay)
        for p in self.processos:
            p.finalizar_execucao()

    def round_robin(self, quantum=2, callback=None, delay=0.3):
        processos = self.processos[:]
        for p in processos:
            p.iniciar_execucao()
        while any(p.tempo_restante > 0 for p in processos):
            for p in processos:
                if p.tempo_restante > 0:
                    p.executar(min(quantum, p.tempo_restante))
                    if callback:
                        callback()
                    time.sleep(delay)
        for p in processos:
            p.finalizar_execucao()

    def por_prioridade(self, callback=None, passo=1, delay=0.3):
        processos = sorted(self.processos, key=lambda p: p.prioridade)
        for p in processos:
            p.iniciar_execucao()
            while p.tempo_restante > 0:
                p.executar(passo)
                if callback:
                    callback()
                time.sleep(delay)
            p.finalizar_execucao()

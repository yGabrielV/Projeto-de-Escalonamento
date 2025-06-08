import tkinter as tk
from processo import Processo
from escalonador import Escalonador
import threading
import random

class main:

    def __init__(self, root):
        self.root = root
        self.root.title("Corrida de Processos - Velozes e Furiosos 🚗💨")

        self.processos = self.criar_processos()

        self.labels = []
        for p in self.processos:
            frame = tk.Frame(root)
            frame.pack(pady=5)

            label_nome = tk.Label(frame, text=p.nome, width=20)
            label_nome.pack(side='left')

            progresso = tk.StringVar()
            label_barra = tk.Label(frame, textvariable=progresso, width=30, bg='white', relief='sunken')
            label_barra.pack(side='left', padx=5)

            self.labels.append((progresso, p))


        #Cria botão
        self.btn_fifo = tk.Button(root, text="Iniciar FIFO", command=lambda: self.iniciar_corrida('fifo'))
        self.btn_fifo.pack(pady=5)

        self.btn_rr = tk.Button(root, text="Iniciar Round Robin", command=lambda: self.iniciar_corrida('round_robin'))
        self.btn_rr.pack(pady=5)

        self.btn_prioridade = tk.Button(root, text="Iniciar Prioridade", command=lambda: self.iniciar_corrida('prioridade'))
        self.btn_prioridade.pack(pady=5)

        self.status = tk.Label(root, text="", justify='left')
        self.status.pack(pady=10)

        self.executando = False


    #cria os corredores
    def criar_processos(self): 
        return [
            Processo("Dominic Toretto", random.randint(5, 15), prioridade=2),
            Processo("Brian O'Conner", random.randint(5, 15), prioridade=1),
            Processo("Roman Pearce", random.randint(5, 15), prioridade=4),
            Processo("Han Lue", random.randint(5, 15), prioridade=3)
        ]


    #manda as variaveis de arrasta(reinicia elas)
    def resetar_processos(self):
        self.processos = self.criar_processos()
        for i, (var, _) in enumerate(self.labels):
            self.labels[i] = (var, self.processos[i])
        self.atualizar_barras()


    def atualizar_barras(self):
        for var, processo in self.labels:
            progresso = int((1 - processo.tempo_restante / processo.tempo_total) * 30)
            barra = '█' * progresso + ' ' * (30 - progresso)
            porcentagem = int((progresso / 30) * 100)
            var.set(f"[{barra}] {porcentagem}%")


    def corrida(self, politica):
        self.executando = True
        self.resetar_processos()
        escalonador = Escalonador(self.processos)

        if politica == 'fifo':
            escalonador.fifo(callback=self.atualizar_barras, passo=1, delay=0.3)
        elif politica == 'round_robin':
            escalonador.round_robin(quantum=1, callback=self.atualizar_barras, delay=0.3)
        elif politica == 'prioridade':
            escalonador.por_prioridade(callback=self.atualizar_barras, passo=1, delay=0.3)

        classificados = sorted(self.processos, key=lambda p: p.tempo_execucao_real or float('inf'))
        podio = "🏆 Podium:\n"
        for i, p in enumerate(classificados[:3], 1):
            tempo = f"{p.tempo_execucao_real:.2f}s" if p.tempo_execucao_real else "N/A"
            podio += f"{i}º - {p.nome} em {tempo}\n"
        self.status.config(text=podio)
        self.executando = False


    def iniciar_corrida(self, politica):
        if self.executando:
            return  #é oque nao deixa o codigo quebrar(nao roda duas corridas ao mesmo tempo)
        thread = threading.Thread(target=lambda: self.corrida(politica))
        thread.start()

if __name__ == "__main__":
    root = tk.Tk()
    app = main(root)
    root.mainloop()

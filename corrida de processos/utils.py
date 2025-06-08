import os

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

#ajusta a barra 
def exibir_barras(processos):
    barra_len = 30
    
    for p in processos:
        progresso_atual = int((1 - p.tempo_restante / p.tempo_total) * barra_len)
        
        barra = '=' * progresso_atual + ' ' * (barra_len - progresso_atual)
        
        porcentagem = int((progresso_atual / barra_len) * 100)
        
        print(f"{p.nome:25}: [{barra}] {porcentagem}%")

from processo import Processo
from escalonador import Escalonador

def main():
    processos = [
        Processo("Dominic Toretto", 10,prioridade=2),
        Processo("Brian O'Conner", 8,prioridade=1),
        Processo("Romam Pearce", 12,prioridade=4),
        Processo("Han Lue", 9,prioridade=3)
    ]

    print("Escolha a política de escalonamento:")
    print("1 - FIFO")
    print("2 - Round Robin")
    print("3 - Prioridade")

    escolha = input("Digite o número da política: ")

    escalonador = Escalonador(processos)

    if escolha == '1':
        escalonador.fifo()
    elif escolha == '2':
        escalonador.round_robin(quantum=2)
    elif escolha == '3':
        escalonador.prioridades()
    else:
        print("Opção não implementada ainda")

if __name__ == "__main__":
    main()

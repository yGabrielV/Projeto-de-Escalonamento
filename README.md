## 🏎️ Projeto de Escalonamento de Processos

Simulação educativa de escalonamento de processos em Python, com interface gráfica (`tkinter`) e três algoritmos diferentes: **FIFO**, **Round Robin** e **Prioridade**.

---

## 🎯 Objetivos

- Visualizar como cada algoritmo escalona processos.
- Tornar o aprendizado de Sistemas Operacionais mais intuitivo e interativo.
- Exibir os resultados em tempo real com uma “corrida” divertida inspirada em Velozes e Furiosos.

---

## 🚀 Como executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/yGabrielV/Projeto-de-Escalonamento.git
   cd Projeto-de-Escalonamento

2. Execute o Script do Projeto
   ```bash
   python gui.py
   
3. Escolha um algoritmo de escalonamento clicando em:

Iniciar FIFO

Iniciar Round Robin

Iniciar Prioridade

---

## 🧠 Algoritmos Implementados
FIFO (First-In, First-Out)
Processos são executados na ordem de chegada, um de cada vez.

Round Robin
Cada processo recebe um quantum fixo de tempo; a execução alterna entre eles até que todos terminem.

Por Prioridade
Processos são ordenados por nível de prioridade (menor número = maior prioridade) e executados em sequência.

## ℹ️ Como o sistema funciona
São criados 4 processos com:

Nome (ex: Dominic Toretto, Brian O'Conner…)

Tempo de execução aleatório

Prioridade aleatória

A barra de progresso (label) mostra o avanço de cada processo em tempo real.

A corrida é executada em thread separada para não travar a interface.

Ao final, é exibido um “pódio” com os 3 processos mais rápidos (menor tempo real de execução).

---

## 📚 Bibliografia / Referências
1. TANENBAUM, Andrew S.; BOS, Herbert. Modern Operating Systems. 4ª edição. Pearson, 2015.
(Referência principal para conceitos de escalonamento, processos, prioridades e algoritmos.)

2. STALLINGS, William. Operating Systems: Internals and Design Principles. 9ª edição. Pearson, 2018.
(Utilizado para estudo dos algoritmos FIFO, Round Robin e Prioridade.)

3. Matérias da disciplina de Sistemas Operacionais — Prof.Fabio Rocha de Araujo — CESUPA, 2025.
 https://github.com/fabioraraujo/escalonamento/?authuser=1

4. Python Software Foundation. Python 3 Documentation
(Referência para uso de bibliotecas padrão como threading, random e tkinter.)

5. GeeksforGeeks. Process Scheduling Algorithms
(Consultado para revisão dos conceitos práticos de escalonamento de processos.)

6. YouTube – Ttinker - Curso completo para iniciantes(Python)
   (Referencia visual para a criaçao da interface grafica./Canal - Rafael Serafim)

7. Documentação oficial do Tkinter
 https://docs.python.org/3/library/tkinter.html

8. ChaGpt
   (Foi utilizado com o intuito de esclarecer, ensinar e me auxiliar na criação do projeto. Como o entendimento mais profundo da linguagem(Phython), a construção da Interface grafica, ideias de quais bibliotecas utilizar, um esclarecimento maior das politicas de escalonamento e correção de erros)



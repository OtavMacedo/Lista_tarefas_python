import json
import os

def verifica_lista(lista,mensagem):
    if not lista:
        print(mensagem)
        return False
    return True

def listar(tarefas):
    print()
    if not verifica_lista(tarefas, "Lista de tarefas vazia"):
        return
    
    print("Tarefas:")
    for tarefa in tarefas:
        print(f'\t{tarefa}')
    print()

def mover_tarefa(lista_1, lista_2, mensagem):
    if not verifica_lista(lista_1,mensagem):
        return
    lista_2.append(lista_1.pop())

def desfazer(tarefas, lixeira):
    mover_tarefa(tarefas,lixeira, "Não há nada para desfazer")

def refazer(lixeira,tarefas):
    mover_tarefa(lixeira,tarefas, "Não há nada para refazer")

def salvar(dados, tarefas, lixeira):
    dados['lista_tarefas'] = tarefas
    dados['lixeira'] = lixeira
    with open('dados\\data_base.json', 'w', encoding='utf8') as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False)

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

with open('dados\\data_base.json', 'r', encoding='utf8') as arquivo:
    dados = json.load(arquivo)

tarefas = dados['lista_tarefas']
lixeira = dados['lixeira']

comandos = {
    'listar': lambda: listar(tarefas),
    'desfazer': lambda: desfazer(tarefas, lixeira),
    'refazer': lambda: refazer(lixeira, tarefas),
    'salvar': lambda: salvar(dados, tarefas, lixeira),
    'clear': limpar_tela
}

while True:
    print('Comandos: listar, desfazer, refazer, salvar')
    entrada = input('Digite uma tarefa ou comando: ')

    comando = comandos.get(entrada)

    if comando:
        comando()
    else:
        tarefas.append(entrada)

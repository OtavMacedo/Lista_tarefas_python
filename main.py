import json
import os


def verifica_tarefa(tarefa, tarefas):
    tarefa = tarefa.strip()
    if not tarefa:
        print("Campo vazio")
        return False
    if tarefa in tarefas:
        print("Esta tarefa já existe")
        return False
    return tarefa

def adicionar(tarefa,tarefas):
    print()
    tarefa_verificada = verifica_tarefa(tarefa,tarefas)
    if tarefa_verificada:
        tarefas.append(tarefa_verificada)

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
    tarefa = lista_1.pop()
    lista_2.append(tarefa)

def desfazer(tarefas, lixeira):
    mover_tarefa(tarefas,lixeira, "Não há nada para desfazer")

def refazer(lixeira,tarefas):
    mover_tarefa(lixeira,tarefas, "Não há nada para refazer")

def limpar_lixeira(lixeira):
    lixeira.clear()

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
    'limpar':lambda: limpar_lixeira(lixeira),
    'salvar': lambda: salvar(dados, tarefas, lixeira),
    'clear': limpar_tela
}

while True:
    print('Comandos: listar, desfazer, refazer, limpar,salvar')
    entrada = input('Digite uma tarefa ou comando: ')

    comando = comandos.get(entrada)

    if comando:
        comando()
    else:
        adicionar(entrada, tarefas)

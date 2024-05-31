from lista_tarefas_functions import *

def main():

    dados = carregar_dados()

    tarefas = dados['lista_tarefas']
    lixeira = dados['lixeira']

    comandos = {
        'listar': lambda: listar(tarefas),
        'desfazer': lambda: desfazer(tarefas, lixeira),
        'refazer': lambda: refazer(lixeira, tarefas),
        'limpar': lambda: limpar_lixeira(lixeira),
        'salvar': lambda: salvar(dados, tarefas, lixeira),
        'clear': limpar_tela
    }

    while True:
        print('Comandos: listar, desfazer, refazer, limpar, salvar')
        entrada = input('Digite uma tarefa ou comando: ')

        comando = comandos.get(entrada)

        if comando:
            comando()
        else:
            adicionar(entrada, tarefas)

if __name__ == "__main__":
    main()
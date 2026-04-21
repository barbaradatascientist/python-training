'''
EXERCÍCIO 2---
Desenvolva um programa em Python para gerenciar uma lista de tarefas no terminal.
O sistema deve permitir:

Criar uma lista de tarefas (finalizando com "OK")
Adicionar novas tarefas
Exibir as tarefas numeradas
Remover uma tarefa pelo número
Encerrar o programa quando o usuário escolher sair

O menu deve ser exibido continuamente até que o usuário opte por sair.
'''

import os

lista_de_tarefas = []

#Função para exibir as opções que podem ser escolhidas e retornará a opção desejada
def tela_inicial():
    os.system('cls')
    print('''
        
    █░░ █ █▀ ▀█▀ ▄▀█   █▀▄ █▀▀   ▀█▀ ▄▀█ █▀█ █▀▀ █▀▀ ▄▀█ █▀
    █▄▄ █ ▄█ ░█░ █▀█   █▄▀ ██▄   ░█░ █▀█ █▀▄ ██▄ █▀░ █▀█ ▄█
        
        ''')
    
    print('''
        1 - Criar lista
        2 - Adicionar na lista
        3 - Ver lista
        4 - Remover na lista
        0 - Sair
    ''')
    return input('= ')
    
    
#Função de criar lista, inserindo quantas tarefas o usuario quiser e quebrando o loop com a palavra 'ok'
def criar_lista():
    os.system('cls')
    print('Digite "OK" quando acabar de fazer a lista...')
    
    j = 1
    while True:
        elemento = input(f'{j}:  ').strip()
        
        if elemento.upper() == 'OK':
            break
        
        lista_de_tarefas.append(elemento)
        j = j + 1
    
        

#Função de adicionar na lista
def adicionar_na_lista():
    os.system('cls')
    tarefa = input('Inserir tarefa: ')
    lista_de_tarefas.append(tarefa)
    
    print('Tarefa adicionada!\n')
    
    '''
    Input sempre tem que esperar o usuario apertar Enter para continuar o programa, 
    e como após cada função, o programa retorna ao loop da main, o Enter satisfaz nossa necessidade.
    '''
    input('Pressione Enter para voltar...')

    

#Função de remover da lista
#Adicionei um try-except para que o código não quebre
def remover_da_lista():
    os.system('cls')
    indice = input('Numero da tarefa a ser removida: ')
    try:
        indice = int(indice)
    except ValueError:
        print('Tarefa inválida!')
              
    lista_de_tarefas.pop(indice - 1)
    
    print('Tarefa removida!\n')
    
    input('Pressione Enter para voltar...')
    



#Ver a lista completa
def ver_lista():
    os.system('cls')
    print('''
          == 𝑳𝒊𝒔𝒕𝒂 𝒅𝒆 𝑻𝒂𝒓𝒆𝒇𝒂𝒔 ==
          ''')
    i = 1
    for tarefa in lista_de_tarefas:
        print(f'{i}- {tarefa}')
        i = i+1
        
    input('Pressione Enter para voltar...')
    
  
#Condição para determinar se é um script ou importação = "if __name__ == '__main__':"
if __name__ == '__main__':
    
    '''
    Condição While que permite que o codigo entre em um loop e o programa só fechará se a opção 0 ser escolhida,
    senão, a condição continua sendo satisfeita. 
    '''
    while True:
        opcao = int(tela_inicial())
        
        if opcao == 1:
            criar_lista()
        elif opcao == 2:
            adicionar_na_lista()
        elif opcao == 3:
            ver_lista()
        elif opcao == 4:
            remover_da_lista()
        elif opcao == 0:
            print('Saindo...')
            break
        else:
            print('Opção inválida! Tente novamente.')
            input('Pressione espaço...')   
    
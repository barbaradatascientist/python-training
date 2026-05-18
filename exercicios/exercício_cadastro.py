'''
EXERCÍCIO 1--
Cadastro de integrantes, idades e indices de temas disponiveis. Deve conter:
-Lista de números de 1 a 10;
-Lista com quatro nomes;
-Lista com idades.
'''
import os

lista_de_numeros = []
lista_de_nomes = []
lista_de_idade = {}

def subtitulo():
    os.system('cls')
    print('''
    
    ▀█▀ █▀█ ▄▀█ █▄▄ ▄▀█ █░░ █░█ █▀█   █▀▀ █▀▄▀█   █▀▀ █▀█ █░█ █▀█ █▀█
    ░█░ █▀▄ █▀█ █▄█ █▀█ █▄▄ █▀█ █▄█   ██▄ █░▀░█   █▄█ █▀▄ █▄█ █▀▀ █▄█
    
    ''')


def mostrar_lista(lista):
    for elemento in lista:
        print(f'.{elemento}')

    print('')

def mostrar_dicionario(dicionario):
    for chave, valor in dicionario.items():
        print(f'{chave}: {valor}')
    
    print('')

if __name__ == '__main__':
    
    #Lista de números de 1 a 10

    for i in range(1,11):
        lista_de_numeros.append(i)

    #Lista com quatro nomes, com input

    subtitulo()
    print('Insira os integrantes do seu grupo: ')
    for j in range(4):
        lista_de_nomes.append(input(f'{j+1}° integrante: '))

    #Lista com a idade

    subtitulo()
    print('Insira a idade dos integrantes em ordem-- ')
    for k in range(4):
        lista_de_idade[f'Idade do {k+1}° integrante '] = int(input('='))

    subtitulo()
    print('Integrantes----')
    mostrar_lista(lista_de_nomes)
    print('Idade dos integrantes----')
    mostrar_dicionario(lista_de_idade)
    print('Temas disponiveis para o trabalho----')
    mostrar_lista(lista_de_numeros)


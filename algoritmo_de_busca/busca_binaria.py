'''
PSEUDOCODIGO
A busca binária consiste em dividir um vetor previamente ordenado ao meio e verificar 
se o valor procurado está na parte esquerda ou direita. De acordo com o resultado da 
comparação, o algoritmo divide novamente a metade correspondente do vetor até encontrar 
o valor desejado ou concluir que ele não existe no vetor.

função busca_binária(vetor_ordenado, valor, incio_vetor, fim_vetor){
    
    Caso Base: Caso base: quando o número procurado não existe no vetor. Nesse caso, 
    o valor do início do vetor será maior que o valor do fim do vetor, indicando que 
    não há mais posições válidas para realizar a busca.
    if inicio_vetor > fim_vetor:
        return -1
        
    indice = (inicio + fim) /2
    
    Caso 1: Quando o indice é igual ao valor buscado
    if vetor_ordenado[indice] = valor:
        return indice;
        
    Caso 2: Quando o indice é maior que o valor procurado
    elif vetor_ordenado[indice] > valor:
        busca_binaria(vetor_ordenado, valor, incio_vetor, indice - 1);
    
    Caso 3: Quando o indice é menor que o valor procurado
    else:
        busca_binaria(vetor_ordenado, valor, indice + 1, fim_vetor);
    
}
'''

def BUSCA_BINARIA(vetor_ordenado, valor, inicio_vetor, fim_vetor):
    
    if inicio_vetor > fim_vetor:
        return - 1;
        
    indice = (inicio_vetor + fim_vetor) // 2
    
    if vetor_ordenado[indice] == valor:
        return indice
    
    elif vetor_ordenado[indice] > valor:
        return BUSCA_BINARIA(vetor_ordenado, valor, inicio_vetor, indice - 1)
        
    else:
        return BUSCA_BINARIA(vetor_ordenado, valor, indice + 1, fim_vetor)


if __name__ == '__main__':
    vetor = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    
    print(BUSCA_BINARIA(vetor, 'C', 0, 6))
'''
PSEUDOCODIGO
O Insertion Sort consiste em organizar os elementos de um vetor de forma semelhante à maneira 
como organizamos cartas de baralho em mãos. O algoritmo percorre o vetor comparando cada elemento 
com os anteriores e o insere na posição correta. Inicialmente, compara o primeiro elemento com o 
segundo e realiza a troca caso o segundo seja menor. Em seguida, continua avançando pelo vetor, 
movendo os elementos maiores para a direita até encontrar a posição adequada para inserir o elemento atual. 
Esse processo se repete até que todo o vetor esteja ordenado.

função insertion_sort(vetor):
    for i até comprimento(vetor) - 1, faça:
        aux = vetor[i]
        j = i - 1
        
        while((j >= 0) and (aux < vetor[j])):
            vetor[j + 1] = vetor[j]
            j = j - 1
        
        vetor[j + 1] = aux
        
'''

def insertion_sort(vetor):
    
    for i in range(1, len(vetor)):
        aux = vetor[i]
        j = i - 1
        
        while((j >= 0) and (aux < vetor[j])):
            vetor[j+1] = vetor[j]
            j = j - 1
            
        vetor[j+1] = aux
        
    return vetor
    
if __name__ == '__main__':
    
    vet = [7, 3, 1, 8, 10, 0]
    
    print(insertion_sort(vet))
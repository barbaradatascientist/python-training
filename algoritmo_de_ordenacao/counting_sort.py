'''
PSEUDOCODIGO

função COUNTING_SORT(array):

    verificar se o array contém 1 ou nenhum elemento
    
    percorrer o array e achar o valor máximo do vetor (valor_maximo = max(array))
    
    criar uma lista com a quantidade de indices do valor máximo
    
    contar quantas vezes cada indice aparece (for num in array: count[num] += 1)
    
    EM OUTROS CÓDIGOS:
    "contar as ococrrencias somando o atual ao anterior começando do segundo elemento
    exemplo: 
    Vetor =               [2, 2, 0, 3, 1, 1, 2, 2]
    indice:               | 0 | 1 | 2 | 3 |
    qunt_valor:           | 1 | 2 | 4 | 1 |   
    soma das ocorrencias: | 1 | 3 | 6 | 7 |
    
    apos somar as ocorrencias, realoque o vetor no vetor de saida, sendo um ponteiro contando de tras pra frente, e depois indo subtraindo as ocorrencias.
    "
    
    EM PYTHON: 
    usar o método enumerate() que retorna o indice e o valor alocado no indidce como um contador e depois juntar tudo em um vetor só com o método extend
'''
def COUNTING_SORT(vetor):
    se_vazio = len(vetor)
    if se_vazio == 0:
        return vetor
    
    valor_maximo = max(vetor)
    
    count = [0 for _ in range(valor_maximo + 1)]
    
    #contando a quantidade de vezes que cada número aparece
    for num in vetor: 
        count[num] += 1
    
    saida_count = []
    for i, valor in enumerate(count):
        saida_count.extend([i] * valor)
        
    return saida_count

if __name__ == '__main__':
    
    vetor = [3, 4, 2, 3, 4, 1, 4]  
    
    print(COUNTING_SORT(vetor))
    
           
    
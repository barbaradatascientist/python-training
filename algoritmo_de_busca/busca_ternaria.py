'''
PSEDOCODIGO
A busca ternária é um algoritmo de busca parecido com a busca binária; porém, ela se caracteriza pela divisão do vetor em três partes 
para seguir a lógica de "dividir e conquistar". O algoritmo divide o vetor em três partições definindo dois pontos médios ($m1$ e $m2$). 
Logo em seguida, ocorre a verificação para identificar em qual dessas partições encontra-se o valor desejado.

função busca_ternaria(vetor_ordenado, valor, inicio_vetor, fim_vetor){
    
    Caso Base: Quando ao tentar passar o valor do tamanho do vetor entrar na condição de que o inicio é maior que o final do vetor, signifuca que o valor nao esta no vetor
    if inicio_vetor > fim_vetor:
        return -1
    
    m1 = inicio_vetor + ((fim_vetor - inicio_vetor) // 3)
    m2 = fim_vetor - ((fim_vetor - inicio_vetor) // 3)
    
    Caso 1: Quando o valor de m1 é igual ao valor procurado
    if vetor_ordenado[m1] == valor:
        return m1
        
    Caso 2: Quando o valor de m2 é igual ao valor procurado
    elif vetor_ordenado[m2] == valor:
        return m2
        
    Caso 3: Se m1 for maior queo valor, significa que o valor que procuramos esta no primeiro terço do vetor
    elif vetor_ordenado[m1] > valor:
        return busca_ternaria(vetor_ordenado, valor, inicio_vetor, m1 - 1)
        
    Caso 4: Se m2 for menor que o valor procurado, signifuca qie o valor que estamos procurando está na terceira parte do vetor
    elif vetor_ordenado[m2] < valor:
        return busca_ternaria(vetor_ordenado, valor, m2 + 1, fim_vetor)
    
    Caso 5: Se não tender nenhuma das condiçoes, signifuca wue o valor esta na parte do meio
    else:
        return busca_ternaria(vetor_ordenado, valor, m1 + 1, m2 - 1)
       
'''

def BUSCA_TERNARIA(vetor_ordenado, valor, inicio_vetor, fim_vetor):
    
    if inicio_vetor > fim_vetor:
        return -1
        
    m1 = inicio_vetor + ((fim_vetor - inicio_vetor) // 3)
    m2 = fim_vetor - ((fim_vetor - inicio_vetor) // 3)
     
    if vetor_ordenado[m1] == valor:
        return m1
     
    elif vetor_ordenado[m2] == valor:
        return m2
       
    elif vetor_ordenado[m1] > valor:
        return BUSCA_TERNARIA(vetor_ordenado, valor, inicio_vetor, m1 - 1)
        
    elif vetor_ordenado[m2] < valor:
        return BUSCA_TERNARIA(vetor_ordenado, valor, m2 + 1, fim_vetor)
        
    else:
        return BUSCA_TERNARIA(vetor_ordenado, valor, m1 + 1, m2 - 1)   
        
if __name__ == '__main__':
    
    vetor = [0, 1, 2, 3, 5, 7, 11, 13, 17]     
    
    print(BUSCA_TERNARIA(vetor, 17, 0, 8))
'''
PSEUDOCÓDIGO

função QUICKSORT(pivô, início_vetor, fim_vetor):
    definir pivô como o primeiro elemento (neste caso);
    definir ponteiro esquerdo = inicio vetor;
    definir ponteiro direito = fim do vetor;

    VERIFICAÇÃO:
    enquanto(ponteiro direito for maior ou igual ao ponteiro esquerdo):

        enquanto ponteiro esquerdo for < pivô: 
            ponteiro esquerdo + 1;
        
        enquanto ponteiro direito for > pivô:
            ponteiro dirieto - 1;

        se ponteiro direito for menor que ponteiro esquerdo:
            aux = valor ponteiro esquerdo
            valor do ponteiro esquerdo = valor do ponteiro direito;
            valor do ponteiro direito = valor aux;
            ponteiro direito --;
            ponteiro esquerdo ++;

    *chamada recursiva da função para "dividir" o vetor em dois, utilizando o principio que o vetor como um todo
    so terá acabado de se organizar quando o ponteiro da direita chegar no incio do vetor e quando o ponteiro da 
    esquerda chegar no fim do vetor "original"
    /subvetores/
    se incio vetor < ponteiro direita:
        QUICKSORT(pivô, inicio_vetor, ponteiro direita);
    se ponteiro esqurda < fim vetor:
        QUICKSORT(pivô, ponteiro esquerda, fim_vetor);
'''

def QUICKSORT(vetor, inicio_vetor, fim_vetor):

    pivo = vetor[inicio_vetor]
    p_esquerdo = inicio_vetor
    p_direito = fim_vetor

    while p_esquerdo <= p_direito:

        while vetor[p_esquerdo] < pivo:
            p_esquerdo += 1
        
        while vetor[p_direito] > pivo:
            p_direito -= 1

        if p_esquerdo <= p_direito:

            aux = vetor[p_esquerdo]
            vetor[p_esquerdo] = vetor[p_direito]
            vetor[p_direito] = aux

            p_esquerdo += 1
            p_direito -= 1

    if inicio_vetor < p_direito:
        QUICKSORT(vetor, inicio_vetor, p_direito)

    
    if p_esquerdo < fim_vetor:
        QUICKSORT(vetor, p_esquerdo, fim_vetor)

    

if __name__ == '__main__':

    vetor = [4, 1, 3, 8, 5, 4, 0]

    QUICKSORT(vetor, 0, len(vetor) - 1)

    print(vetor)

    
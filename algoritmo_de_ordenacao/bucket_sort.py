from insertion_sort import INSERTION_SORT

'''
PSEUDOCÓDIGO

função BUCKET_SORT(vetor):

    verificar se o vetor não está vazio
    retorne nada se estiver vazia
    
    difinir a quantidade de baldes a serem criados (num_buckets = len(vetor))
    criar uma lista com os baldes de acordo com a conta acima (buckets = [ [] for _ in range(num_buckets)])
    
    valor_maximo = max(vetor) // ve qual é o maior numero do vetor
    para cada valor no vetor, faça:
        normalizacao = valor / max + 1 // calcula o valor nominal
        indice_bucket = int(valor * normalizacao) // calcula o índice inteiro para saber em qual balde colocar
        bucket[indice_bucket].append(valor)
    
    depois de separar os valores e alocar nos devidos indices dos baldes, ordenar cada balde separadamente por insertion_sort
    
    para cada bucket em buckets, faça: 
        INSERTION_SORT(bucket)
    
    junte os baldes que estavam separados
        
    para cada bucket em buckets, faça:
        juntar todos os bucketes em uma lista só
        
    return output
    
'''

def BUCKET_SORT(vetor):
    #verificar se a entrada não está vazia ou se tem apenas 1 elemento
    se_vazio = len(vetor)
    if se_vazio == 0:
        return vetor
    
    quantidade_buckets = len(vetor)
    buckets = [[] for _ in range(quantidade_buckets)]
    
    valor_maximo = max(vetor)
    for num in vetor: 
        indice_bucket = int((num / valor_maximo) * (quantidade_buckets - 1))
        buckets[indice_bucket].append(num)
    
    #chama o insertion sort para cada subvetor(bucket) 
    for bucket in buckets:
        INSERTION_SORT(bucket)
    
    output = []
    #junta os buckets em um unico vetor
    for bucket in buckets:
        output.extend(bucket)
    return output

if __name__ == '__main__':
    
    array = [31, 2, 30.2, 1, 100.5, 0]
    print(BUCKET_SORT(array))
 
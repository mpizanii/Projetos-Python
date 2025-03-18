# Implementação sequencial

import hashlib
import itertools
import string

def hash(texto):
    return hashlib.sha256(texto.encode()).hexdigest()

def buscar_string(hash_alvo):
    caracteres = string.ascii_lowercase  
    contador = 0  

    for combinacao in itertools.product(caracteres, repeat=7):
        tentativa = ''.join(combinacao)
        hash_gerada = hash(tentativa)
        contador += 1
        if contador % 1000000== 0: 
            print(f"Tentativas: {contador} - Hash gerada: {hash_gerada}")
        
        if hash_gerada == hash_alvo:
            print(f"String encontrada: {tentativa}")
            return tentativa
    
    print("Nenhuma string encontrada que corresponda à hash alvo.")
    return None

hash_alvo = "70502ff6bb85356055ea52ff0a657afd09a52324a33734ccfb7bdedf05634925"
buscar_string(hash_alvo)

# Implementação paralela

import hashlib
import itertools
import string
import multiprocessing  

def hash(texto):
    return hashlib.sha256(texto.encode()).hexdigest()

def buscar_string_parte(hash_alvo, prefixo, caracteres, queue, processo_id):
    contador = 0
    for combinacao in itertools.product(caracteres, repeat=7-len(prefixo)):
        tentativa = prefixo + ''.join(combinacao)
        hash_gerada = hash(tentativa)
        contador += 1
        if contador % 1000000 == 0:
            print(f"Processo {processo_id} - Tentativas: {contador} - Hash gerada: {hash_gerada}")
        
        if hash_gerada == hash_alvo:
            print(f"Processo {processo_id} - String encontrada: {tentativa}")
            queue.put(tentativa)  
            return

def buscar_string(hash_alvo):
    caracteres = string.ascii_lowercase
    queue = multiprocessing.Queue()  

    processos = []
    for i, prefixo in enumerate(caracteres):
        p = multiprocessing.Process(target=buscar_string_parte, args=(hash_alvo, prefixo, caracteres, queue, i))
        processos.append(p)
        p.start()
    
    resultado = None
    while resultado is None:
        if not queue.empty():
            resultado = queue.get()  
            break

    for p in processos:
        p.terminate()

    if resultado:
        print(f"String encontrada: {resultado}")
        return resultado
    else:
        print("Nenhuma string encontrada que corresponda à hash alvo.")
        return None

if __name__ == "__main__":
    hash_alvo = "70502ff6bb85356055ea52ff0a657afd09a52324a33734ccfb7bdedf05634925"
    p = multiprocessing.Process(target=buscar_string, args=(hash_alvo,))
    p.start()
    p.join()

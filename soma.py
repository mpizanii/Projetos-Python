import multiprocessing as mp
import numpy as np

def soma_parcial(array_slice):
    return sum(array_slice)

def soma_paralela(array):
    num_cores = mp.cpu_count()
    tamanho_parte = len(array) // num_cores
    partes = [array[i * tamanho_parte:(i + 1) * tamanho_parte] for i in range(num_cores)]
    
    with mp.Pool(processes=num_cores) as pool:
        somas_parciais = pool.map(soma_parcial, partes)
    
    soma_total = sum(somas_parciais)
    
    return soma_total

if __name__ == "__main__":
    array = np.random.randint(1, 100, size=1_000_000)
    soma_total = soma_paralela(array)
    print(f"Soma total do array: {soma_total}")
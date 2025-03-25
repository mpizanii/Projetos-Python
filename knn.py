import numpy as np 
from collections import Counter 
from sklearn.datasets import make_classification 
from sklearn.model_selection import train_test_split 
from sklearn.metrics import accuracy_score 

def calcular_distancia(x1, x2): 
    return np.sqrt(np.sum((x1 - x2) ** 2)) 
def knn(xTrain, yTrain, xTest, k): 
    yPred = []  
    for x_test in xTest: 
    distâncias = [calcular_distancia(x_test, x_train) for x_train in xTrain] 
    kIndices = np.argsort(distâncias)[:k] 
    kVizinhos = [yTrain[i] for i in kIndices] 
    classe_predita = Counter(kVizinhos).most_common(1)[0][0] 
    yPred.append(classe_predita) 
    return np.array(yPred) 
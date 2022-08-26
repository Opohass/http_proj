import numpy as np
from threading import Thread

class KNNBrute:
    def __init__(self, k_neighbors=3):
        self.k_neighbors = k_neighbors
        self.data_x = None
        self.data_y = None
        self.distances = []
        
    def fit(self, X, y):
        self.data_x = X
        self.data_y = y
    
    def predict(self, X):
        predictions = []
        threads = []
        for i in range(len(X)):
            t = Thread(target=self.distances_thread, args=[X[i],i])
            t.start()
            threads.append(t)
        for t in threads:
            t.join()
        for i in range(len(X)):
            self.distances[i] = np.array(self.distances[i])
            self.distances[i][self.distances[i][:,0].argsort()]
            predictions.append(self.ret_amnt(self.distances[i][:self.k_neighbors, 1]))
        return predictions
            
    def distances_thread(self, x, i):
        self.distances.append([])
        for p_x in self.data_x:
            self.distances[i].append([self.euclidean_distance(x, p_x), self.data_y[i]])
        
        
    
    @staticmethod     
    def euclidean_distance(p1, p2):
        return np.sqrt(np.sum(np.square(p1 - p2)))
    
    @staticmethod
    def ret_amnt(lst):
        dict_pred = {}
        for pred in lst:
            if pred in list(dict_pred.keys()):
                dict_pred[pred] += 1
            else:
                dict_pred[pred] = 1
        keys = list(dict_pred.keys())
        values = list(dict_pred.values())
        return keys[values.index(max(values))]
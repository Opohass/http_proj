import numpy as np


class KNNBrute:
    def __init__(self, k_neighbors=3):
        self.k_neighbors = k_neighbors
        self.data_x = None
        self.data_y = None
        self.distances = None
        
    def fit(self, X, y):
        self.data_x = X
        self.data_y = y
    
    def predict(self, X):
        distances = []
        predictions = []
        for i in len(X):
            distances.append([])
            for p_x in self.x:
                distances[i].append(self.euclidean_distance(X[i], p_x))
            distances[i] = sorted(distances[i])
            predictions.append(self.ret_amnt(distances[i][:self.k_neighbors]))
        return predictions
            
       
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
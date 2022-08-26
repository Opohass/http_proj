import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
# from MinMaxScale import MinMaxScale
MAX_DEPTH = 2500

class Node():
    def __init__(self):
        self.depth = 0
        self.attr = 0
        self.data_x = None
        self.data_y = None
        self.median = 0
        self.right_child = []
        self.left_child = []
    
    
        

class Tree():
    def __init__(self, data_x, data_y, max_depth=MAX_DEPTH):
        self.data_x = data_x
        self.data_y = data_y
        self.max_depth = max_depth
        self.tree = self.build_kd_tree(self.data_x, self.data_y, Node(), 1, self.max_depth)
    
    def build_kd_tree(self, data_x, data_y, node, depth, max_depth):
        
        if depth < max_depth:
            if len(data_x) == 1:
                node.median = None
                node.left_child = None
                node.right_child = None
                node.depth = depth
                node.attr = None
                node.data_x = data_x
                node.data_y = data_y
                return node
            elif len(data_x) == 0:
                return None
        elif depth == max_depth:
            node.median = None
            node.left_child = None
            node.right_child = None
            node.depth = depth
            node.attr = None
            node.data_x = data_x
            node.data_y = data_y
            return node
        else:
            raise RecursionError(f"Python Only Allowes Recursion depth of {MAX_DEPTH}")
            
        median = np.median(data_x[:,depth % len(data_x[0,:])], axis=0)
        if median == 1.0:
            median = 0.99999
        elif median == 0.0:
            median == 0.00001
        node.attr = depth % len(data_x[0,:])
        node.median = median
        node.depth = depth
        right_data_x = data_x[data_x[:,node.attr] >= median]
        right_data_y = data_y[(data_x[:,node.attr] >= median).nonzero()]
        left_data_x = data_x[data_x[:,node.attr] < median]
        left_data_y = data_y[(data_x[:,node.attr] < median).nonzero()]
        node.right_child = self.build_kd_tree(right_data_x, right_data_y, Node(), depth+1, max_depth)
        node.left_child = self.build_kd_tree(left_data_x, left_data_y, Node(), depth+1, max_depth)
        return node

class KnnClassifier:
    def __init__(self, k_neighbors=3, depth=MAX_DEPTH):
        self.train_set = None
        self.k_neighbors = k_neighbors
        self.depth = depth
        self.tree = None
        
    def fit(self, X, y):
        self.tree = Tree(X, y, self.depth)
    
    def predict(self, X):
        prediction = []
        for i in np.arange(len(X)):
            x_pred = []
            x_pred = KnnClassifier.get_prediction(X[i], self.tree.tree, self.k_neighbors, x_pred)
            prediction.append(KnnClassifier.get_final_answer(x_pred))
        return prediction
        
    @staticmethod
    def get_prediction(X, node, k_neighbors, x_pred):
            if len(x_pred) == k_neighbors or node == None:
                return x_pred
            if type(node.data_x) == type(None):
                if X[node.attr] >= node.median:
                    single_pred = KnnClassifier.get_prediction(X, node.right_child, k_neighbors, x_pred)
                    if single_pred != None:
                        x_pred = single_pred
                    if len(x_pred) == k_neighbors:
                        return x_pred
                    else:
                        single_pred = KnnClassifier.get_prediction(X, node.left_child, k_neighbors, x_pred)
                        if single_pred != None:
                            x_pred = single_pred
                        if len(x_pred) == k_neighbors:
                            return x_pred
                else:
                    single_pred = KnnClassifier.get_prediction(X, node.right_child, k_neighbors, x_pred)
                    if single_pred != None:
                        x_pred = single_pred
                    if len(x_pred) == k_neighbors:
                        return x_pred
                    else:
                        single_pred = KnnClassifier.get_prediction(X, node.right_child, k_neighbors, x_pred)
                        if single_pred != None:
                            x_pred = single_pred
                        if len(x_pred) == k_neighbors:
                            return x_pred
            else:
                for data_p in node.data_y:
                    if len(x_pred) >= k_neighbors:
                        break
                    if data_p != None:
                        x_pred.append(data_p)
                return x_pred
                        
        
                    
    @staticmethod
    def get_final_answer(preds):
        preds_dict = {}
        for i in preds:
            if i in preds_dict.keys():
                preds_dict[i] += 1
            else:
                preds_dict[i] = 1
        return list(preds_dict.keys())[list(preds_dict.values()).index(max(preds_dict.values()))]
            
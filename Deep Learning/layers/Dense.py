import numpy as np
import sys
sys.path.append('../tools/')
import tools

class Dense():
    """
    Dense Layer used for the DNN object
    weights: numpy array() weight matrix
    output: output of the layer
    deriv: derivative of activation
    activation_name: name of activation, used to print
    activation: activation functions
    shape: output shape
    prevlayer: previous layer
    next: next layer
    """
    
    def __init__(self,prevlayer,outputdims,activation="sigmoid"):
        
        self.weights = np.random.uniform(-1,1,size=(prevlayer.shape[1],outputdims))
        self.output = 0
        self.deriv = 1
        self.activation_name = activation
        self.activation = None
        self.shape = (None,outputdims)
        self.prevlayer = prevlayer
        self.next = None
        
        if activation == "sigmoid":
            self.activation = tools.sigmoid
            
        elif activation == "linear":
            self.activation = self.linear
        
    def getWeights(self):
        
        return self.weights
    
    def setNext(self,layer):
        
        self.next = layer
        
    def getNext(self):
        
        return self.next
    
    def getPrev(self):
        
        return self.prevlayer
        
    def dot(self,X,t=False):
        
        if t == True:
            return self.output.T.dot(X)
        return self.output.dot(X)
        
    def foward(self):
        
        layer_mul = self.prevlayer.dot(self.weights)
        self.output = self.activation(layer_mul)
        self.deriv = self.activation(layer_mul,True)
    
    def predict(self,X):
        
        return self.activation(X.dot(self.weights))
        
    def update(self,X):

        self.weights = X
        
    def linear(self,X,deriv=False):
        
        if deriv == True:
            return 1
        else:
            return X
        
    def __repr__(self):
        
        string = "Dense: " + "activation: " + self.activation_name +  ", weight shape: " + str(self.weights.shape) + ", output shape: " + str(self.shape)
        string = string + ", parameters: " + str(self.weights.shape[0]*self.weights.shape[1])
        string = string + '\n' + "-----------------------------------------------------------------" + '\n'
        return string  
    
    def __str__(self):
        
        string = "Dense: " + "activation: " + self.activation_name +  ", weight shape: " + str(self.weights.shape) + ", output shape: " + str(self.shape)
        string = string + ", parameters: " + str(self.weights.shape[0]*self.weights.shape[1])
        string = string + '\n' + "-----------------------------------------------------------------" + '\n'
        return string  
         

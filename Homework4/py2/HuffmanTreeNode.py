#!/usr/bin/python

###############################################
# module: HuffmanTreeNode.py
# author: Vladimir Kulyukin
# bugs to vladimir dot kulyukin at usu dot edu
###############################################

class HuffmanTreeNode(object):
    
    def __init__(self, symbols=set(), weight=0):
        self.__symbols = set(symbols)
        self.__weight = weight
        self.__leftChild = None
        self.__rightChild = None

    def getSymbols(self):
        return self.__symbols

    def setSymbols(self, s):
        self.__symbols = s

    def getWeight(self):
        return self.__weight

    def setWeight(self, w):
        self.__weight = w

    def getLeftChild(self):
        return self.__leftChild

    def setLeftChild(self, lc):
        self.__leftChild = lc

    def getRightChild(self):
        return self.__rightChild

    def setRightChild(self, lc):
        self.__rightChild = lc
        
    def __str__(self):
        return 'HTN(' + str(self.__symbols) + ', ' + str(self.__weight) + ')'

    def __eq__(self, htn):
        return self.getWeight() == htn.getWeight() and \
                    len(self.getSymbols().difference(htn.getSymbols())) == 0

    def isLeaf(self):
        return self.__rightChild is None and self.__leftChild is None
    



    

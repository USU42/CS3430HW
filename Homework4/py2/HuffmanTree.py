#!/usr/bin/python

######################################
## module: HuffmanTreeNode.py
# Kelsye Anderson
# A02093326
######################################

from __future__ import division
import __future__
from HuffmanTreeNode import HuffmanTreeNode


class HuffmanTree(object):
    def __init__(self, root=None):
        self.__root = root

    def getRoot(self):
        return self.__root

    def encodeSymbol(self, s):
        if not s in self.__root.getSymbols():
            raise Exception('Unknown symbol')
        else:
            encode = ""
            temp = self.__root
            while not temp.isLeaf():
                if s in temp.getLeftChild().getSymbols():
                    encode += "0"
                    temp = temp.getLeftChild()
                elif s in temp.getRightChild().getSymbols():
                    encode += "1"
                    temp = temp.getRightChild()
            return encode

    def encodeText(self, txt):
        output = ""
        for x in txt:
            output += HuffmanTree.encodeSymbol(self, x)
        return output

    def decode(self, bin_string):
        txt = ""
        temp = self.__root
        for x in bin_string:
            while not temp.isLeaf():
                if x is 0:
                    temp = temp.getLeftChild()
                    del x
                elif x is 1:
                    del x
                    temp = temp.getRightChild()
            txt += temp.getSymbol()
        return txt

    @staticmethod
    def mergeTwoNodes(htn1, htn2):
        # print 'Merging', str(htn1), str(htn2)
        symbols = set(htn1.getSymbols())
        for i in htn2.getSymbols():
            symbols.add(i)
        n = HuffmanTreeNode(symbols=symbols, weight=htn1.getWeight() + htn2.getWeight())
        n.setLeftChild(htn1)
        n.setRightChild(htn2)
        return n

    @staticmethod
    def findTwoLowestWeightNodes(list_of_nodes):
        list_of_nodes.sort(key=lambda x: x.getWeight(), reverse=False)
        temp = HuffmanTree.mergeTwoNodes(list_of_nodes[0], list_of_nodes[1])
        list_of_nodes.pop(0)
        list_of_nodes.pop(0)
        return temp

    @staticmethod
    def displayListOfNodes(list_of_nodes):
        for n in list_of_nodes:
            print(str(n))

    @staticmethod
    def fromListOfHuffmanTreeNodes(list_of_nodes):
        if len(list_of_nodes) == 0:
            raise Exception('Cannot construct from empty list of nodes')
        elif len(list_of_nodes) == 1:
            return HuffmanTree(root=list_of_nodes[0])
        else:
            x = HuffmanTree.findTwoLowestWeightNodes(list_of_nodes)
            list_of_nodes.append(x)
            return HuffmanTree.fromListOfHuffmanTreeNodes(list_of_nodes)

    @staticmethod
    def freqMapToListOfHuffmanTreeNodes(freq_map):
        return [HuffmanTreeNode(symbols=set([item[0]]), weight=item[1]) for item in freq_map.items()]






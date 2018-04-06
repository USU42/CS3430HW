
#############################
# module: BSTree.py
# Kelsye Anderson
# A02093326
#############################

from BSTNode import BSTNode

class BSTree:

    def __init__(self, root=None):
        self.__root = root
        if root==None:
            self.__numNodes = 0
        else:
            self.__numNodes = 1

    def getRoot(self):
        return self.__root

    def getNumNodes(self):
        return self.__numNodes

    def isEmpty(self):
        return self.__root == None

    def hasKey(self, key):
        if self.isEmpty():
            return False
        else:
            currNode = self.__root
            while currNode != None:
                if currNode.getKey() == key:
                    return True
                elif key < currNode.getKey():
                    currNode = currNode.getLeftChild()
                elif key > currNode.getKey():
                    currNode = currNode.getRightChild()
                else:
                    raise Exception('hasKey: ' + str(key))
            return False

    def insertKey(self, key):
        if self.isEmpty():
            self.__root = BSTNode(key=key)
            self.__numNodes += 1
            return True
        elif self.hasKey(key):
            return False
        else:
            currNode = self.__root
            parNode = None
            while currNode != None:
                parNode = currNode
                if key < currNode.getKey():
                    currNode = currNode.getLeftChild()
                elif key > currNode.getKey():
                    currNode = currNode.getRightChild()
                else:
                    raise Exception('insertKey: ' + str(key))
            if parNode != None:
                if key < parNode.getKey():
                    parNode.setLeftChild(BSTNode(key=key))
                    self.__numNodes += 1
                    return True
                elif key > parNode.getKey():
                    parNode.setRightChild(BSTNode(key=key))
                    self.__numNodes += 1
                    return True
                else:
                    raise Exception('insertKey: ' + str(key))
            else:
                raise Exception('insertKey: parNode=None; key= ' + str(key))
     
    def heightOf(self, currnode):
        ## your code
        if not currnode:
            return -1
        else:
            return 1 + max(self.heightOf(currnode.getLeftChild()), self.heightOf(currnode.getRightChild()))


    def isBalanced(self, currnode):
        ## your code
        if not currnode:
            return True

        heightL = self.heightOf(currnode.getLeftChild())
        heightR = self.heightOf(currnode.getRightChild())

        if abs(heightL-heightR) > 1:
            return False

        return self.isBalanced(currnode.getLeftChild()) and self.isBalanced(currnode.getRightChild())


    def __displayInOrder(self, currnode):
        if currnode == None:
            print('NULL')
        else:
            self.__displayInOrder(currnode.getLeftChild())
            print(str(currnode))
            self.__displayInOrder(currnode.getRightChild())

    def displayInOrder(self):
        self.__displayInOrder(self.__root)

    def isList(self, currnode):
        ## your code
        if currnode == None:
            return True

        if ((currnode.getLeftChild() != None and currnode.getRightChild() != None)):
            return False

        return (self.isList(currnode.getLeftChild()) and self.isList(currnode.getRightChild()))



                


    
            

    
   

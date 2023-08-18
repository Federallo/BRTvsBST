#use random functions
import random 

#creating node class 
class Node:
    'Class for treee nodes'

    #creating Node class
    def __init__(self, key, color, nodeFather) :
        self.key = key
        #color initialisation
        self.color = color
        #children and father initialisation
        self.left = None
        self.right = None
        self.p = nodeFather  

#creating Binary Search Tree class 
class RBT:
    'Class for Red-Black Tree'

    #creating tree
    def __init__(self) :
        self.root = None   

    #creating root node
    def setRoot(self, key) :
        self.root = Node(key, "Black", None)    

    #insert method for root and nodes
    def insert(self, key) :
        if(self.root is None) :
            self.setRoot(key)
        else :
            #iterative insertion
            self.nodeInsertion(self.root, key)

    #method to rotate tree to the left 
    def leftRotate(self, x) :
        y = x.right
        x.right = y.left #connect children from one side. Moves y left children to x right children
        if(y.left != None) :
            y.left.p = x #connect children from the other side
            
        y.p = x.p    
        if(x.p == None) :
            self.root = y
        elif(x == x.p.left) :
            x.p.left = y
        else :
            x.p.right = y
        #move set x as y's left children    
        y.left = x
        x.p = y          

    #method to rotate tree to the right
    def rightRotate(self, x) :
        y = x.left
        x.left = y.right #connect children from one side. Moves y right children to x left children
        if(y.right != None) :
            y.right.p = x #connect children from the other side
            
        y.p = x.p    
        if(x.p == None) :
            self.root = y
        elif(x == x.p.right) :
            x.p.right = y
        else :
            x.p.left = y
        #move set x as y's right children    
        y.right = x
        x.p = y                

    #insert fixup for red-black trees
    def insertFixup(self, newNode) :
        while(newNode != self.root and newNode.p.color == "Red") :
            if(newNode.p == newNode.p.p.left) :
                y = newNode.p.p.right #uncle of newNode
                if(y and y.color == "Red") :#we need to check also if the left subtree exists
                    newNode.p.color = "Black"
                    y.color = "Black"
                    newNode.p.p.color = "Red"
                    newNode = newNode.p.p #after setting father and uncle black, and grandad black, we climb to grandad 
                                          #(it could be root)  
                else :
                    if(newNode == newNode.p.right) :
                        newNode = newNode.p
                        self.leftRotate(newNode) 
                    newNode.p.color = "Black"
                    newNode.p.p.color = "Red"                    
                    self.rightRotate(newNode.p.p)
            else :#same thing but with left and right swapped
                y = newNode.p.p.left
                if(y and y.color == "Red") :
                    newNode.p.color = "Black"
                    y.color = "Black"
                    newNode.p.p.color = "Red"
                    if(newNode.p.p) :
                        newNode = newNode.p.p
                else :
                    if(newNode == newNode.p.left) :
                        newNode = newNode.p
                        self.rightRotate(newNode)
                    newNode.p.color = "Black"
                    newNode.p.p.color = "Red"
                    self.leftRotate(newNode.p.p)
        self.root.color = "Black"                

    #iterative node insertion
    def nodeInsertion(self, currentNode, key) :
        while (currentNode) :

            #tracking previous node
            tracker = currentNode

            #exploring the tree
            if(key < currentNode.key) :
                currentNode = currentNode.left
            else :
                currentNode = currentNode.right

        #inserting a new node with the new key given in input         
        currentNode = tracker        
        if (key < currentNode.key) :
            currentNode.left = Node(key, "Red", currentNode)
            self.insertFixup(currentNode.left) 
        else :
            currentNode.right = Node(key, "Red", currentNode)
            self.insertFixup(currentNode.right)     

    #using searching node method to calculate the distance of this last from the root
    def searchNode(self, key, node) :
        distance = 0
        while(node) :
            if(node.key == key) :
                return distance
            elif(key < node.key) :
                node = node.left
                distance += 1
            else :
                node = node.right 
                distance += 1
                

         

#main
if __name__ == "__main__" :
    #distance between nodes and root intepreted as number o edges

    #creating a list of input arrays length
    arrayLength = [100, 250, 500, 800, 900, 1000, 1250, 1500, 1750, 2000]

    #creating BST
    tree = RBT()

    #we will do 50 tests
    for i in range(0, len(arrayLength)) :

        #average distance of 50 tries (sorted list)
        avg50DistanceSorted = 0

        #average distance of 50 tries (shuffled sorted list)
        avg50DistanceShuffled = 0

        for j in range(0, 50) :#number of tries

            #average distance of a single try (sorted list)
            avgDistanceSorted = 0

            #average distance of a single try (shuffled sorted list)
            avgDistanceShuffled = 0

            #sorted list tree creation
            for k in range(0, arrayLength[i]) :
                tree.insert(k)

            #getting distance of nodes from root
            for k in range (0, arrayLength[i]) :    
                avgDistanceSorted += tree.searchNode(k, tree.root)
            
            #getting average distance of created list    
            avgDistanceSorted = avgDistanceSorted/(arrayLength[i])#OK

            #adding tries in variable
            avg50DistanceSorted += avgDistanceSorted

            #deleting tree
            del tree
            tree = RBT()

            #shuffled list tree creation 
            l = arrayLength[i] 
            A = random.sample(range(l), l)

            #shuffled list tree creation
            for k in range(0, len(A)) :
                tree.insert(A[k])

            #getting distance of nodes from root
            for k in range (0, len(A)) :
                avgDistanceShuffled += tree.searchNode(A[k], tree.root)

            #getting average distance of created list
            avgDistanceShuffled = avgDistanceShuffled/len(A)

            #adding tries in variable    
            avg50DistanceShuffled += avgDistanceShuffled

            #deleting tree
            del tree
            tree = RBT()

        #average in 50 tries for both lists    
        avg50DistanceSorted = avg50DistanceSorted/50
        avg50DistanceShuffled = avg50DistanceShuffled/50

        #printing results for both random and sorted lists
        print("Average distance of keys from root (50 tries):")
        print("List of ", arrayLength[i], " elements")
        print("Sorted List: ", avg50DistanceSorted)
        print("Shuffled List: ", avg50DistanceShuffled)        
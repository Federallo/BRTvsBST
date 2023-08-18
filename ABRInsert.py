#use random functions
import random 

#creating node class 
class Node:
    'Class for treee nodes'

    #creating Node class
    def __init__(self, key) :
        self.key = key
        #childrens initialisation
        self.left = None
        self.right = None

#creating Binary Search Tree class 
class BST:
    'Class for Binary Search Tree'

    #creating tree
    def __init__(self) :
        self.root = None   

    #creating root node
    def setRoot(self, key) :
        self.root = Node(key)    

    #insert method for root and nodes, and distance between them
    def insert(self, key) :
        distance = 0
        if(self.root is None) :
            self.setRoot(key)
        else :
             #iterative insertion
            distance = self.nodeInsertion(self.root, key)
        return distance

    #iterative node insertion
    def nodeInsertion(self, currentNode, key) :
        #tracking distance
        distance = 0
        while (currentNode) :

            #tracking previous node
            tracker = currentNode

            #exploring the tree
            if(key < currentNode.key) :
                currentNode = currentNode.left
                distance += 1
            else :
                currentNode = currentNode.right
                distance += 1

        #inserting a new node with the new key given in input         
        currentNode = tracker        
        if (key < currentNode.key) :
            currentNode.left = Node(key)
            return distance
        else :
            currentNode.right = Node(key)   
            return distance    


         

#main
if __name__ == "__main__" :
    #distance between nodes and root intepreted as number o edges

    #creating a list of input arrays length
    arrayLength = [100, 250, 500, 800, 900, 1000, 1250, 1500, 1750, 2000]

    #creating BST
    tree = BST()

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
                avgDistanceSorted += tree.insert(k)
            
            #getting average distance of created list    
            avgDistanceSorted = avgDistanceSorted/(arrayLength[i])

            #adding tries in variable
            avg50DistanceSorted += avgDistanceSorted

            #deleting tree
            del tree
            tree = BST()

            #shuffled list tree creation 
            l = arrayLength[i] 
            A = random.sample(range(l), l)

            #shuffled list tree creation
            for k in range(0, len(A)) :
                avgDistanceShuffled += tree.insert(A[k])

            #getting average distance of created list
            avgDistanceShuffled = avgDistanceShuffled/len(A)

            #adding tries in variable    
            avg50DistanceShuffled += avgDistanceShuffled

            #deleting tree
            del tree
            tree = BST()

        #average in 50 tries for both lists    
        avg50DistanceSorted = avg50DistanceSorted/50
        avg50DistanceShuffled = avg50DistanceShuffled/50

        #printing results for both random and sorted lists
        print("Average distance of keys from root (50 tries):")
        print("List of ", arrayLength[i], " elements")
        print("Sorted List: ", avg50DistanceSorted)
        print("Shuffled List: ", avg50DistanceShuffled)
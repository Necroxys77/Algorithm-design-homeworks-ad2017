'''
Created on 29 nov 2017

@author: matteo
'''
'''
Created on 27 nov 2017

@author: matteo
'''

class Node(object):
    def __init__(self,name):
        self.value = name
        self.counter = 0 #num of nodes of the "subtree" that has as root the current Node +1
        self.neighbors = []
        self.isVisited = False

#starting from a random node, I increment the counters
def updateCounter(current_node):
    current_node.isVisited = True
    current_node.counter = 1
    for neighbor in current_node.neighbors:
        if neighbor.isVisited:
            continue
        else:
            current_node.counter+=updateCounter(neighbor)
    return current_node.counter

#return the hub conductor
def findHub(node,v):
    hub = node
    #instead of making a 2nd DFS to modify the isVisited values
    #the semantic is inverted: True means that the node is not visited,
    #False otherwise
    node.isVisited = False
    for neighbor in node.neighbors:
        if not neighbor.isVisited:
            continue
        if neighbor.counter > v//2:
            hub = findHub(neighbor, v)
    return hub

#node of the graph
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
#cardinality graph
cardin = 5
#build edges
a.neighbors = [b,c]
b.neighbors = [a]
c.neighbors = [d,a,e]
d.neighbors = [c]
e.neighbors = [c]
#random node
start_node = a
#update counters
updateCounter(start_node)
#find hub conductor
hub = findHub(start_node, cardin)
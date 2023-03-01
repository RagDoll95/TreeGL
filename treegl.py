from ete3 import Tree
from sympy.utilities.iterables import multiset_permutations
import random
import math

#hardcoding these values for now
TREE_FILE = 'test.nh'
GAINS = 1
LOSSES = 1
SAMPLE_SIZE = 10
t = Tree(TREE_FILE)

# produce a multiset from a set a and its multiplicities
def multi(a, ms) :

    s = []
    for x,y in zip(a, ms) :
        s += [x] * y

    return s

def getTotalPermutations(g,l,n):
    s = {"G","L","N"}
    multiSet = multi(s,[GAINS,LOSSES,n-(GAINS+LOSSES)])
    return list(multiset_permutations(multiSet))

def generateRandomTree(t:Tree, permutations:list):
    permutation = random.choice(permutations)
    for index, node in enumerate(t.traverse("postorder")):
        node.add_feature("mutation",permutation[index])
    return t, permutation

def isValidTree(t:Tree):
    # Traverse from all the leaves to the root. If there are ever two gains or two losses in a row, then it is not a valid tree
    validTree = True
    for leafNode in t.get_leaves():
        l = [node.mutation for node in  leafNode.iter_ancestors() if node.mutation != "N"]
        if consecutiveDuplicates(l):
            validTree = False
            break
    return validTree

def consecutiveDuplicates(l):
    for i in range (len(l) - 1):
        if l[i] == l[i + 1]:
            return True;
    return False;


#############################################################

n = len(list(t.traverse()))
p = getTotalPermutations(GAINS,LOSSES,n)
previouslyComputed = dict()
count = 0
for i in range(SAMPLE_SIZE):
    sampleTree, samplePermutation = generateRandomTree(t, p)
    if str(samplePermutation) not in previouslyComputed:
        previouslyComputed[str(samplePermutation)] = True
        if isValidTree(sampleTree):
            count +=1
    else:
        SAMPLE_SIZE+=1

estimated_gains_losses = math.comb(n , GAINS + LOSSES) * (count / SAMPLE_SIZE)

print(estimated_gains_losses)

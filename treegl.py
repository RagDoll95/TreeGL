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
n = len(list(t.traverse()))

# produce a multiset from a set a and its multiplicities
def multi(a, ms) :

    s = []
    for x,y in zip(a, ms) :
        s += [x] * y

    return s

def getTotalPermutations(g,l,n):
    s = {"G","L","N"}
    multiSet = multi(s,[GAINS,LOSSES,n-(GAINS+LOSSES)])
    return list(multiset_permutations(s))

def generateRandomTree(t:Tree, permutations:list):
    permutation = random.choice(permutations)
    for index, node in enumerate(t.traverse("postorder")):
        node.addfeature("mutation",permutation[index])
    return t, permutation



def isValidTree(t):
    # idea: traverse to all the leaves, if there is ever two identical features in a row (i.e, two gains or two losses)
    # then it's not a valid tree.
    return False



count = 0
for i in range(SAMPLE_SIZE):
    sampleTree, samplePermutation = generateRandomTree(t, 1, 1, n)
    if isValidTree(sampleTree):
        count +=1


estimated_gains_losses = math.comb(n , GAINS + LOSSES) * (count / SAMPLE_SIZE)

print(estimated_gains_losses)

from ete3 import Tree
from sympy.utilities.iterables import multiset_permutations
import math


def generateRandomTree(t, g, l):
    # TODO come up with a way of generating a random tree
    for node in t.traverse():
        if not node.is_root:
            node.add_feature(feature="gain")
            print("internal node " + str(edge))
            edge += 1
    return t

def isValidTree(t):
    # idea: traverse to all the leaves, if there is ever two identical features in a row (i.e, two gains or two losses)
    # then it's not a valid tree.
    return False

#hardcoding these values for now
TREE_FILE = 'test.nh'
GAINS = 1
LOSSES = 1
SAMPLE_SIZE = 10

t = Tree(TREE_FILE)


count = 0
for i in range(SAMPLE_SIZE):
    sampleTree = generateRandomTree(t, 1, 1)
    if isValidTree(sampleTree):
        count +=1


estimated_gains_losses = math.comb(len(list(t.traverse())), GAINS + LOSSES) * (count / SAMPLE_SIZE)

print(estimated_gains_losses)

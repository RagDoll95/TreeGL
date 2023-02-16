from ete3 import Tree

#hardcoding these values for now
TREE_FILE = 'test.nh'
GAINS = 1
LOSSES = 1

t = Tree(TREE_FILE)

branches = len(t.get_tree_root())

print(branches)
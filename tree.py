def makeTree(root,trl,trr):
    return ['btree', root,trl,trr]

def make_empty_tree():
    return ['btree']

def is_btree(tree):
    if tree[0] == "btree":
        return True
    else:
        return False
    
def root(tree):
    return tree[1]

def left_subtree(tree):
    return tree[2]

def right_subtree(tree):
    return tree[3]

def is_empty_tree(tree):
    if tree == ['btree']:
        return True
    return False

def is_leaf_tree(tree):
    return is_empty_tree(left_subtree(tree)) and is_empty_tree(right_subtree(tree))

def preorder(tree):
    if is_empty_tree(tree):
        return []
    else:
        return [root(tree)]+preorder(left_subtree(tree))+preorder(right_subtree(tree))

def inorder(tree):
    if is_empty_tree(tree):
        return []
    else:
        return inorder(left_subtree(tree))+[root(tree)]+inorder(right_subtree(tree))

def postorder(tree):
    if is_empty_tree(tree):
        return []
    else:
        return postorder(left_subtree(tree))+postorder(right_subtree(tree))+[root(tree)]



tree_ex = makeTree ('/' ,makeTree ('+',
         makeTree(40,make_empty_tree(), make_empty_tree()),makeTree(5,make_empty_tree(), make_empty_tree())),\
         makeTree('*', makeTree(3,make_empty_tree(),make_empty_tree()),\
         makeTree('-',makeTree(7,make_empty_tree(),make_empty_tree()),makeTree(2,make_empty_tree(),make_empty_tree()))))


use recursion
start at the root, recursively compare right and left child to parent until root null
base case: root null, return true
recursive case, compare left child and right child to root, if conditions satisfied continue calling itself on each child, if not satisfied return false
use root as upper/lower bound for right/left subtree, respectively

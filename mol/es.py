   def add_to_tree(tree, path):
       current = tree
       for node in path:
           if node not in current:
               current[node] = {}
           current = current[node]
   
   def tuples_to_tree(tuples):
       tree = {}
       for path in tuples:
           add_to_tree(tree, path)
       return tree
   
   # Example usage:
   tuples = [('A', 'B', 'C'), ('A', 'B', 'D'), ('A', 'E'), ('F', 'G')]
   tree = tuples_to_tree(tuples)
   print(tree)
   
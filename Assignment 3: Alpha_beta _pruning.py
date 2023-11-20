import random
import math
studentid=input()
min_max_range=input().split(" ")
number_of_turns=int(studentid[0])
initial_lifeline=int(studentid[-1:-3:-1])
number_of_bullets=int(studentid[2])
min_value=int(min_max_range[0])
max_value=int(min_max_range[1])
branch_and_depth=2*int(studentid[0])
leaf_node=[]
for i in range((number_of_bullets**branch_and_depth)):
    leaf_node.append(random.randint(min_value,max_value))
alpha=-math.inf
beta=math.inf
def alphabeta(depth_of_graph,child,maximiz,leaf_node,alpha,beta,indx): 
    global count_of_node
    if depth_of_graph == 0: 
        count_of_node+=1
        return leaf_node[indx] 
    if maximiz == True: 
        maxnode_value = -math.inf
        for inx in range(child): 
            maxnode_value = max(maxnode_value, alphabeta(depth_of_graph-1 , child, False, leaf_node, alpha, beta,indx * 2 + inx)) 
            alpha = max(alpha, maxnode_value) 
            if alpha >= beta : 
                break
        return maxnode_value 
    else:
        minnode_value =  math.inf
        for inx in range(child): 
            minnode_value = min(minnode_value, alphabeta(depth_of_graph-1,child, True, leaf_node, alpha, beta, indx * 2 + inx))
            beta = min(beta, minnode_value)
            if alpha >= beta:
                break
        return minnode_value
count_of_node=0
print(f'Depth and Branches ratio is {branch_and_depth}:{number_of_bullets}')
print(f'Terminal States(Leaf Nodes) are {",".join(str(i) for i in leaf_node)}.')
print('Left life(HP) of the defender after maximum damage caused by the attacker is',initial_lifeline-alphabeta(branch_and_depth,number_of_bullets,True,leaf,alpha,beta,0))
print('After Alpha-Beta Pruning Leaf Node Comparisons', count_of_node)

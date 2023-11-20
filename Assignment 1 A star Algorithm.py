import heapq
import math
f = open("Input file.txt", "r")
lst = ''
for line in f:
    lst += line
a = lst.split('\n')
new_lst = []
for j in a:
    new_lst.append(j.split(' '))
f.close()
simplified={'Arad': 'A', 'Neamt': 'F', 'Bucharest': 'Z', 'Oradea': 'B', 'Craiova': 'S', 'Pitesti': 'P', 'Eforie': 'T', 
            'RimnicuVilcea': 'R', 'Fagaras': 'O', 'Timisoara': 'C', 'Dobreta': 'V', 'Urziceni': 'D', 'Hirsova': 'N', 
            'Vaslui': 'H', 'lasi': 'Q', 'Zerind': 'E', 'Lugoj': 'G', 'Mehadia': 'L'} 
distance={}
heuristic={}
visited={}
for temp in new_lst:
    distance[temp[0]] = {}
    visited[temp[0]] = False
    heuristic[temp[0]] = int(temp[1])
    for i in range(2, len(temp), 2):
        visited[temp[i]] = False
        distance[temp[0]][temp[i]] = int(temp[i+1])

start = input("Start node: ")
goal = input("End node: ")
p_queue=[]
max_distance = math.inf
path1=[]
visited[start] = True
for node,path in distance[start].items():    
    heapq.heappush(p_queue, (path+heuristic[node],[start,node]))
    
while(len(p_queue) > 0):
    cost,paths = heapq.heappop(p_queue)
    if(visited[paths[-1]]):
        continue
    visited[paths[-1]] = True
    for node,path in distance[paths[-1]].items():
        paths_new = paths + [node]
        new_cost = cost - heuristic[paths[-1]] + heuristic[node] + distance[paths[-1]][node]
        heapq.heappush(p_queue, (new_cost,paths_new))
        if(paths_new[-1] == goal and new_cost < max_distance):
            max_distance = new_cost
            path1 = paths_new

if path1==[]:
    print("NO PATH FOUND")
else:
    print('Path:','->'.join(path1))
    print(f'Total distance: {max_distance} km')

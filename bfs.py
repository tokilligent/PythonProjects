total_nodes=9
no_of_connetion=13
matrix=[[1,2,3],[0,3,4],[0,3],[1,2,5,6],[1,7,8],[3,6],[3,5,7],[4,6,8],[4,7]]

def bfs(nodes,total_conn,matrix_conn,source,target):
    if (source==target):
        return 0
    visited=[]
    visited.append(source)
    queue=[]
    
    level=0
    for i in range(len(matrix_conn[source])):
        if(matrix_conn[source][i] not in visited):
            queue.append(matrix_conn[source][i])
    
    #print(queue)
    while(len(queue)!=0):
        level=level+1
        temp_set=set([])
        for i in range(len(queue)):
            if(queue[i] not in visited):
                visited.append(queue[i])
                for j in range(len(matrix_conn[queue[i]])):
                    if(matrix_conn[queue[i]][j] not in visited and matrix_conn[queue[i]][j] not in queue):
                        temp_set.add(matrix_conn[queue[i]][j])

            if(queue[i]==target):
                return level
            
        queue.clear()
        queue=list(temp_set)

print(bfs(total_nodes,no_of_connetion,matrix,0,6))





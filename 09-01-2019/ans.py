import collections
def bridgeUtil(u, visited, parent, low, disc, adj, Time, ans): 
    visited[u]= True
    disc[u] = Time 
    low[u] = Time 
    Time += 1
    for v in adj[u]: 
        if visited[v] == False : 
            parent[v] = u 
            bridgeUtil(v, visited, parent, low, disc, adj, Time, ans) 
            low[u] = min(low[u], low[v])   
            if low[v] > disc[u]: 
                ans.append([u,v])
        elif v != parent[u]: 
            low[u] = min(low[u], disc[v]) 

def bridge():
    V = 7
    adj = [[] for i in range(7)] 
    connections = [[0,1],[1,2],[2,0],[1,3],[1,4],[1,6],[3,5],[4,5]]
    #connections = [[1,2],[1,3],[1,4],[4,5],[3,4]]
    adj = collections.defaultdict(list)
    for u,v in connections:
        adj[u].append(v)
        adj[v].append(u)

    visited = [False] * V
    disc = [float("Inf")] * V
    low = [float("Inf")] * V
    parent = [-1] * V 
    ans = []
    for i in range(V): 
        if visited[i] == False: 
            bridgeUtil(i, visited, parent, low, disc, adj, 0,ans) 
    return ans

print(bridge())
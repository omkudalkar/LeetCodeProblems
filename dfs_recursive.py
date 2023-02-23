def main():
    graph : dict = {'a': ['b','c'], 'b':['d'], 'c':['e'], 'd':['f'], 'e':[], 'f':[]}
    dfs_recursive(graph, 'a')


def dfs_recursive(graph, source):
    print(source)
    for i in graph[source]:
        dfs_recursive(graph, i)

main()

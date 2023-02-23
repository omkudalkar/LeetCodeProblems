def main():
    graph = {'a': ['c', 'b'], 'b':['d'], 'c':['e'], 'd':['f'], 'e':[], 'f':[]}
    bfs(graph, 'a')


def bfs(graph: dict, source: str):
    queue = [source]
    while len(queue) > 0:
        curr_element = queue.pop()
        print(curr_element)
        for i in graph[curr_element]:
            queue.insert(0,i)

main()

def main():
    graph : dict = {'a': ['c', 'b'], 'b':['d'], 'c':['e'], 'd':['f'], 'e':[], 'f':[]}
    dfs_iterative(graph, 'a')


def dfs_iterative(graph, source):
    stack = [source]
    while len(stack) > 0:
        curr_ele = stack.pop()
        print(curr_ele)
        for i in graph[curr_ele]:
            stack.append(i)

main()

        
def main():
    edge_list: list = [['i','j'], ['k','i'], ['m','k'], ['k','l'], ['o','n']]    
    graph = convert_edge_list_to_adjacency_list(edge_list)
    count = connected_components_count(graph)
    print(count)

def  convert_edge_list_to_adjacency_list(edge_list:list):
    # we want to convert the edge list to a more favourable format like an adjacency list
    graph: dict = {}

    for i in edge_list:
        if i[0] not in graph:
            graph[i[0]] = []
            graph[i[0]].append(i[1])
        else:
            graph[i[0]].append(i[1])
        
        if i[1] not in graph:
            graph[i[1]] = []
            graph[i[1]].append(i[0])
        else:
            graph[i[1]].append(i[0])
    return graph


def connected_components_count(graph):
    visited: set = set()
    count = 0
    for j in graph:
        stack = [j]
        if j not in visited:
            while len(stack) > 0:
                curr_ele = stack.pop()
                visited.add(curr_ele)
                #print(f"curr_ele = {curr_ele}")
                for i in graph[curr_ele]:
                    if i not in visited:
                        stack.append(i)
            count+=1
    return count
            
   

main()



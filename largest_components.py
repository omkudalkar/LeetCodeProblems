from re import L
from tabnanny import check


def main():
    edge_list: list = [['i','j'], ['k','i'], ['m','k'], ['k','l'], ['o','n'], ['l','f'], ['f', 'g']]    
    graph = convert_edge_list_to_adjacency_list(edge_list)
    count = largest_component(graph)
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


def largest_component(graph):
    visited: set = set()
    longest: int = 0

    for i in graph:
        curr_size = check_size(graph, i, visited)
        if curr_size > longest:
            longest = curr_size
    return longest





def check_size( graph, node, visited):
    if node in visited: return 0
    visited.add(node)
    count = 1
    for i in graph[node]:
        count += check_size(graph, i, visited)
    return count



            
   

main()



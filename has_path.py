def main():
    test()

def test():
    graph : dict = {'f': ['g','i'], 'g':['h'], 'h':[], 'i':['g','k'], 'j':['i'], 'k':[]}

    assert (has_path(graph, "f", "k")) =="PATH FOUND" 
    assert (has_path(graph, "f", "g")) =="PATH FOUND" 
    assert (has_path(graph, "f", "h")) =="PATH FOUND" 
    assert (has_path(graph, "i", "k")) =="PATH FOUND" 
    assert (has_path(graph, "f", "j")) =="NO PATH FOUND" 
    assert (has_path(graph, "i", "g")) =="PATH FOUND" 




def has_path(graph, source, destination):
    stack = [source]
    while len(stack) > 0:
        curr_ele = stack.pop()
        for i in graph[curr_ele]:
            if i == destination:
                return ("PATH FOUND")
            stack.append(i)
    return("NO PATH FOUND")
 


main()



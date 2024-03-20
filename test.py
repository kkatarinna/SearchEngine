from primeri_graf import *
from dfs import *
from bfs import *
from search import brojOdlaznihLinkova

if __name__=='__main__':
    graph = figure_14_12()
    print('-------------- DFS --------------')
    forest = DFS_complete(graph)
    for vertex in forest.keys():
        print('Vertex: ' + str(vertex))
        if forest[vertex]:
            print('Edge: ' + str(forest[vertex]))
        else:
            print('Edge: None')

    print('\n\n-------------- BFS --------------')
    forest = BFS_complete(graph)
    lista = []
    for vertex in forest.keys():
        print('Vertex: ' + str(vertex))
        print('degree: ', graph.degree(vertex))
        print('get edge', graph.get_edge(vertex, True))
        if forest[vertex]:
            print('Edge: ' + str(forest[vertex]))
        else:
            print('Edge: None')

    




import queue

class GNode:
    def __init__(self, data: str):
        self.data = data
        self.children: list[GNode] = []
    
    def __hash__(self):
        return hash(self.data)

    def __str__(self):
        return self.data
    
class Graph:
    def __init__(self):
        self.nodes: list[GNode] = []
    
    def __init__(self, nodes: list[GNode]):
        self.nodes: list[GNode] = nodes
    
    def bfs(self, root: GNode):
        if not root in self.nodes:
            raise ValueError("The starting root node isn't in the graph.")

        q : queue.Queue[GNode] = queue.Queue()
        visited = {n: False for n in self.nodes}

        q.put(root)
        visited[root] = True

        while not q.empty():
            node = q.get()
            print(node)
        
            for child in node.children:
                if not visited[child]:
                    q.put(child)
                    visited[child] = True

    

if __name__ == '__main__':
    ben = GNode("Ben")
    travis = GNode("Travis")
    patrick = GNode("Patrick")
    kevin = GNode("Kevin")
    matt = GNode("Matt")
    richard = GNode("Richard")
    antonio = GNode("Antonio")
    soon = GNode("Soon")
    jon = GNode("Jon")
    yui = GNode("Yui")

    ben.children = [travis, patrick, matt, richard, antonio, soon, jon]
    travis.children = [ben, patrick, kevin]
    patrick.children = [ben, travis, kevin]
    kevin.children = [travis, patrick]
    matt.children = [ben, richard]
    richard.children = [ben, matt]
    antonio.children = [ben]
    soon.children = [ben, jon, yui]
    jon.children = [ben, soon, yui]
    yui.children = [jon, soon]

    graph = Graph([ben, travis, patrick, kevin, matt, richard, antonio, soon, jon, yui])

    graph.bfs(ben)

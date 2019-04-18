from random import choice,randrange
import Trees
class ADT(object):
    """description of class"""
    def __init__(self,file_name="edges.txt"):
        '''
        The initialiser of the graph
        parameter file_name the name of the file in which the graph is stored
        postconditions: in_edges, out_edges, cost_of_edge will be populated accordingly from the file
        '''
        self.file_name = file_name
        self.__in_edges = dict()
        self.__out_edges = dict()
        self.__cost_of_edge = dict()
        self.__r_in_edges = dict()
        self.__r_out_edges = dict()
        self.__r_cost_of_edge = dict()
        self.__number_of_vertices = int()
        self.__number_of_edges = int()
        self.processed=list()
        self.visited=list()
        self.queue=list()
        self.store_edges=list()
        self.__vertices=list()
        self.__LoadFromFile()
        #print(self.__cost_of_edge)

    def __LoadFromFile(self):
        '''
        Reads from the file the input + and initializies the graph
        parameter file_ame: the name of the file
        precondition:File has to exist
        postconditions : number_of_vertices,number_of_edges,in_edges,out_edges,cost_of_edges will be be populated with the content from the given file
        '''
        file = open(self.file_name,'r')
        line = file.readline().strip()
        string=line;
        line = file.readline().strip()
        line = line.split()
        self.__number_of_vertices = int(line[0])
        self.__number_of_edges = int(line[1])   
        for index in range(0,self.__number_of_vertices):
            self.__in_edges[index] = list()
            self.__vertices.append(index)
            self.__out_edges[index] = list()
            if string=="directed":
                self.__r_in_edges[index]=list()
                self.__r_out_edges[index]=list()
        for index in range(0,self.__number_of_edges):
            line = file.readline().strip()
            line = line.split()
            self.__in_edges[int(line[1])].append(int(line[0]))
            self.__out_edges[int(line[0])].append(int(line[1]))
            self.__cost_of_edge[(int(line[0]),int(line[1]))] = int(line[2])
            if string=="undirected":
                self.__in_edges[int(line[0])].append(int(line[1]))
                self.__out_edges[int(line[1])].append(int(line[0]))
                self.__cost_of_edge[(int(line[1]),int(line[0]))] = int(line[2])
            if string=="directed":
                self.__r_in_edges[int(line[0])].append(int(line[1]))
                self.__r_out_edges[int(line[1])].append(int(line[0]))
                self.__r_cost_of_edge[(int(line[1]),int(line[0]))] = int(line[2])
        file.close()

    def GetNumberOfVertices(self):
        """
        Returns the number of vertices
        """
        return self.__number_of_vertices

    def FindEdge(self,first_vertex,second_vertex):
        '''
        Returns true if an edge exist else it will return False
        parameter 1 first_vertex: the first given vertex
        parameter 2 second_vertex: the second given vertex
        return True if there exists an edge between first_vertex and second_vertex
                False otherwise
        '''
        if first_vertex in self.__in_edges[second_vertex]:
            return True
        else:
            return False

    def ParseGraph(self):
        '''
        Returns the vertices of the graph 
        return: Returns a list(iterator) containing the vertices  
        '''
        vertices = list()
        for key in self.__in_edges.keys():
            vertices.append(key)
        return vertices

    def VertexDegrees(self,vertex):
        '''
        Returns a pair containing the inbound degree of a vertex and the outound degree of the same vertex
        Parameter:vertex-the vertex
        Return:Returns a list containing first the inbound degree and then the outbound degree
        '''
        return [len(self.__in_edges[vertex]),len(self.__out_edges[vertex])]

    def OutboundEdges(self,vertex):
        '''
        Returns a list containing the outbound edges for a vertex
        parameter:vertex the given vertex
        return:Returns a list containing all the outbound edges from the given vertex
        '''
        return self.__out_edges[vertex]

    def InboundEdges(self,vertex):
        '''
        Returns a list containing the inbound edges for a vertex
        parameter:vertex the given vertex
        return:Returns a list containing all the inbound edges from the given vertex
        '''
        return self.__in_edges[vertex]

    def RetrieveEdge(self,second_vertex,first_vertex):
        '''
        Returns the cost of the edge if it exist else it returns None
        parameter 2 first_vertex: the first given vertex
        parameter 1 second_vertex: the second given vertex
        Return:Return None-if edge doesn't exist else 
        Return the cost of the edge -int type

        '''
        if (first_vertex,second_vertex) in self.__cost_of_edge.keys():
            return self.__cost_of_edge[(first_vertex,second_vertex)]
        return None

    def ModifyEdge(self,second_vertex,first_vertex,new_cost):
        """
        Change the edge cost if it is possible
        parameter 2 first_vertex: the first given vertex
        parameter 1 second_vertex: the second given vertex
        parameter 3 new_cost the new cost of the edge
        except Throw an error if the edge doesn't exist
                else modify the cost of the edge
        return nothing
        postconditions cost_of_edge[(first_vertex, second_vertex)] will be updated with new_cost
        """
        if (first_vertex,second_vertex) in self.__cost_of_edge.keys():
            self.__cost_of_edge[(first_vertex,second_vertex)] = new_cost
        else:
            raise ValueError("The edge doesn't exist")

    def AddEdge(self,second_vertex,first_vertex,cost):
        """
        Add an edge cost if it is possible
        parameter 2 first_vertex: the first given vertex
        parameter 1 second_vertex: the second given vertex
        parameter 3 cost the new cost of the edge
        except Throw an error if the edge exist or the vertices doesn't exist
        Precondition: there must be no edge from first_vertex to second_vertex.
        postconditions out_edges[first_vertex]' = out_edges[first_vertex] + second_vertex
                       in_edges[second_vertex]' = in_edges[second_vertex] + first_vertex
                       cost_of_edge' = cost_of_edge + cost_of_edge[(first_vertex, second_vertex)]    
        """
        if (first_vertex,second_vertex) in self.__cost_of_edge.keys():
            raise ValueError("The edge already exists try to modify the cost")
        else:
            if second_vertex in self.__in_edges.keys():
                if first_vertex in self.__out_edges.keys():
                    self.__cost_of_edge[(first_vertex,second_vertex)] = cost
                    self.__in_edges[second_vertex].append(first_vertex)
                    self.__out_edges[first_vertex].append(second_vertex)
                    self.__number_of_edges+=1
                else:
                    raise ValueError("Out vertex doesn't exist")
            else:
                raise ValueError("In vertex doesn't exist")

    def RemoveEdgeFromTheInandOutEdges(self,first_vertex,second_vertex):
        '''
        Removes an edge from the in_edges and out_edges dict
        parameter 2 first_vertex: the first given vertex
        parameter 1 second_vertex: the second given vertex
        return nothing
        postconditions out_edges[first_vertex]' = out_edges[first_vertex] - second_vertex
                        in_edges[second_vertex]' = in_edges[second_vertex] - first_vertex
        '''
        for index in range(0,len(self.__in_edges[second_vertex])):
            if self.__in_edges[second_vertex][index] == first_vertex:
                self.__in_edges[second_vertex].pop(index)
                break
        for index in range(0,len(self.__out_edges[first_vertex])):
            if self.__out_edges[first_vertex][index] == second_vertex:
                self.__out_edges[first_vertex].pop(index)
    def RemoveEdge(self,second_vertex,first_vertex):
        '''
        Removes an edge from the in_edges,cost_of_edges and out_edges dict
        parameter 2 first_vertex: the first given vertex
        parameter 1 second_vertex: the second given vertex
        return nothing
        postconditions out_edges[first_vertex]' = out_edges[first_vertex] - second_vertex
                       in_edges[second_vertex]' = in_edges[second_vertex] - first_vertex
                       cost_of_edge' = cost_of_edge - cost_of_edge[(first_vertex, second_vertex)]      
        except:if it doesn't exist throw an ValueError
        '''
        if (first_vertex,second_vertex) in self.__cost_of_edge.keys():
            self.__cost_of_edge.pop((first_vertex,second_vertex))
            self.RemoveEdgeFromTheInandOutEdges(first_vertex,second_vertex)
            self.__number_of_edges-=1
        else:
            raise ValueError("Edge doesn't exist")

    def AddVertex(self,vertex):
        """
        Adds an vertex to the in_edges and out_edges dictionaries
        parameter 1:vertex the given vertex
        return nothing
        except:Throw an error if Vertex already exists
        postconditions:adds it in the in_edges,out_edges
        """
        if vertex in self.__in_edges.keys():
            raise ValueError("Vertex already exists")
        else:
            self.__in_edges[vertex] = list()
            self.__out_edges[vertex] = list()
            self.__number_of_vertices+=1

    def RemoveVertex(self,vertex):
        '''
        Removes every edge that includes vertex from the in_edges,cost_of_edges and out_edges dict
        parameter 1 vertex the given vertex
        return nothing
        postconditions The vertex and the edges containing vertex are removed from the dictionaries
        except if it doesn't exist throw an ValueError
        '''
        if vertex in self.__in_edges.keys():
            for key in self.__in_edges.keys():
                if (vertex,key) in self.__cost_of_edge.keys():
                    self.RemoveEdge(key,vertex)
                if (key,vertex) in self.__cost_of_edge.keys():
                    self.RemoveEdge(vertex,key)
            self.__in_edges.pop(vertex)
            self.__out_edges.pop(vertex)
            self.__number_of_vertices-=1
        else:
            raise ValueError("Vertex doesn't exist")

    def RandomGraph(self,number_of_vertices,number_of_edges):
        '''
        This function generates a random directed graph based on a number of vertices and number of edges
        parameter 1 number_of_vertices: int - the number of vertices of the graph
        parameter 2 number_of_edges: int - number of edges of the graph
        preconditions numberOfVertices > 0
                      0 <= numberOfEdges <= numberOfVertices^2
        return nothing
        postconditions the file 'random_graph.out' will be populated with the newly generated digraph
        '''
        file = open("random_graph.out","w+")
        file.write(str(number_of_vertices) + " " + str(number_of_edges) + "\n")
        edge_list = []
        for index in range(0,number_of_vertices):
            for index_2 in range(0,number_of_vertices):
                edge_list.append((index,index_2))
        for index in range(0,number_of_edges):
            pair = choice(edge_list)
            edge_list.remove(pair)
            cost = randrange(-1000,1000)
            file.write(str(pair[0]) + " " + str(pair[1]) + " " + str(cost) + "\n")

    def DFS(self,tree,vertex):
        '''
        This function creates the DFS tree starting in the given vertex
        Pre:vertex doesn't appear in the tree
        '''
        print("["+str(vertex),end="")
        stack=list()
        self.store_edges.clear()
        for key in self.__in_edges.keys():
            if (key,vertex) in self.__cost_of_edge.keys():
                self.store_edges.append([vertex,key])
        stack.append(vertex)
        while(stack):
            value=stack.pop()
            for y in self.OutboundEdges(value):
                if not tree.isVertex(y):
                    tree.addChild(value,y)
                    for key in self.__in_edges.keys():
                       if (key,y) in self.__cost_of_edge.keys():
                           self.store_edges.append([y,key])
                    print(","+str(y),end="")
                    stack.append(y)
        print("]")
    def ConexComponentsDFS(self):
        '''
        Creates all the conex components using a dfs algorithm
        '''
        tree=Trees.Trees()
        for vertex in self.__vertices:
            if not tree.isVertex(vertex):
                tree.newRoot(vertex)
                self.DFS(tree,vertex)
                #print(tree.ThisRoot(vertex))
                print(self.store_edges)

    def DFSKosaraju(self,vertex):
        for out in self.__out_edges[vertex]:
            if out not in self.visited:
                self.visited.append(out)
                self.DFSKosaraju(out)
        self.processed.append(vertex)

    def Kosaraju(self):
        self.processed.clear()
        self.visited.clear()

        for vertex in self.__vertices:
            if vertex not in self.visited:
                self.visited.append(vertex)
                self.DFSKosaraju(vertex)

        self.visited.clear()
        self.queue.clear()
        component={}
        c=0
        while len(self.processed)!=0:
            vertex=self.processed.pop()
            if vertex not in self.visited:
                c=c+1
                component[c]=list()
                component[c].append(vertex)
                self.queue.append(vertex)
                self.visited.append(vertex)
                while len(self.queue)!=0:
                    new_vertex=self.queue.pop(0)
                    for vertex_in in self.InboundEdges(new_vertex):
                        if vertex_in not in self.visited:
                            self.visited.append(vertex_in)
                            self.queue.append(vertex_in)
                            component[c].append(vertex_in);

        for index in range(1,c+1):
            print(component[index])
    def CabbageLettuceWolf(self):
        pass
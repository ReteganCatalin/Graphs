from copy import deepcopy
class UI(object):
    def __init__(self,directed_graph):
        self.__directed_graph=directed_graph

    def StartMenu(self):
        while True:
            print("1-Get the number of vertices")
            print("2-Parse the graph(TBD)")
            print("3-Find edge")
            print("4-In degree and out degreee of a vertex")
            print("5-Outbound degree of a vertex")
            print("6-Inbound degree of a vertex")
            print("7-Retrieve the cost of the edge")
            print("8-Modify the cost of the edge")
            print("9-Add an edge")
            print("10-Remove an edge")
            print("11-Add an vertex")
            print("12-Remove an vertex")
            print("13-Copy the graph")
            print("15-Print out all isolated vertices")
            print("14-Exit")
            print("16-Create random vector")
            print("17-Depth first search on the graph")
            choice=input()
            if(choice=='1'):
                self.NumberOfVertices()
            elif(choice=='2'):
                self.ParseGraph()
            elif(choice=='3'):
                self.FindEdge()
            elif(choice=='4'):
                self.InDegreeOutDegree()
            elif(choice=='5'):
                self.OutboundEdges()
            elif(choice=='6'):
                self.InboundEdges()
            elif(choice=='7'):
                self.Retrieve()
            elif(choice=='8'):
                self.Modify()
            elif(choice=='9'):
                self.AddEdge()
            elif(choice=="10"):
                self.RemoveEdge()
            elif(choice=="11"):
                self.AddVertex()
            elif(choice=="12"):
                self.RemoveVertex()
            elif(choice=="13"):
                self.CopyGraph()
            elif(choice=='14'):
                return 
            elif(choice=='15'):
                self.IsolatedVertices()
            elif(choice=='16'):
                self.RandomGraph()
            elif(choice=='17'):
                self.__directed_graph.ConexComponentsDFS()
            elif(choice=='18'):
                self.__directed_graph.Kosaraju()
    def RandomGraph(self):
        number_of_vertices=int(input("Give number of vertices:"))
        number_of_edges=int(input("Give number of edges:"))
        if number_of_vertices<0:
            print("The number of vertices is not a natural number")
        if number_of_vertices*number_of_vertices < number_of_edges:
            print("The number of edges is too big")
        else:
            self.__directed_graph.RandomGraph(number_of_vertices,number_of_edges)
    def IsolatedVertices(self):
        new_list=self.__directed_graph.ParseGraph()
        number_of_isolated=0
        for index in new_list:
            pair_degrees=self.__directed_graph.VertexDegrees(index)
            if pair_degrees[0]==0 and pair_degrees[1]==0:
                number_of_isolated+=1
                print(str(index),end=" ")
        print("Number of isolated vertices:",str(number_of_isolated))
    def NumberOfVertices(self):
        print(str(self.__directed_graph.GetNumberOfVertices()))
    def ParseGraph(self):
        list_with_vertices=self.__directed_graph.ParseGraph()
        for index in list_with_vertices:
            print(index,end=" ")
        print()
    def FindEdge(self):
        first_vertex=input("Give first vertex:")
        second_vertex=input("Give second vertex:")
        if self.__directed_graph.FindEdge(int(first_vertex),int(second_vertex))==True:
            print("There exist an edge from",str(first_vertex),"to ",str(second_vertex))
        else:
            print("That edge doesn't exists")
    def InDegreeOutDegree(self):
        vertex=input("Give vertex:")
        pair_of_degrees=self.__directed_graph.VertexDegrees(int(vertex))
        print("In degree is",pair_of_degrees[0])
        print("Out degree is",pair_of_degrees[1])
    def OutboundEdges(self):
        vertex=input("Give vertex:")
        outbound_edges=self.__directed_graph.OutboundEdges(int(vertex))
        print("For the outbound edge:",vertex)
        print("All edges are:")
        for index in range(0,len(outbound_edges)):
            print(outbound_edges[index],end=" ")
        print()
    def InboundEdges(self):
        vertex=input("Give vertex:")
        inbound_edges=self.__directed_graph.InboundEdges(int(vertex))
        print("For the onbound edge:",vertex)
        print("All edges are:")
        for index in range(0,len(inbound_edges)):
            print(inbound_edges[index],end=" ")
        print()
    def Retrieve(self):
        first_vertex=input("Give first vertex:")
        second_vertex=input("Give second vertex:")
        print(self.__directed_graph.RetrieveEdge(int(second_vertex),int(first_vertex)))
    def Modify(self):
        first_vertex=input("Give first vertex:")
        second_vertex=input("Give second vertex:")
        new_cost=input("Give new cost:")
        try:
            self.__directed_graph.ModifyEdge(int(second_vertex),int(first_vertex),int(new_cost))
            print("Success")
        except ValueError as Value:
            print(Value)
    def AddEdge(self):
        second_vertex=input("Give in vertex:")
        first_vertex=input("Give out vertex:")
        cost=input("Give cost:")
        try:
            self.__directed_graph.AddEdge(int(second_vertex),int(first_vertex),int(cost))
            print("Success")
        except ValueError as Value:
            print(Value)
    def RemoveEdge(self):
        second_vertex=input("Give in vertex:")
        first_vertex=input("Give out vertex:")
        try:
            self.__directed_graph.RemoveEdge(int(second_vertex),int(first_vertex))
            print("Success")
        except ValueError as Value:
            print(Value)
    def AddVertex(self):
        vertex=input("Give vertex to be added:")
        try:
            self.__directed_graph.AddVertex(int(vertex))
            print("Success")
        except ValueError as Value:
            print(Value)
    def RemoveVertex(self):
        vertex=input("Give vertex to be removed:")
        try:
            self.__directed_graph.RemoveVertex(int(vertex))
            print("Success")
        except ValueError as Value:
            print(Value)
    def CopyGraph(self):
        '''
        Creates a copy of the directed graph
        '''
        self.__copy_graph=deepcopy(self.__directed_graph())
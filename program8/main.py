make a stack then make a list of visited for all the verices then for given start point then push that onto stack then go to while loop for while stack is not empty keep digging through graph for the to if stack is empty that means there is no to as such it failed if the while loop found the to index then use the stack to build the path

#check forward
        #if cant go forward pop back and try a different path
        #check if done
        # if done return list of path on stack in correct order 

#After loading the graph information, use a depth first search to find a path (or 'None') for all of the test cases.
#Repeat using a breadth first search.https://www.khanacademy.org/computing/computer-science/algorithms/graph-representation/a/representing-graphs
from collections import defaultdict
class CoreStack:

  def __init__(self):
    self.items = []

  def Size(self):
    return len(self.items)

  def push(self, item):
    self.items.append(item)

  def pop(self):
    if self.Size() <= 0:
	    print("she is giving all that she got captain")
	    return
    return self.items.pop()
  
  def Seek(self, warrent):
    if warrent in self.items:
      return True
    return False

  def TopLook(self):
    return self.items[-1]
  def isempty(self):
    if self.Size() == 0:
      return True
    else:
      return False

class Graph: 
  
    # Constructor 
  def __init__(self): 
  
        # default dictionary to store graph 
      self.graph = defaultdict(list)
  
    # function to add an edge to graph 
  def addEdge(self,u,v): 
      self.graph[u].append(v) 

  def isedge(self,start,finish):
    for i in self.graph[start]:
      if i == finish:
        return True
    return False
  def findneighbors(self,v):
    return self.graph[v]
  
  def size(self):
    return len(self.graph)

#https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/
        # A function used by DFS 
  def DFSUtil(self,start,finish,visited): 
  
        # Mark the current node as visited and print it 
      visited[int(start)] = True
        # Recur for all the vertices adjacent to this vertex 
      for i in self.findneighbors(start):
          if i == finish:
            visited[int(i)] = True
            answer = []
            count = -1
            for i in visited:
              count += 1
              if i == True:
                answer.append(count)
            return answer
          if visited[int(i)] == False: 
              self.DFSUtil(i,finish,visited) 
  
  
    # The function to do DFS traversal. It uses 
    # recursive DFSUtil() 
  def findpathdepthfirst(self,start,finish): 
  
        # Mark all the vertices as not visited 
      visited = [False]*(len(self.graph)) * 2
  
        # Call the recursive helper function to print 
        # DFS traversal 
      return(self.DFSUtil(start,finish,visited)) 


#https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/    
        # Function to print a BFS of graph 
  def findpathbreathfirst(self,start,finish): 
      print('cat')
        # Mark all the vertices as not visited 
      visited = [False] * (len(self.graph)) * 2 
  
        # Create a queue for BFS 
      queue = [] 
  
        # Mark the source node as  
        # visited and enqueue it 
      queue.append(start) 
      visited[start] = True
  
      while queue: 
  
            # Dequeue a vertex from  
            # queue and print it 
          s = queue.pop(0) 
          print(s)
          print (s, end = " ") 
  
            # Get all adjacent vertices of the 
            # dequeued vertex s. If a adjacent 
            # has not been visited, then mark it 
            # visited and enqueue it 
          for i in self.graph[s]: 
              print(i)
              if visited[i] == False: 
                  queue.append(i) 
                  visited[i] = True
      return(queue)
    

def main():
  Data = open('ADJ.txt', 'r+')#from file put into variable
  line = Data.readlines()
  ADJ = Graph()
  for i in range(len(line)):
    if i >= 2:
      if i == int(line[1]) + 2:
          break
      if i <= int(line[1]) + 1:
        number = line[i]
        ADJ.addEdge(number[0],number[1])
        #use stripped first line of variable to initalize a AJlist of apporpite size into a variable
  #store next line in a varabile to be used to make sure i didn't make a mistake
  #from the file the next lines are vertices test to make sure they are vertices then add them to the AJlist keep track of how many i add and compare to the stored value to make sure i am on track
  #store next line in a variable to be used to make sure i dint't make a mistake on the next step

  numbers = []
  for i in range(len(line)):
    if i >= int(line[1]) + 3:
      number = line[i]
      print(ADJ.findpathdepthfirst(number[0],number[1]))

  for number in numbers:
    print(ADJ.findpathbreathfirst(number[0],number[1]))
  #first use the depth search method and then the breath search method the same test cases keep track of test cases may need to save them to re use them and compare to saved variable to make sure right number of test cases are bing used
  print('code is done')
  Data.close()


main()

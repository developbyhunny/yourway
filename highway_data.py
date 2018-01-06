import sys

class Vertex:

	def __init__(self, node):
		self.id = node
		self.adjacent = {}

		# Set distance to infinity for all nodes	
		self.distance = sys.maxint
		# Mark all nodes unvisited
		self.visited = False
		# Predecessor
		self.previous = None

	def add_neighbor(self, neighbor, weight=0):
		self.adjacent[neighbor] = weight

	def get_connections(self):
		return self.adjacent.keys()

	def get_id(self):
		return self.id

	def get_weight(self, neighbor):
		return self.adjacent[neighbor]

	def set_distance(self, dist):
		self.distance = dist
	
	def get_distance(self):
		return self.distance
	
	def set_previous(self, prev):
		self.previous = prev
	
	def set_visited(self):
		self.visited = True
	
	def __str__(self):
		return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])


class Graph:

	def __init__(self):
		self.vert_dict = {}
		self.num_vertices = 0
	
	def __iter__(self):
		return iter(self.vert_dict.values())

	def add_vertex(self, node):
		self.num_vertices = self.num_vertices + 1
		new_vertex = Vertex(node)
		self.vert_dict[node] = new_vertex
		return new_vertex
	
	def get_vertex(self, n):
		if n in self.vert_dict:
			return self.vert_dict[n]
		else:
			return None
	
	def add_edge(self, frm, to, cost = 0):
		if frm not in self.vert_dict:
			self.add_vertex(frm)
		if to not in self.vert_dict:
			self.add_vertex(to)

		self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
		self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

	def get_vertices(self):
		return self.vert_dict.keys()

	def set_previous(self, current):
		self.previous = current

	def get_previous(self, current):
		return self.previous

def shortest(v, path):
#''' make shortest path from v.previous'''

	if v.previous:
		path.append(v.previous.get_id())
		shortest(v.previous, path)
	return

import heapq

def dijkstra(aGraph, start, target):
    print '''Dijkstra's shortest path'''
    # Set the distance for the start node to zero 
    start.set_distance(0)

    # Put tuple pair into the priority queue
    unvisited_queue = [(v.get_distance(),v) for v in aGraph]
    heapq.heapify(unvisited_queue)

    while len(unvisited_queue):
        # Pops a vertex with the smallest distance 
        uv = heapq.heappop(unvisited_queue)
        current = uv[1]
        current.set_visited()

#for next in v.adjacent:
       	for next in current.adjacent:
            # if visited, skip
            if next.visited:
                continue
            new_dist = current.get_distance() + current.get_weight(next)
            
            if new_dist < next.get_distance():
                next.set_distance(new_dist)
                next.set_previous(current)
                print 'updated : current = %s next = %s new_dist = %s'%(current.get_id(), next.get_id(), next.get_distance())
            else:
                print 'not updated : current = %s next = %s new_dist = %s'%(current.get_id(), next.get_id(), next.get_distance())


# Rebuild heap
        # 1. Pop every item
        while len(unvisited_queue):
            heapq.heappop(unvisited_queue)
        # 2. Put all vertices not visited into the queue
        unvisited_queue = [(v.get_distance(),v) for v in aGraph if not v.visited]
        heapq.heapify(unvisited_queue)
    
def get_data_from_main(source,destination):

	#VERTEX
	g = Graph()
	g.add_vertex('a')
	g.add_vertex('b')
	g.add_vertex('c')
	g.add_vertex('d')
	g.add_vertex('e')
	g.add_vertex('f')
	g.add_vertex('g')
	g.add_vertex('h')
	g.add_vertex('i')
	g.add_vertex('j')
	g.add_vertex('k')
	g.add_vertex('l')
	g.add_vertex('m')
	g.add_vertex('n')
	g.add_vertex('o')
	g.add_vertex('p')
	g.add_vertex('q')
	g.add_vertex('r')
	g.add_vertex('s')
	g.add_vertex('t')
	g.add_vertex('u')
	g.add_vertex('v')

# EDGES
	g.add_edge('a', 'o',40.6)
	g.add_edge('a', 'v',60.8)
	g.add_edge('a', 'u',57.7)
	g.add_edge('a', 'j',76.5)

	#g.add_edge('b', '-',0)
	#g.add_edge('c', '-',0)

	g.add_edge('d', 'n',31.7)
	g.add_edge('d', 'f',53.2)
	g.add_edge('d', 't',83.7)
	g.add_edge('d', 'r',108)

	g.add_edge('e', 's',87.7)
	g.add_edge('e', 'g',69.2)

	g.add_edge('f', 'q',62)
	g.add_edge('f', 'd',53.2)
	g.add_edge('f', 't',80.9)
	g.add_edge('f', 'r',73.5)

	g.add_edge('g', 'e',49.9)
	g.add_edge('g', 'j',113)
	g.add_edge('g', 'r',105)

	g.add_edge('h', 'r',39.1)
	g.add_edge('h', 'q',52.5)

	g.add_edge('i', 'r',60.3)

	g.add_edge('j', 'g',113)
	g.add_edge('j', 'a',76.5)

	g.add_edge('k', 'u',42.8)
	g.add_edge('k', 'p',35.3)

	#g.add_edge('l', '-',0)

	#g.add_edge('m', '-',0)

	g.add_edge('n', 'd',31.7)
	g.add_edge('n', 'q',93.9)

	g.add_edge('o', 'v',97.2)

	g.add_edge('p', 'k',35.3)
	g.add_edge('p', 't',51.6)

	g.add_edge('q', 'f',60.8)
	g.add_edge('q', 'h',53.2)
	g.add_edge('q', 'n',96.5)

	g.add_edge('r', 'h',39.1)
	g.add_edge('r', 'g',105)
	g.add_edge('r', 'i',60.3)
	g.add_edge('r', 'f',73.5)
	g.add_edge('r', 'd',108)
	g.add_edge('r', 't',59.9)

	g.add_edge('s', 'e',87.7)

	g.add_edge('t', 'd',83.7)
	g.add_edge('t', 'f',80.9)
	g.add_edge('t', 'r',59.9)
	g.add_edge('t', 'p',51.6)

	g.add_edge('u', 'a',57.7)
	g.add_edge('u', 'k',42.8)

	g.add_edge('v', 'a',60.8)
	g.add_edge('v', 'o',97.2)

	print 'Graph data:'
	for v in g:
		for w in v.get_connections():
			vid = v.get_id()
			wid = w.get_id()
			print '( %s , %s, %3d)'  % ( vid, wid, v.get_weight(w))

	dijkstra(g, g.get_vertex(source), g.get_vertex(destination))
	target = g.get_vertex(destination)
	path = [target.get_id()]
	shortest(target, path)
	path.reverse()
	return path


#if __name__ == '__main__':


	#dijkstra(g, g.get_vertex('a'), g.get_vertex('e'))
	#target = g.get_vertex('e')
	#path = [target.get_id()]
	#shortest(target, path)
	#path.reverse()
	#print(path)
	#print 'The shortest path : %s' %(path[::-1])


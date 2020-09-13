# Graph Classes

### Overview

Easy Graph provides two types of graph classes, Graph and DiGraph, which is undirected graph and directed graph, respectively.

Both of these graph classes allow for any hashable Python objects as nodes, and edges are saved as Python dictionary type with custom key values and data.



## Graph - Undirected Graph

```python
class Graph(object):
	"""
	Base class for undirected graphs.
	
	Nodes are allowed for any hashable Python objects, including int, string, dict, etc.
	Edges are stored as Python dict type, with optional key/value attributes.
	
	
	"""
```



### Examples



#### Graph Creation:

Create an empty undirected graph with no nodes and edges.

```python
G = eg.Graph()
```

Create a deep copy graph *G2* from existing Graph *G1*.

```python
G2 = G1.copy()
```

Create subgraph of existing Graph with a list of nodes.

```python
G_sub = G.nodes_subgraph(from_nodes = [1,2,3])
```

Create an ego network graph of one center node from an existing Graph.

```python
ego_network = G.ego_subgraph(center='Jack')
```



#### Nodes:

Add one node, type of which is any hashable Python object, such as int, string, dict, or even Graph itself. You can add with node attributes using Python dict type.

```python
G.add_node('a')
G.add_node('hello world')
G.add_node(1)

G.add_node('Jack', node_attr={
    'age': 10,
    'gender': 'M'
})
```



Add nodes with a list of nodes. You can add with node attributes using a list of Python dict type, each of which is the attribute of each node, respectively.

```python
G.add_nodes([1, 2, 'a', 'b'])
G.add_nodes(range(1, 200))

G.add_nodes(['Jack', 'Tom', 'Lily'], nodes_attr=[
    {
        'age': 10,
        'gender': 'M'
    },
    {
        'age': 11,
        'gender': 'M'
    },
    {
        'age': 10,
        'gender': 'F'
    }
])
```



Remove one node or nodes from your graph.

```python
G.remove_node('Jack')
G.remove_nodes([1, 2, 'a', 'b'])
```



#### Edges:

Add one edge. Nodes of this edge will be automatically added to the graph, if they do not exist.

```python
G.add_edge(1,2)
G.add_edge('Jack', 'Tom')
```



Add a list of edges.

```python
G.add_edges([
    (1, 2),
    (3, 4),
    ('Jack', 'Tom')
])
```



Add edge with attributes, edge weight, for example,

```python
G.add_edge(1, 2, edges_attr={
    'weight': 20
})

G.add_edges([(1,2), (2, 3)], edges_attr=[
    {
        'weight': 20
    },
    {
        'weight': 15
    }
])
```



Add (weighted) edges from files. Each line is in form like `a b 23.0`, denoting edge and its weight.

```python
""" ./karate_club.txt
Jack Mary 23.0
Mary Tom 15.0
Tom Ben 20.0
"""
G.add_edges_from_file(file='./karate_club.txt', weighted=True)
```



Remove edge or a list of edges.

```python
G.remove_edge(1,2)
G.remove_edge([
    ('Jack', 'Mary'),
    ('Mary', 'Tom')
])
```



#### Properties:

Returns the adjacency matrix of the graph.

```python
G.adj
```

Returns all the nodes with their attributes. 

```python
G.nodes
```

Returns all the edges with their attributes.

```python
G.edges
```



#### Neighbors:

Returns an iterator of a node's neighbors.

```python
G = eg.Graph()
G.add_edges([(1,2), (2,3), (2,4)])

for neighbor in G.neighbors(node=2):
    print(neighbor)
```



#### Degree:

Returns the weighted degree of of each node, the key of weight is 'weight' by default,

```python
G.degree()
G.degree(weight='weight')
```

or you can customize the weight key.

```python
G.degree(weight='weight_1')
```

If the graph is not weighted, all the weights will be regarded as 1.



#### Isomorphic Graph:

Considering that the nodes of your graph may be any possible hashable Python object, you can get an isomorphic graph of the original one, with each node switched to its index.

The following method returns this isomorphic graph and index-to-node dictionary as well as node-to-index dictionary.

```python
G_index_graph, index_of_node, node_of_index = G.to_index_node_graph()
```



## Graph - Directed Graph

```python
class DiGraph(object):
   	"""
   	Base class for directed graphs.
	
	Nodes are allowed for any hashable Python objects, including int, string, dict, etc.
	Edges are stored as Python dict type, with optional key/value attributes.
	
	
   	"""
```



### Examples



#### Graph Creation:

Create an empty directed graph with no nodes and edges.

```python
G = eg.DiGraph()
```

Create a deep copy graph *G2* from existing Graph *G1*.

```python
G2 = G1.copy()
```

Create subgraph of existing Graph with a list of nodes.

```python
G_sub = G.nodes_subgraph(from_nodes = [1,2,3])
```

Create an ego network graph of one center node from an existing Graph.

```python
ego_network = G.ego_subgraph(center='Jack')
```



#### Nodes:

Add one node, type of which is any hashable Python object, such as int, string, dict, or even Graph itself. You can add with node attributes using Python dict type.

```python
G.add_node('a')
G.add_node('hello world')
G.add_node(1)

G.add_node('Jack', node_attr={
    'age': 10,
    'gender': 'M'
})
```



Add nodes with a list of nodes. You can add with node attributes using a list of Python dict type, each of which is the attribute of each node, respectively.

```python
G.add_nodes([1, 2, 'a', 'b'])
G.add_nodes(range(1, 200))

G.add_nodes(['Jack', 'Tom', 'Lily'], nodes_attr=[
    {
        'age': 10,
        'gender': 'M'
    },
    {
        'age': 11,
        'gender': 'M'
    },
    {
        'age': 10,
        'gender': 'F'
    }
])
```



Remove one node or nodes from your graph.

```python
G.remove_node('Jack')
G.remove_nodes([1, 2, 'a', 'b'])
```



#### Edges:

Add one edge. Nodes of this edge will be automatically added to the directed graph, if they do not exist.

```python
G.add_edge(1,2)
G.add_edge('Jack', 'Tom')
```



Add a list of edges.

```python
G.add_edges([
    (1, 2),
    (3, 4),
    ('Jack', 'Tom')
])
```



Add edge with attributes, edge weight, for example,

```python
G.add_edge(1, 2, edges_attr={
    'weight': 20
})

G.add_edges([(1,2), (2, 3)], edges_attr=[
    {
        'weight': 20
    },
    {
        'weight': 15
    }
])
```



Add (weighted) edges from files. Each line is in form like `a b 23.0`, denoting edge and its weight.

```python
""" ./karate_club.txt
Jack Mary 23.0
Mary Tom 15.0
Tom Ben 20.0
"""
G.add_edges_from_file(file='./karate_club.txt', weighted=True)
```



Remove edge or a list of edges.

```python
G.remove_edge(1,2)
G.remove_edge([
    ('Jack', 'Mary'),
    ('Mary', 'Tom')
])
```



#### Properties:

Returns the adjacency matrix of the graph.

```python
G.adj
```

Returns all the nodes with their attributes. 

```python
G.nodes
```

Returns all the edges with their attributes.

```python
G.edges
```



#### Neighbors:

Returns an iterator of a node's successors .

```python
G = eg.Graph()
G.add_edges([(1,2), (2,3), (2,4)])

for neighbor in G.successors(node=2):
    print(neighbor)
```

Returns an iterator of a node's predecessors.

```python
G = eg.Graph()
G.add_edges([(1,2), (2,3), (2,4)])

for neighbor in G.predecessors(node=2):
    print(neighbor)
```



#### Degree:

Returns the weighted degree of of each node, and the key of weight is 'weight' by default. For directed graph, it returns the sum of out degree and in degree,

```python
G.degree()
G.degree(weight='weight')
```

or you can customize the weight key.

```python
G.degree(weight='weight_1')
```

If the graph is not weighted, all the weights will be regarded as 1.



Also, you can get the out degree and in degree separately,

```python
G.out_degree(weight='weight')
G.in_degree(weight='weight')
```



#### Isomorphic Graph:

Considering that the nodes of your graph may be any possible hashable Python object, you can get an isomorphic graph of the original one, with each node switched to its index.

The following method returns this isomorphic graph and index-to-node dictionary as well as node-to-index dictionary.

```python
G_index_graph, index_of_node, node_of_index = G.to_index_node_graph()
```






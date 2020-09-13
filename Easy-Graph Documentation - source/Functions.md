# Functions

For now, Easy Graph has implemented graph computation functions, including fundamental methods, for example, connected/biconnected components, community detection, PageRank; as well as advanced methods, for example, structure hole spanners detection, graph embedding. All of these functions are implemented with Python language in Easy Graph, even if the original authors of some graph computing methods are using different language, C and C++, for instance. 

With the help of Easy Graph, users can easily try and compare different graph computation methods in the same platform.

 ## Components

Easy Graph can help users check whether the graph (undirected) is connected/biconnected or not. It can also provide with connected/biconnected components.

### Connected Components

Returns whether the graph is connected or not.

```python
# G: <class 'Graph'>
is_connected(G)
```

Returns the number of connected components of graph.

```python
number_connected_components(G)
```

Returns the connected components of each node in graph.

```python
connected_components(G)
```

Returns the connected component of one node `Jack`.

```python
connected_component_of_node(G, node='Jack')
```



### Biconnected Components

Returns whether the graph is biconnected or not.

```python
# G: <class 'Graph'>
is_biconnected(G)
```

Returns the biconnected components of each node in graph.

```python
connected_components(G)
```

Returns a generator of nodes in all biconnected components.

```python
generator_biconnected_components_nodes(G)
```

Returns a generator of edges in all biconnected components.

```python
generator_biconnected_components_edges(G)
```

Returns a generator of the articulation points.

```python
generator_articulation_points(G)
```



## Community

### Greedy Modularity Community Detection

Find communities in graph using Clauset-Newman-Moore greedy modularity maximization. This method currently supports the Graph class.

Greedy modularity maximization begins with each node in its own community and joins the pair of communities that most increases modularity until no such pair exists.

```python
greedy_modularity_communities(G, weight='weight')
```

> References
>
> [1] M. E. J Newman 'Networks: An Introduction', page 224 Oxford University Press 2011.
>
> [2] Clauset A, Newman M E J, Moore C. Finding community structure in very large networks[J]. Physical review E, 2004, 70(6): 066111.



## Structural Holes Spanners

Easy Graph has implemented several most commonly used structural holes spanners detection methods, including HIS, MaxD, HAM, Common_Greedy,  AP_Greedy. Burt‘s evaluation metric for structural holes, Effective Size, Efficiency, Constraint and Hierarchy, are also included. 

### HIS & MaxD

Both **HIS** and **MaxD** are methods in [1]. The authors developed these two methods to find the structural holes spanners, base on theory of information diffusion. 

Returns the value of `S`, `I`, `H` ,defined in **HIS** of [1], of each node in the graph. Note that `H` quantifies the possibility that a node is a structural hole spanner. To use `HIS` method, you should provide the community detection result as parameter.

```python
get_structural_holes_HIS(G,
                         C = [frozenset([1,2,3]), frozenset([4,5,6])], # Two communities
                         epsilon = 0.01,
                         weight = 'weight'
                         )
```

Returns the top k nodes as structural hole spanners, using **MaxD**.

```python
get_structural_holes_MaxD(G,
                          k_size = 5, # To find top five structural holes spanners.
                          C = [frozenset([1,2,3]), frozenset([4,5,6])] # Two communities
                         )
```



### HAM

Use **HAM** to jointly detect structural holes spanners as well as communities. The related research paper is [2].  

Returns the top-k nodes as structural hole spanners, and a Ndarray of labeled communities of the nodes.

```python
get_structural_holes_HAM(G,
                       	 k = 2, # To find top two structural holes spanners.
                         c = 2,
                         ground_truth_labels = [[0], [0], [1], [0], [1]] # The ground truth labels for each node - community detection result, for example.
                        ) 
```



### common_greedy & AP_greedy

The authors of [3] developed two methods, **common_greedy** and **AP_greedy**, to find the top k nodes as structural holes spanners. Both of them are greedy methods and **AP_greedy** leverages articulation points to speedup the procedure.

Returns the top k nodes as structural hole spanners, using **common_greedy**.

```python
common_greedy(G,
              k = 3, # To find top three structural holes spanners.
              c = 1.0, # To define zeta: zeta = c * (n*n*n), and zeta is the large value assigned as the shortest distance of two unreachable vertices.
              weight = 'weight')
```

Returns the top k nodes as structural hole spanners, using **AP_greedy**.

```python
AP_greedy(G,
          k = 3, # To find top three structural holes spanners.
          c = 1.0, # To define zeta: zeta = c * (n*n*n), and zeta is the large value assigned as the shortest distance of two unreachable vertices.
          weight = 'weight')
```



### Burt's Metrics

When Burt put forward theory of structural hole spanners [4] in 1992, he also raised four metrics for structural hole evaluation: Effective Size, Efficiency, Constraint, Hierarchy. They are also implemented in Easy Graph.

Returns the Effective Size of the nodes in the graph.

```python
effective_size(G,
               nodes=[1,2,3], # Compute the Effective Size of some nodes. The default is None for all nodes in G.
               weight='weight' # The weight key of the graph. The default is None for unweighted graph.
               )
```

Returns the Efficiency of the nodes in the graph.

```python
efficiency(G,
           nodes=[1,2,3], # Compute the Efficiency of some nodes. The default is None for all nodes in G.
           weight='weight' # The weight key of the graph. The default is None for unweighted graph.
           )
```

Returns the Constraint of nodes.

```python
constraint(G,
           nodes=[1,2,3], # Compute the Constraint of some nodes. The default is None for all nodes in G.
           weight='weight', # The weight key of the graph. The default is None for unweighted graph.
           n_workers=4 # Parallel computing on four workers. The default is None for serial computing.
           )
```



> References
>
> [1] Lou T, Tang J. Mining structural hole spanners through information diffusion in social networks[C]//Proceedings of the 22nd international conference on World Wide Web. 2013: 825-836.
>
> [2] He L, Lu C T, Ma J, et al. Joint community and structural hole spanner detection via harmonic modularity[C]//Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining. 2016: 875-884.
>
> [3] Xu W, Rezvani M, Liang W, et al. Efficient Algorithms for the Identification of Top-$ k $ Structural Hole Spanners in Large Social Networks[J]. IEEE Transactions on Knowledge and Data Engineering, 2017, 29(5): 1017-1030.
>
> [4] Burt R S. Structural holes: The social structure of competition[M]. Harvard university press, 2009.

 

## Graph Embedding

Easy Graph has implemented several methods of graph embedding.

### DeepWalk

Returns

1. The embedding vector of each node via DeepWalk [1]
2. The most similar nodes of each node and its similarity

```python
deepwalk(G,
         dimensions=128, # The graph embedding dimensions.
         walk_length=80, # Walk length of each random walks.
         num_walks=10, # Number of random walks.
         skip_gram_params = dict( # The skip_gram parameters in Python package gensim.
         	window=10,
            min_count=1,
            batch_words=4,
            iter=15
         ))
```



 ### Node2Vec

Returns

1. The embedding vector of each node via node2vec [2]
2. The most similar nodes of each node and its similarity

```python
node2vec(G,
         dimensions=128, # The graph embedding dimensions.
         walk_length=80, # Walk length of each random walks.
         num_walks=10, # Number of random walks.
         p=1.0, # The `p` possibility in random walk in [2]
         q=1.0, # The `q` possibility in random walk in [2]
         weight_key='weight',
         skip_gram_params=dict( # The skip_gram parameters in Python package gensim.
         	window=10,
            min_count=1,
            batch_words=4
         ))
```



### LINE

**LINE** is a graph embedding method in [3].

```python
model = LINE(G, 
             embedding_size=16, 
             order='all') # The order of model LINE. 'first'，'second' or 'all'.

model.train(batch_size=1024, epochs=1, verbose=2)
embeddings = model.get_embeddings() # Returns the graph embedding results.
```



### SDNE

**SDNE** is a graph embedding method in [4].

```python
model = SDNE(G, 
             hidden_size=[256, 128]) # The hidden size in SDNE.

model.train(batch_size=3000, epochs=40, verbose=2)
embeddings = model.get_embeddings() # Returns the graph embedding results.
```



> References
>
> [1] Perozzi B, Al-Rfou R, Skiena S. Deepwalk: Online learning of social representations[C]//Proceedings of the 20th ACM SIGKDD international conference on Knowledge Discovery and Data mining. 2014: 701-710.  
>
> [2] Grover A, Leskovec J. node2vec: Scalable feature learning for networks[C]//Proceedings of the 22nd ACM SIGKDD international conference on Knowledge Discovery and Data mining. 2016: 855-864.
>
> [3] Tang J, Qu M, Wang M, et al. Line: Large-scale information network embedding[C]//Proceedings of the 24th international conference on World Wide Web. 2015: 1067-1077  
>
> [4] Wang D, Cui P, Zhu W. Structural deep network embedding[C]//Proceedings of the 22nd ACM SIGKDD international conference on Knowledge Discovery and Data mining. 2016: 1225-1234.




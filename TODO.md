# TODO

## 辅助函数

- [ ] 随机数生成 (pseudo random number generator)
  - [ ] Xorshift
    - [ ] Xorshift128
    - [ ] Xorshift128*
    - [x] Xorshift128+
- [ ] 字符串hash
  - [x] SipHash

## 基本数据结构

| List               | Array | Stack | Queue | Deque | Graph | DiGraph |
| ------------------ | ----- | ----- | ----- | ----- | ----- | ------- |
| Static Array       |  [ ]  |       |       |       |       |         |
| Fixed Array        |  [x]  |  [x]  |  [x]  |  [ ]  |  [ ]  |   [x]   |
| Dynamic Array      |  [x]  |  [x]  |       |       |  [ ]  |   [ ]   |
| Singly-Linked List |       |  [ ]  |       |       |       |         |
| Doubly-Linked List |       |  [ ]  |  [ ]  |  [ ]  |  [ ]  |   [x]   |

| Tree               | Set | Multiset | Map | Multimap | Heap | PriorityQueue | PriorityDeque |
| ------------------ | --- | -------- | --- | -------- | ---- | ------------- | ------------- |
| Binary Search Tree | [x] |   [ ]    | [x] |   [ ]    |  [ ] |      [ ]      |      [ ]      | 
| AVL Tree           | [x] |   [ ]    | [x] |   [ ]    |  [ ] |      [ ]      |      [ ]      |
| Red-black Tree     | [ ] |   [ ]    | [ ] |   [ ]    |  [ ] |      [ ]      |      [ ]      |

| Heap               | Heap | PriorityQueue |
| ------------------ | ---- | ------------- |
| d-ary Heap         |  [ ] |      [x]      |
| Leftist Tree       |  [ ] |      [ ]      |
| Binomial Heap      |  [ ] |      [ ]      |
| Fibonacci Heap     |  [ ] |      [ ]      |

## 排序 (Sorting)

- [ ] 求逆序数
- [ ] selection sort
- [ ] insertion sort
- [x] heap sort
- [ ] counting sort
- [ ] radix sort
  - [ ] lsd
  - [ ] msd

## 计算

- [ ] 矩阵
- [ ] 大数运算
  - [ ] 进制转换
  - [ ] 整数
    - [ ] 加/减法
    - [ ] 乘法
      - [ ] 竖式乘法
      - [ ] Toom-Cook
      - [ ] NTT
  - [ ] 分数
  - [ ] 浮点数

## 数据结构 (Data Structure)

- [ ] Bit Set
- [ ] HashTable
- [ ] Trie
- [ ] Treap
- [ ] Catersian Tree
- [ ] Interval Tree
- [ ] Segment Tree
- [ ] Disjoint Set
- [ ] Binary Indexed Tree
- [ ] Skip List
- [ ] Splay Tree
- [ ] B Tree

## 递归 (Recursion)

- [ ] 矩阵乘法
- [ ] 动态规划

## 数组 (Array)

- [ ] 匹配 (matching)
  - [ ] 单串
    - [ ] MP
    - [ ] KMP
  - [ ] 多串
    - [ ] Aho Corasick
  - [ ] Regular Expression
  - [ ] Parsing
- [ ] 后缀数组 (Suffix Array)
  - [ ] prefix doubling
  - [ ] DC3
  - [x] LCP Array
- [ ] BWT
- [ ] permutation
  - [ ] prev/next permutation
- [ ] 回文子串长度
  - [x] Manacher's Algorithm
- [ ] Range Minimum Query
  - [ ] Full Table
  - [ ] Tree Table
  - [ ] Sparse Table
  - [ ] Fischer-Heun Table

## 图论 (Graph Theory)

- [ ] Euler Tour/Path
- [ ] Lowest Common Ancestor

## 图论与搜索 (Graph Theory and Search)

- [ ] Breath-First search
- [ ] Depth-First search
  - [x] 拓扑排序 (Topological sort)
  - [x] 强连通分量 (Strongly Connected Components)
  - [ ] 双连通分量 (Biconnected Components)
    - [ ] Finding articulation points
    - [ ] Finding bridges

## 图论与优化 (Graph Theory and Optimization)

- [ ] 贪婪
  - [ ] 最小生成树 (Minimum Spanning Tree)
    - [x] Prim's algorithm
    - [x] Kruskal's algorithm
- [ ] 最短路径 (Shortest Path)
  - [ ] Floyd-Warshall
  - [x] Bellman-Ford
  - [ ] Dijkstra
- [ ] 网络流
  - [ ] Edmonds-Karp

## 计算几何 (Computational Geometry)

## 数论 (Number Theory)

## 组合与计数 (Combinatorics)

## 博弈论 (Game Theory)

## 概率 (Probability)

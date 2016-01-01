==============
String problem
==============

:tags: dp

注意，这个问题中substring是subsequence意思。

已知字符串S和T，假设函数P能求出一个字符串的所有subsequence，这个题目就是要找出\ :math:`P(S) \setminus P(T)`\ 中最短的。不妨令\ :code:`Q(x,y)`\ 表示\ :math:`P(x) \setminus P(y)`\ 中最短的字符串

.. code::

    P("abc") = {"abc", "ab", "ac", "bc", "a", "b", "c"}

若字符串长度为N，总共会有\ :math:`2^N-1`\ 个subsequence，因此把所有subsequence列一遍是不现实的。

不妨设\ :code:`U = Q(S[0..i], T[0..j])`\ 。若U的最后一个字符不是\ :code:`T[j]`\ ，则\ :code:`Q(S[0..i], T[0..j+1]) = U`\ 。

:math:`\implies`

.. to workaround KaTeX's bug (https://github.com/Khan/KaTeX/issues/190)

证明。因为\ :math:`P(T[0..j]) \subseteq P(T[0..j+1])`\ ，所以\ :math:`V \in P(S[0..i]) \setminus P(T[0..j+1]) \implies V \in P(S[0..i]) \setminus P(T[0..j])`\ 。若有\ :code:`V = Q(S[0..i], T[0..j+1])`\ 且V的长度小于U，那么与\ :code:`U = Q(S[0..i], T[0..j])`\ 矛盾。

用\ :code:`R(S[0..i])`\ 表示S[0..i-1]所有subsequence，分别加上S[i-1]。 不妨用\ :code:`L(x,y)`\ 表示\ :math:`x \setminus y`\ 中最短字符串的长度。令\ :code:`L1(i,j) = L(P(S[0..i]), P(T[0..j]))`\ ，令\ :code:`L2(i,j) = L(P(R[0..i]), P(T[0..j]))`\ 

.. code::

    L1(i,j) = min(L2(0,j), L2(1,j), ... , L2(i,j))
    L1(i,j) = min(L1(i-1,j), L2(i,j))

若\ :math:`S[i] \neq T[j]`\ ，\ :code:`L2(i,j) = L2(i-1,j)`

若\ :math:`S[i] = T[j]`\ ，\ :code:`L2(i,j) = 1 + L1(i-1,j-1)`

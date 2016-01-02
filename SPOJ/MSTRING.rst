==============
String problem
==============

:tags: dp

注意，这个问题中substring是subsequence意思。

令\ :code:`L(x, y) = reduce(min, [|s| FOR s <- (powerset(x) \ powerset(y))])`

已知\ :code:`S : String()`\ 和\ :code:`T : String()`\ ，这个题就是要求\ :code:`L(S, T)`\ 。因为\ :code:`(|S| = N) => (|powerset(S)| = 2**N)`\ ，因此把所有subsequence列一遍是不现实的。

.. code::

    U : String()

    (U <- powerset(S[:i])) /\ (|U| = L(S[:i], T[:j])) /\ (U[-1] =/= T[j]) => (|U| = L(S[:i], T[:j+1]))

证明。

因为\ :code:`powerset(T[:j]) =< P(T[:j+1])`\ ，所以

.. code::

    V : String()

    (V <- (powerset(S[:i]) \ powerset(T[:j+1]))) => (V <- (powerset(S[:i]) \ powerset(T[:j])))

若\ :code:`|V| < |U|`\ ，则\ :code:`L(S[:i], T[:j]) =< |V| < |U|` 与 :code:`L(S[:i], T[:j]) = |U|` 矛盾

令\ :code:`R(x) = {s+[x[-1]] FOR s <- powerset(x[:-1])}`\ ，\ :code:`L'(x,y) = reduce(min, [|s| FOR s <- (R(x) \ powerset(y))])`\ ，有

.. code::

    L(S[:i],T[:j]) = reduce(min, {L'(S[:k], T[:j]) FOR k <- range(0,i)})
                   = min(L(S[:i-1],T[:j]), L'(S[:i],T[:j]))



.. code::

    (S[i] =/= T[j]) => (L'(S[:i], T[:j]) = L'(S[:i-1], T[:j]))


类似上面，用反证法即可证明


.. code::

    (S[i] = T[j]) => L'(S[:i],T[:j]) = 1 + L(S[:i-1],T[:j-1])

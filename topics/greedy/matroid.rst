=======
Matroid
=======


定义
====

若元素类型为\ :code:`X`\ ，Matroid :code:`(E,M)`\ 中，\ :code:`E : Set(X)`\ ，\ :code:`M : Set(Set(X))`\ 满足以下条件

.. code::

    S : Set(X)

    (S <- M) => (S =< E)

继承性: hereditary property

.. code::

    S : Set(X)
    P : Set(X)

    (S <- M) => ((P =< S) => (P <- M))

扩充性: augmentation property, or independent set exchange property

.. code::

    S : Set(X)
    T : Set(X)

    (S <- M) /\ (T <- M) /\ (|S| > |T|) => (EXISTS (e : X) <- (S \ T), (T \/ {e}) <- M)


Basis
=====

定义集合\ :code:`B : Set(Set(X))`\ ，满足

.. code::

    S : Set(X)
    T : Set(X)

    (S <- M) => NOT EXISTS T <- M, ((S < T) <=> (S <- B))


性质一
------

uniformity property

.. code::

    S : Set(X)
    T : Set(X)

    (S <- B) /\ (T <- B) => |S| = |T|

证明：

若\ :code:`|S| > |T|`

由扩充性可得\ :code:`EXISTS (e:X) <- (S \ T), (T \/ {e}) <- M`

即\ :code:`EXISTS (R:Set(X)) <- M, T < R`\ (\ :code:`R = T \/ {e}`\ )

而由Basis的定义可得\ :code:`NOT EXISTS R <- M, T < R`

与前一条结论矛盾，故假设不成立。

同理可得，\ :code:`|S| < |T|`\ 也不成立。

故\ :code:`|S| = |T|`\ 。


性质二
------

将集合\ :code:`E`\ 的元素任意排列，按以下步骤执行，得到\ :code:`S <- B`\ 。

.. code::

    S <= {}
    FOR EACH e <- E
      IF (S \/ {e}) <- M
        S <= S \/ {e}
      ENDIF
    ENDFOR

证明

假设\ :code:`S </- B`\ ，由集合\ :code:`B`\ 的定义 可得\ :code:`EXISTS (T:Set(X)) <- M, S < T`

即\ :code:`|T| > |S|` ，由扩充性可得，\ :code:`EXISTS (e:X) <- (T \ S), (S \/ {e}) <- M`

由Matroid的定义可得，\ :code:`T =< E`\ ，即\ :code:`e <- E`

不妨设执行过程中，\ :code:`NOT (S' \/ {e}) </- M`

因为\ :code:`S' =< S`\ ，所以\ :code:`(S' \/ {e}) =< (S \/ {e})`

由继承性可得，\ :code:`(S' \/ {e}) <- M`

与\ :code:`(S' \/ {e}) </- M`\ 矛盾。

故假设不成立，即\ :code:`S <- B`


Max-Weighted Basis
------------------

假设\ :code:`E`\ 中每个元素都有一个权重，把\ :code:`E`\ 中所有元素按权重从大到小排列后，执行Basis性质二中的步骤，得到的\ :code:`S`\ 就是总权重最大的Basis。

证明

假设存在\ :code:`T : Set(X)`\ ，满足

.. code::

    (T <- B) /\ (reduce(+, T) > reduce(+, S))

由Basis性质一可得，\ :code:`|S| = |T|`

把\ :code:`S`\ 和\ :code:`T`\ ，分别按权重从大到小排列，即


.. code::

    (i < j) => (weight(S[i]) >= weight(S[j]))
    (i < j) => (weight(T[i]) >= weight(T[j]))


不妨设有k使得

.. code::

    (i < k) => (weight(S[i]) >= weight(T[i]))
    weight(S[k]) < weight(T[k])


令

.. code::

    S' = reduce(\/, [{e} FOR (e:X) <- S[:k]])
    T' = reduce(\/, [{e} FOR (e:X) <- T[:k+1])

:code:`|S'| = k < k+1 = |T|`\ ，由扩充性可得，\ :code:`EXISTS e <- (T' \ S'), (S' \/ {e}) \in M`

:code:`weight(e) >= weight(T[k]) > weight(S[k])`

不妨设执行过程中，\ :code:`(S'' \/ {e}) </- M`\ 。

因为\ :code:`S'' =< S'`\ ，所以\ :code:`(S'' \/ {e}) =< (S' \/ {e})`\

由继承性可得，\ :code:`(S'' \/ {e}) <- M`\ 。

与\ :code:`S'' \/ {e} </- M`\ 矛盾。

所以假设不成立，\ :code:`S`\ 就是总权重最大的Basis。

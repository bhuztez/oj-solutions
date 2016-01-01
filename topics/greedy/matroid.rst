=======
Matroid
=======


定义
====

Matroid :math:`(E, M)`\ 。定义集合\ :math:`E`\ 和集合\ :math:`M`\ ，满足以下条件

:math:`\implies`

.. to workaround KaTeX's bug (https://github.com/Khan/KaTeX/issues/190)

* :math:`\forall S \in M, S \subseteq E`
* 非空 :math:`\emptyset \in M`
* 继承性\ [#]_\ 。 :math:`\forall S \in M, P \subseteq S \implies P \in M`
* 扩充性\ [#]_\ 。 :math:`\forall S \in M, \forall T \in M, |S| > |T| \implies \exists e \in S \setminus T, T \cup {e} \in M`

.. [#] 继承性: hereditary property
.. [#] 扩充性: augmentation property, or independent set exchange property


Basis
=====

定义集合\ :math:`B`\ ，满足\ :math:`\forall S \in M, \nexists T \in M, S \subset T \iff S \in B`\ 。


性质一
------

:math:`\forall S \in B, \forall T \in B, |S| = |T|`\ [#]_\

.. [#] uniformity property

证明：

假设\ :math:`|S| > |T|`

由扩充性可得\ :math:`\exists e \in S \setminus T, T \cup \{e\} \in M`

即\ :math:`\exists R \in M, T \subset R` (:math:`R = T \cup \{e\}`)

而由basis的定义可得\ :math:`\nexists R \in M, T \subset R`

与前一条结论矛盾，故假设不成立。

同理可得，\ :math:`|S| < |T|`\ 也不成立。

因此\ :math:`|S| = |T|`\ 。


性质二
------

将集合\ :math:`E`\ 的元素任意排列，按以下步骤执行，得到\ :math:`S \in B`\ 。

    :math:`S \gets \emptyset`

    FOR EACH :math:`e \in E`

        IF :math:`S \cup \{ e \} \in M`

            :math:`S \gets S \cup \{ e \}`

        ENDIF

    ENDFOR


证明

假设\ :math:`S \notin B`\ ，由集合\ :math:`B`\ 的定义 可得\ :math:`\exists T \in M, S \subset T`

即\ :math:`|T| > |S|` ，由扩充性可得，\ :math:`\exists e \in T \setminus S, S \cup \{e\} \in M`

由Matroid的定义可得，\ :math:`T \subseteq E`\ ，即\ :math:`e \in E`

不妨设执行过程中，\ :math:`S' \cup \{ e \} \notin M`

因为\ :math:`S' \subseteq S`\ ，所以\ :math:`S' \cup \{ e \} \subseteq S \cup \{ e \}`

由继承性可得，\ :math:`S' \cup \{ e \} \in M`

与\ :math:`S' \cup \{ e \} \notin M`\ 矛盾。

所以假设不成立，即\ :math:`S \in B`


Max-Weighted Basis
------------------

假设\ :math:`E`\ 中每个元素都有一个权重，把\ :math:`E`\ 中所有元素按权重从大到小排列后，执行Basis性质二中的步骤，得到的\ :math:`S`\ 就是总权重最大的Basis。

证明

假设存在\ :math:`T`\ ，满足\ :math:`T \in B, \sum_i weight(T_i) > \sum_i weight(S_i)`

由Basis性质一可得，\ :math:`|S| = |T|`

把\ :math:`S`\ 和\ :math:`T`\ ，分别按权重从大到小排列，即
:math:`i < j \implies weight(S_i) \geq weight(S_j)$`\ ，
:math:`i < j \implies weight(T_i) \geq weight(T_j)`\ 。

不妨设，\ :math:`i < k \implies weight(S_i) \geq weight(T_i)`\ 且\ :math:`weight(S_k) < weight(T_k)`\ 。

令\ :math:`S' = \cup_{i=1}^{k-1}\{S_i\}`\ ，\ :math:`T' = \cup_{i=1}^k\{T_i\}`

:math:`|S'| = k-1 < k = |T|`\ ，由扩充性可得，\ :math:`\exists e \in T' \setminus S', S' \cup \{e\} \in M`

:math:`weight(e) \ge weight(T_k) > weight(S_k)`

不妨设执行过程中，\ :math:`S'' \cup \{ e \} \notin M`\ 。

因为\ :math:`S'' \subseteq S'`\ ，所以\ :math:`S'' \cup \{ e \} \subseteq S' \cup \{ e \}`\ 

由继承性可得，\ :math:`S'' \cup \{ e \} \in M`\ 。

与\ :math:`S'' \cup \{ e \} \notin M`\ 矛盾。

所以假设不成立，\ :math:`S`\ 就是总权重最大的Basis。

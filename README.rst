====================
Online Judge解题报告
====================

主要就是记录一下解题思路，以及证明的思路。假如题目很长，也会有一个简单的概述。不会有任何实际代码，代码随便搜就有了。

除了解题报告以外，还有按\ `主题 <topics/README.rst>`_\ 排列的知识点。

======================= ============
Online Judge            解题报告
======================= ============
`Google Code Jam`__     `GCJ`__
`PKU JudgeOnline`__     `POJ`__
`Sphere online judge`__ `SPOJ`__
`USACO Traning`__       `USACO`__
`UVa Online Judge`__    `UVA`__
======================= ============

.. __: https://code.google.com/codejam/contests.html
.. __: GCJ/README.rst
.. __: http://poj.org/
.. __: POJ/README.rst
.. __: http://www.spoj.com/
.. __: SPOJ/README.rst
.. __: http://train.usaco.org/usacogate/
.. __: USACO/README.rst
.. __: https://uva.onlinejudge.org/
.. __: UVA/README.rst


================================= ==============
习题集                            解题报告
================================= ==============
`Competitive Programming 3`__     `CP3`__
`CS 97SI`__                       `CS97SI`__
`POJ訓練計劃Moon修訂298道題`__    `MOON298`__
================================= ==============

.. __: https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=604
.. __: CP3/README.rst
.. __: http://web.stanford.edu/class/cs97si/
.. __: CS97SI.rst
.. __: http://cs.cysh.cy.edu.tw/php_system/news/upload/POJ%E9%A1%8C%E7%9B%AE%E8%A8%93%E7%B7%B4%E8%A8%88%E5%8A%83.doc
.. __: MOON298.rst


要生成HTML，请在git clone后运行make。


标签定义
========

========== =======================
dp         Dynamic Programming
manacher   Manacher's Algorithm
suffix     Suffix Array
========== =======================


符号定义
========

解题报告中所使用的符号

======================= ======================================
:code:`NOT`             :math:`\neg`
:code:`FORALL`          :math:`\forall`
:code:`EXISTS`          :math:`\exists`
:code:`{}`              :math:`\emptyset`
:code:`<-`              :math:`\in`
:code:`</-`             :math:`\notin`
:code:`=`               :math:`=`
:code:`=/=`             :math:`\neq`
:code:`|x|`             :math:`|x|`
:code:`<`               :math:`<`\ ,\ :math:`\subset`
:code:`=<`              :math:`\leq`\ ,\ :math:`\subseteq`
:code:`/\ `             :math:`\cap`
:code:`\/`              :math:`\cup`
:code:`\ `              :math:`\setminus`
:code:`=>`              implies
:code:`<=>`             iff
:code:`a**b`            :math:`a^b`
:code:`{x FOR x <- S}`  :math:`\{x | x \in S\}`
:code:`<=`              assignment
======================= ======================================


类型定义
========

解题报告中所使用的类型

整数
----

:code:`Integer()`


集合
----

若元素类型为\ :code:`X`\ ，则集合类型为\ :code:`Set(X)`\ 。比如，元素类型为整数的集合为\ :code:`Set(Integer())`\ 。

.. code::

    1 <- {1,2,3}
    4 </- {1,2,3}
    {1} \/ {2} = {1,2}
    {1,2} /\ {2,3} = {2}
    {1,2} \ {2,3} = {1}
    {1,2} = {1,2}
    {1,2} =/= {1,2,3}
    {} < {1}
    {1} < {1,2}

数组
----

若元素类型为\ :code:`X`\ ，则数组类型为\ :code:`Array(X)`\ 。比如，元素类型为整数的数组为\ :code:`Array(Integer())`\ 。

从数组中取元素的符号与Python一致

.. code::

    [1,2,3] = [1,2,3]
    [1,2,3] + [4] = [1,2,3,4]
    ([1,2,3])[0] = 1
    ([1,2,3])[:2] = [1,2]


字符串
------

:code:`String() = Array(Integer())`

字符串就是普通的整数数组


函数定义
========

解题报告中所使用的函数

min
---

求参数中的最小值

.. code::

    min(1,2,3) = 1
    min(2,3) = 2


max
---

求参数中的最大值

.. code::

    max(1,2,3) = 3
    max(1,2) = 2


range
-----

类似Python中的range

.. code::

    range(1,4) = [1,2,3]


size
----

.. code::

    size([1,1,1]) = 3
    size({1,2,3}) = 3


reduce
------

类似Python中的reduce

.. code::

    reduce(+, [1,1,1]) = 3
    reduce(+, [1,2,3]) = 6


powerset
--------

.. code::

    powerset({1,2,3}) = {{},{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}}
    powerset([1,2,3]) = {[],[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]}
    powerset([1,1,2]) = {[],[1,1],[1,2],[1,1,2]}

===================
Range Minimum Query
===================

推荐参考资料CS166里Range Minimum Queries的\ `Lecture Slides`__

.. __: http://web.stanford.edu/class/cs166/lectures/00/Slides00.pdf


虽然叫Range Minimum Query，实际上这个问题是range reduce问题

给定一个数组A，若有 :code:`i<j` 不妨令 :code:`rmq(i,j) = reduce(f, A[i:j])`


Full preprocessing
==================

.. code::

    rmq(i,i+1) = A[i]
    rmq(i,j+1) = f(rmq(i,j), A[j])

:math:`O(n^2), O(1)`


Block Partition
===============

若f满足结合律，即 :code:`x f (y f z) = (x f y) f z`

令block大小为m

单层
----

:math:`O(n), O(m + n/m)`

多层
----

:math:`O(n \cdot log_m n), O(m \cdot log_m n)`

若m为2，这就是一个Binary Indexed Tree

若m为 :math:`\sqrt{n}` 这就是CS166中说的Block Partition


Sparse Table
============

若f还是幂等的，即 :code:`x f y f y = x f y`

:math:`O(n \cdot log n), O(1)`


Fischer-Heun
============

若 :code:`x f y` 要么等于 x ，要么等于 y 。

那么Cartesian Tree Number相同的range，所有查询结果所在位置都相同

每个block内都用full preprocessing

block以上用Sparce Table

:math:`O(n), O(1)`

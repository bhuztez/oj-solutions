==========
大整数运算
==========


数据表示
========

用一个无符号整数数组从低位到高位存绝对值。

size表示数组元素个数以及符号。

比如，0的size就是0。1的size是1，-1的size是-1


进制转换
========

比如x进制abc转y进制，相当于在y进制下计算 :code:`(a*x+b)*x+c`


加减法
======

先减法改写成加法 也就是 :code:`a-b = a+(-b)`

若两数符号相同，那么两个绝对值相加，最后补上符号就可以了。新的数组长度取两个数中大的再加一

若两数符号不同，那么取两数绝对值，以大减小，符号取绝对值大的。新的数组长度取绝对值大的


乘法
====

竖式乘法
--------

.. code::

             * * * *
     x       * * * *
     ----------------
             * * * *
           * * * *
         * * * *
       * * * *
     -----------------
       * * * * * * *

注意要从结果的最低位开始计算到最高位，不然会多算很多次加法


Toom-Cook算法
-------------

有 :code:`f(x) = a*(x**2)+b*x+c` 已知 f(0) f(1) f(2) ，求 a b c

.. math::

    \left[\begin{matrix}
    f(0) \\
    f(1) \\
    f(2)
    \end{matrix}\right] =
    \left[\begin{matrix}
    1 & 0 & 0 \\
    1 & 1 & 1 \\
    1 & 2 & 4
    \end{matrix}\right] \cdot
    \left[\begin{matrix}
    c \\
    b \\
    a
    \end{matrix}\right]

两边同时乘以逆矩阵得到

.. math::

    \left[\begin{matrix}
    1 & 0 & 0 \\
    1 & 1 & 1 \\
    1 & 2 & 4
    \end{matrix}\right]^{-1} \cdot
    \left[\begin{matrix}
    f(0) \\
    f(1) \\
    f(2)
    \end{matrix}\right] =
    \left[\begin{matrix}
    c \\
    b \\
    a
    \end{matrix}\right]


用竖式乘法，两个n位数相乘需要 :code:`n**2` 次乘法。因为结果只有 :code:`(2*n)-1` 位，所以写成多项式，分别求出 :code:`(2*n)-1` 个点后分别相乘再求出系数就可以了。

Karatsuba algorithm是Toom-Cook算法的一个例子，可以看作是用三次乘法完成两个2位数相乘。

Schonhage-Strassen算法
----------------------

用FFT的矩阵

因为复数精度问题，实现时应该使用有类似性质的Number theoretic transform，参考 http://www.apfloat.org/ntt.html

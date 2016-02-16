===
C++
===

const
=====

const加在类型前，和const加在变量名作用是不同的

:code:`const int *a` 表示不允许改变 :code:`*a` ， :code:`int *const a` 表示不允许改变 :code:`a`


placement new()
===============

各种container申请完内存后调用constructor。

.. code::

    void *p=malloc(sizeof(X));
    new (p) X(x);

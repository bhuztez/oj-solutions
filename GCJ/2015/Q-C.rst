========
Dijkstra
========

简述
====

= == == == ==
x  1  i  j  k
1  1  i  j  k
i  i -1  k -j
j  j -k -1  i
k  k  j -i -1
= == == == ==

i * j = k

j * i = -k

定义运算规则

一个字符串全由i j k组成，判断能否这个字符串分成3段，相乘分别为i j k

输入L X，L表示字符串长度，X表示重复次数

比如 3 2 ijk 表示 ijkijk

能输出YES，不能输出NO

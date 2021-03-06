from issue50 import module_test as tp
from numpy import zeros, ones, float32, abs, max

a = tp.Real_Array()
a.item = ones(6, dtype=float32)  # ones leads to a segfault 11 upon calling tp.testf(a); but zeros does not ... ?
print("This is sent to fortran : " + str(a.item))
tp.testf(a)
print("This is received by python : " + str(a.item))

assert abs(max(a.item - [1.0, 1.0, 1.0, 4.0, 1.0, 1.0])) < 1e-6
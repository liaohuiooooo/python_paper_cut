# https://www.cnblogs.com/lemonbit/p/7043879.html

import numpy as np

# np.arange
print("-------------------------------------------")
print(" np.arange ")
a = np.arange(100)
print(type(a))
print(a)

print("-------------------------------------------")

# 基于list或tuple
print("基于list或tuple")
tup = tuple(range(100))


arr = np.array(tup)

print(arr)
print("-------------------------------------------")
# Numpy的数值类型
print("Numpy的数值类型")
a = np.int8(12.222)
print(a)

b = np.float64(132)
print(b)

c = np.float64(True)
print(c)
print("-------------------------------------------")
# 数组的属性

print("数组的属性")
a = np.arange(4,dtype=float)
print(a)
## 表示复数类型
b =  np.arange(10, dtype='D')
print(b)

## ndim属性，数组的维度
a = np.array([[1,2],[3,4],[5,6]])
print(a.ndim)

# shape属性，数组对象的尺度，对于矩阵，即n行m列,shape是一个元组（tuple）
print(a.shape)
# size属性用来保存元素的数量，相当于shape中nXm的值
print(a.size)
# itemsize属性返回数组中各个元素所占用的字节数大小。
print(a.itemsize)

# nbytes属性，如果想知道整个数组所需的字节数量，可以使用nbytes属性。其值等于数组的size属性值乘以itemsize属性值
print(a.nbytes)

# T属性，数组转置
b = np.arange(4)
print(b)
c = b.reshape(2,2)
print(c,c.shape)

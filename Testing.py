import numpy as np

a=np.array([1,2,3])
print(a)

b=np.arange(6)
print(b)

c=np.arange(1,6)
print(c)

d=np.arange(1,8,3)
print(d)

e=np.linspace(0,0.5,20)
print(e)

f=np.zeros_like(a,dtype="float")
print(f)

g=np.arange(0.5,0.8,0.1)
print(g)

zeros=np.zeros(6,dtype="int")
print(zeros)
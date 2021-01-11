#!/usr/bin/env python
# coding=utf-8

import torch
import numpy as np

a = [i for i in range(10)]
b = np.array(a)
c = torch.tensor(a)
d = torch.tensor(b)
e = torch.from_numpy(b)

print(a)
print(b)
print(c)
print(d)
print(e)

b[0] = 100
print(b)
print(d)
print(e)

s = torch.zeros((3, 3))
t = torch.ones((3, 3))
w = torch.full((3, 3), 10)
print(s)
print(t)
print(w)

print(torch.eye(5))
# print(torch.normal(0, 1, 10))
print(torch.randn((3, 3)))
print(torch.rand((3, 3)))

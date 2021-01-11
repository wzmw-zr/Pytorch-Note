#!/usr/bin/env python
# coding=utf-8

import torch
# import numpy as np

a = torch.zeros((3, 3, 3))
b = torch.ones((3, 3, 3))

print("cancatenate operations")
print(a.shape)
print(b.shape)
c = torch.cat([a, b], dim=0)
d = torch.cat([a, b], dim=1)
e = torch.cat([a, b], dim=2)
print(c.shape)
print(d.shape)
print(e.shape)

f = torch.stack([a, b], dim=0)
print(f.shape)

print("split operations")

g = torch.zeros((2, 9))
list_of_tensors = torch.chunk(g, dim=1, chunks=3)
for tensors in list_of_tensors:
    print(tensors.shape)

split_tensors = torch.split(g, 4, dim=1)
for tensors in split_tensors:
    print(tensors.shape)

split_tensors_2 = torch.split(g, [1, 1, 7], dim=1)
for tensors in split_tensors_2:
    print(tensors.shape)

print("index operations")
print(a)
print(a[0])
print(a[0][0])
print(a[0][0][0])

h = torch.rand((3, 3, 3))
indices = torch.tensor([0, 2])
print(torch.index_select(h, 0, indices))


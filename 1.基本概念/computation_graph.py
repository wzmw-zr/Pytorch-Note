#!/usr/bin/env python
# coding=utf-8
import torch

a = torch.normal(0, 1, (1, ), requires_grad=True)
b = torch.rand((1, ), requires_grad=True)

c = torch.add(a, b)
c.retain_grad()
print(c.grad_fn)
d = c.mean()
d.retain_grad()
d.backward()
print(a.grad)
print(b.grad)
# print(d.grad)

print(a.is_leaf, b.is_leaf, c.is_leaf, d.is_leaf)
print(a.grad, b.grad, c.grad, d.grad)

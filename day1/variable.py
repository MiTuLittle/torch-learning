#!/usr/bin/env/python3
# -*- coding: utf-8 -*-
# author: hongtao.zhang
# date: 2020-03-12

import torch
from torch.autograd import Variable

tensor = torch.FloatTensor([[1, 2], [3, 4]])
variable = Variable(tensor, requires_grad=True)

print(tensor, 'tensor')
print(variable*variable)
t_out = torch.mean(tensor * tensor)
v_out = torch.mean(variable * variable)
print(t_out, 't_out')
print(v_out, 'v_out')

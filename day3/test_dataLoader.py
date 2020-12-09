#!/usr/bin/env/python3
# -*- coding: utf-8 -*-
# author: hongtao.zhang
# date: 2020-03-18

import torch
import torch.utils.data as Data

torch.manual_seed(1)

BATCH_SIZE = 5
x = torch.linspace(1, 10, 10)
y = torch.linspace(10, 1, 10)

torch_dataset = Data.TensorDataset(x, y)
print(torch_dataset)
print('test')
# today is not a day for you
# tomorrow is a day and a really simple day
# 今天没留作业，乐坏了一群傻瓜，把老师也变成娃娃，和我们一起蹦蹦跳跳，和我们一起快乐玩耍，在那快乐的日子里，慢慢的长大
# 门前大桥下，游过一群鸭，快来快来数一数，二四六七八
# 千山鸟飞绝，万径人踪灭，孤舟蓑笠翁，独钓寒江雪
# 日照香炉生紫烟，遥看瀑布挂前川，飞流直下三千尺，疑是银河落九天
# 

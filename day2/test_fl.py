#!/usr/bin/env/python3
# -*- coding: utf-8 -*-
# author: hongtao.zhang
# date: 2020-03-17

import torch
import matplotlib.pyplot as plt
import torch.nn.functional as F

n_data = torch.ones(100, 2)
x_0 = torch.normal(2 * n_data, 1)
y_0 = torch.zeros(100)
x_1 = torch.normal(-2 * n_data, 1)
y_1 = torch.ones(100)
x = torch.cat((x_0, x_1), 0).type(torch.FloatTensor)
y = torch.cat((y_0, y_1), ).type(torch.LongTensor)


class Net(torch.nn.Module):
    def __init__(self, n_feature, n_hidden, n_output):
        super(Net, self).__init__()
        # 定义每层用什么样的形式
        self.hidden = torch.nn.Linear(n_feature, n_hidden)  # 隐藏层线性输出
        self.predict = torch.nn.Linear(n_hidden, n_output)  # 输出层线性输出

    def forward(self, x_c):
        # 正向传播输入值，神经网络分析出输出层
        x_r = F.relu(self.hidden(x_c))  # 激励函数（隐藏层的线性值）
        x_e = self.predict(x_r)  # 输出值
        return x_e


net = Net(n_feature=2, n_hidden=10, n_output=2)

optimizer = torch.optim.SGD(net.parameters(), lr=0.02)
loss_func = torch.nn.CrossEntropyLoss()

plt.ion()
plt.show()

for i in range(100):
    out = net(x)
    loss = loss_func(out, y)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    if i % 2 == 0:
        plt.cla()
        prediction = torch.max(F.softmax(out, dim=1), 1)[1]
        pred_y = prediction.data.numpy().squeeze()
        target_y = y.data.numpy()
        plt.scatter(x.data.numpy()[:, 0], x.data.numpy()[:, 1], c=pred_y, s=100, lw=0, cmap='RdYlGn')
        accuracy = sum(pred_y == target_y) / 200
        plt.text(1.5, -4, 'Accuracy=%.2f' % accuracy, fontdict={'size': 20, 'color': 'red'})
        plt.pause(0.1)
plt.ioff()
plt.show()

#!/usr/bin/env/python3
# -*- coding: utf-8 -*-
# author: hongtao.zhang
# date: 2020-03-17

import torch
import matplotlib.pyplot as plt
import torch.nn.functional as F

x = torch.unsqueeze(torch.linspace(-1, 1, 100), dim=1)
y = x.pow(2) + 0.2 * torch.rand(x.size())


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


net = Net(n_feature=1, n_hidden=10, n_output=1)
print(net)
# optimizer = torch.optim.SGD(net.parameters(), lr=0.5)  # 训练工具，梯度下降
optimizer = torch.optim.Adam(net.parameters(), lr=0.2, betas=(0.9, 0.99))
loss_func = torch.nn.MSELoss()  # 损失函数
plt.ion()
plt.show()
for t in range(200):
    prediction = net(x)  # Net类继承自Module，Module类中定义类__call__方法，因此，net(x)经过__call__方法转到类forward方法
    loss = loss_func(prediction, y)  # 计算预测值和实际值之间的误差
    optimizer.zero_grad()  # 清空上一步的残余，更新参数值
    loss.backward()  # 误差反向传播，计算参数更新值
    optimizer.step()  # 将参数更新值施加到net的parameters
    if t % 5 == 0:
        plt.cla()
        plt.scatter(x.data.numpy(), y.data.numpy())
        plt.plot(x.data.numpy(), prediction.data.numpy(), 'r-', lw=1.5)
        plt.text(0.5, 0, 'Loss=%.4f' % loss.data.numpy(), fontdict={'size': 20, 'color': 'red'})
        plt.pause(0.1)

plt.ioff()
plt.show()

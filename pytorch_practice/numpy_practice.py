# numpy version
# import numpy as np
#
# N, D_in, H, D_out = 64, 1000, 100, 10
#
# x = np.random.randn(N, D_in)
# y = np.random.randn(N, D_out)
#
# w1 = np.random.randn(D_in, H)
# w2 = np.random.randn(H, D_out)
#
# learning_rate = 1e-6
# for t in range(500):
#     h = x.dot(w1)
#     h_relu = np.maximum(h, 0)
#     y_pred = h_relu.dot(w2)
#
#     loss = np.square(y_pred - y).sum()
#     print(t, loss)
#
#     grad_y_pred = 2.0 * (y_pred - y)
#     grad_w2 = h_relu.T.dot(grad_y_pred)
#     grad_h_relu = grad_y_pred.dot(w2.T)
#     grad_h = grad_h_relu.copy()
#     grad_h[h < 0] = 0
#     grad_w1 = x.T.dot(grad_h)
#
#     w1 -= learning_rate * grad_w1
#     w2 -= learning_rate * grad_w2

#-------------------------------------------------------------------------

#torch tensor version
# import torch
#
# dtype = torch.FloatTensor
#
# N, D_in, H, D_out = 64, 1000, 100, 10
#
# x = torch.randn(N, D_in).type(dtype)
# y = torch.randn(N, D_out).type(dtype)
#
# w1 = torch.randn(D_in, H).type(dtype)
# w2 = torch.randn(H, D_out).type(dtype)
#
# learning_rate = 1e-6
# for t in range(500):
#     h = x.mm(w1)
#     h_relu = h.clamp(min = 0)
#     y_pred = h_relu.mm(w2)
#
#     loss = (y_pred - y).pow(2).sum()
#     print(t, loss)
#
#     grad_y_pred = 2.0 * (y_pred - y)
#     grad_w2 = h_relu.t().mm(grad_y_pred)
#     grad_h_relu = grad_y_pred.mm(w2.t())
#     grad_h = grad_h_relu.clone()
#     grad_h[h < 0] = 0
#     grad_w1 = x.t().mm(grad_h)
#
#     w1 -= learning_rate * grad_w1
#     w2 -= learning_rate * grad_w2

#-------------------------------------------------------------------------

#pytorch Variables version
# import torch
# from torch.autograd import Variable
#
# class MyRelu(torch.autograd.Function):
#     def forward(self, input):
#         self.save_for_backward(input)
#         return input.clamp(min=0)
#
#     def backward(self, grad_output):
#         input, = self.saved_tensors
#         grad_input = grad_output.clone()
#         grad_input[input < 0] = 0
#         return grad_output
#
# dtype = torch.FloatTensor
#
# N, D_in, H, D_out = 64, 1000, 100, 10
#
# x = Variable(torch.randn(N, D_in).type(dtype), requires_grad=False)
# y = Variable(torch.randn(N, D_out).type(dtype), requires_grad=False)
#
# w1 = Variable(torch.randn(D_in, H).type(dtype), requires_grad=True)
# w2 = Variable(torch.randn(H, D_out).type(dtype), requires_grad=True)
#
# learning_rate = 1e-6
# for t in range(500):
#     relu = MyRelu()
#     y_pred = relu(x.mm(w1)).mm(w2)
#
#     loss = (y_pred - y).pow(2).sum()
#     print(t, loss.data[0])
#
#     loss.backward()
#
#     w1.data -= learning_rate * w1.grad.data
#     w2.data -= learning_rate * w2.grad.data
#
#     w1.grad.data.zero_()
#     w2.grad.data.zero_()

#-------------------------------------------------------------------------

#nn package
# import torch
# from torch.autograd import Variable
# N, D_in, H, D_out = 64, 1000, 100, 10
#
# x = Variable(torch.randn(N, D_in))
# y = Variable(torch.randn(N, D_out), requires_grad=False)
#
# model = torch.nn.Sequential(
#     torch.nn.Linear(D_in, H),
#     torch.nn.ReLU(),
#     torch.nn.Linear(H, D_out),
# )
#
# loss_fn = torch.nn.MSELoss(size_average=False)
#
# learning_rate = 1e-4
# for t in range(500):
#     y_pred = model(x)
#     loss = loss_fn(y_pred, y)
#     print(t, loss.data[0])
#     model.zero_grad()
#     loss.backward()
#     for param in model.parameters():
#         param.data -= learning_rate * param.grad.data

# -------------------------------------------------------------------------

#with optim package
# import torch
# from torch.autograd import Variable
# N, D_in, H, D_out = 64, 1000, 100, 10
#
# x = Variable(torch.randn(N, D_in))
# y = Variable(torch.randn(N, D_out), requires_grad=False)
#
# model = torch.nn.Sequential(
#     torch.nn.Linear(D_in, H),
#     torch.nn.ReLU(),
#     torch.nn.Linear(H, D_out),
# )
#
# loss_fn = torch.nn.MSELoss(size_average=False)
# learning_rate = 1e-4
# optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)
#
# for t in range(500):
#     y_pred = model(x)
#     loss = loss_fn(y_pred, y)
#     print(t, loss.data[0])
#     optimizer.zero_grad()
#     loss.backward()
#     optimizer.step()

# -------------------------------------------------------------------------

#custom nn modules
# import torch
# from torch.autograd import Variable
#
# class TwoLayerNet(torch.nn.Module):
#     def __init__(self, D_in, H, D_out):
#         super(TwoLayerNet, self).__init__()
#         self.linear1 = torch.nn.Linear(D_in, H)
#         self.linear2 = torch.nn.Linear(H, D_out)
#
#     def forward(self, x):
#         h_relu = self.linear1(x).clamp(min=0)
#         y_pred = self.linear2(h_relu)
#         return y_pred
#
# N, D_in, H, D_out = 64, 1000, 100, 10
#
# x = Variable(torch.randn(N, D_in))
# y = Variable(torch.randn(N, D_out), requires_grad=False)
#
# model = TwoLayerNet(D_in, H, D_out)
#
# criterion = torch.nn.MSELoss(size_average=False)
# optimizer = torch.optim.SGD(model.parameters(), lr=1e-4)
#
# for t in range(500):
#     y_pred = model(x)
#     loss = criterion(y_pred, y)
#     print(t, loss.data[0])
#     optimizer.zero_grad()
#     loss.backward()
#     optimizer.step()
# -------------------------------------------------------------------------

# custom nn modules
import random
import torch
from torch.autograd import Variable


class DynamicNet(torch.nn.Module):
    def __init__(self, D_in, H, D_out):
        super(DynamicNet, self).__init__()
        self.input_linear = torch.nn.Linear(D_in, H)
        self.middle_linear = torch.nn.Linear(H, H)
        self.out_linear = torch.nn.Linear(H, D_out)

    def forward(self, x):
        h_relu = self.input_linear(x).clamp(min=0)
        for _ in range(random.randint(0,3)):
            h_relu = self.middle_linear(h_relu).clamp(min=0)
        y_pred = self.out_linear(h_relu)
        return y_pred


N, D_in, H, D_out = 64, 1000, 100, 10

x = Variable(torch.randn(N, D_in))
y = Variable(torch.randn(N, D_out), requires_grad=False)

model = DynamicNet(D_in, H, D_out)

criterion = torch.nn.MSELoss(size_average=False)
optimizer = torch.optim.SGD(model.parameters(), lr=1e-4, momentum=0.9)

for t in range(500):
    y_pred = model(x)
    loss = criterion(y_pred, y)
    print(t, loss.data[0])
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
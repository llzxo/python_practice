import torch
from torch.autograd import Variable
import torch.nn as nn
import torch.nn.functional as F

class MNISTConvNet(nn.Module):
    def __init__(self):
        super(MNISTConvNet,self).__init__()
        self.conv1 = nn.Conv2d(1, 10, 5)
        self.pool1 = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(10, 20, 5)
        self.pool2 = nn.MaxPool2d(2, 2)
        self.fc1 = nn.Linear(320, 50)
        self.fc2 = nn.Linear(50, 10)

    def forward(self, input):
        x = self.pool1(F.relu(self.conv1(input)))
        x = self.pool2(F.relu(self.conv2(x)))
        x = x.view(x.size(0), -1)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        return x

net = MNISTConvNet()
print(net)

inputs = Variable(torch.randn(1, 1, 28, 28))
out = net(inputs)
print(out.size())

target = Variable(torch.LongTensor([3]))
loss_fn = nn.CrossEntropyLoss()
err = loss_fn(out, target)
err.backward()
print(err)

print(net.conv1.weight.data.norm())
print(net.conv1.weight.grad.data.norm())

import torch
from torch.autograd import Variable
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
import torch.nn.functional as F

train_loader = torch.utils.data.DataLoader(
    datasets.MNIST('./mnist', train=True, download=True, transform=transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.1307, ), (0.3081, ))
    ])), batch_size=64, shuffle=True
)

test_loader = torch.utils.data.DataLoader(
    datasets.MNIST('./mnist', train=False, transform=transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.1307, ), (0.3081, ))
    ])), batch_size=1000, shuffle=True,
)

class MNISTConvNet(nn.Module):
    def __init__(self):
        super(MNISTConvNet,self).__init__()
        self.conv1 = nn.Conv2d(1, 10, 5)
        self.pool1 = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(10, 20, 5)
        self.pool2 = nn.MaxPool2d(2, 2)
        self.conv2_drop = nn.Dropout2d()
        self.fc1 = nn.Linear(320, 50)
        self.fc2 = nn.Linear(50, 10)

    def forward(self, x):
        x = F.relu(self.pool1(self.conv1(x)))
        x = F.relu(self.pool2(self.conv2_drop(self.conv2(x))))
        x = x.view(x.size(0), -1)
        x = F.relu(self.fc1(x))
        x = F.dropout(x, training=self.training)
        x = F.relu(self.fc2(x))
        return F.log_softmax(x)

net1 = MNISTConvNet()
print(net1)
if torch.cuda.is_available():
    net = net1.cuda()

optimizer = optim.SGD(net1.parameters(), lr=0.01, momentum=0.9)

def train(epoch):
    net1.train()
    for batch_idx, (data, target) in enumerate(train_loader):
        if torch.cuda.is_available():
            data, target = data.cuda(), target.cuda()
        data, target = Variable(data), Variable(target)
        optimizer.zero_grad()
        output = net1(data)
        loss = F.nll_loss(output, target)
        loss.backward()
        optimizer.step()
        if batch_idx % 50 == 0:
            print('Train Epoch: {} [{}/{} ({:.0f}%)]\tLoss: {:.6f}'.format(
                epoch, batch_idx * len(data), len(train_loader.dataset),
                       100. * batch_idx / len(train_loader), loss.data[0]))

def test(net, epoch):
    net.eval()
    test_loss = 0
    correct = 0
    for data, target in test_loader:
        if torch.cuda.is_available():
            data, target = data.cuda(), target.cuda()
        data, target = Variable(data, volatile=True), Variable(target)
        output = net(data)
        test_loss += F.nll_loss(output, target).data[0]
        pred = output.data.max(1)[1]
        correct += pred.eq(target.data).cpu().sum()
    test_loss = test_loss
    test_loss /= len(test_loader)
    print('\nTest set: Average loss: {:.4f}, Accuracy: {}/{} ({:.0f}%)\n'.format(
        test_loss, correct, len(test_loader.dataset),
        100. * correct / len(test_loader.dataset)))

# for epoch in range(1,100):
#     train(epoch)
#     test(epoch)
#     torch.save(net, 'mnist.pkl')
def re_load():
    net2 = torch.load('mnist.pkl')
    return net2

net3 = re_load()
print(net3)

test(net1, 10)
test(net3, 10)
# inputs = Variable(torch.randn(1, 1, 28, 28))
# out = net(inputs)
# print(out.size())
#
# target = Variable(torch.LongTensor([3]))
# loss_fn = nn.CrossEntropyLoss()
# err = loss_fn(out, target)
# err.backward()
# print(err)
#
# print(net.conv1.weight.data.norm())
# print(net.conv1.weight.grad.data.norm())

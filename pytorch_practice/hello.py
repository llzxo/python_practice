import torch
import torchvision
import torchvision.transforms as transforms

from torch.autograd import Variable
import torch.nn as nn
import torch.nn.functional as F

import time
import torch.optim as optim

transform = transforms.Compose(
    [transforms.ToTensor(),transforms.Normalize((0.5,0.5,0.5),(0.5,0.5,0.5))]
)

trainset = torchvision.datasets.CIFAR10(root='./data', train=True, download=True, transform=transform)
trainloader = torch.utils.data.DataLoader(trainset, batch_size=4, shuffle=True, num_workers=2)

testset = torchvision.datasets.CIFAR10(root='./data', train=False, download=True, transform=transform)
testloader = torch.utils.data.DataLoader(testset, batch_size=4, shuffle=False, num_workers=2)

classes = ('plane', 'car', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'trunk')

class Net(nn.Module):
    def __init__(self):
        super(Net,self).__init__()
        self.conv1 = nn.Conv2d(3,10,5)
        self.pool = nn.MaxPool2d(2,2)
        self.conv2 = nn.Conv2d(10,16,5)
        self.fc1 = nn.Linear(16 * 5 * 5, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84,10)

    def forward(self,x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = x.view(-1, 16 * 5 * 5)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x
net = Net()
net = net.cuda()

criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(net.parameters(), lr=0.001, momentum=0.9)

start1 = time.clock()
start2 = time.time()

for epoch in range(2):
    running_loss = 0.0
    for i,data in enumerate(trainloader,0):
        inputs, labels = data

        # inputs,labels = Variable(inputs),Variable(labels)
        inputs,labels = Variable(inputs.cuda()),Variable(labels.cuda())
        optimizer.zero_grad()

        outputs = net(inputs)
        loss = criterion(outputs,labels)
        loss.backward()
        optimizer.step()

        running_loss += loss.data[0]
        if i%2000 ==1999:
            print('[%d,%5d] loss:%.3f' %(epoch + 1, i + 1, running_loss/2000 ))
            running_loss = 0.0
print('Finished Training')

imsize = 256
loader = transforms.Compose([transforms.Scale(imsize), transforms.ToTensor()])

def image_loader(image_name):
    image = Image.open(image_name)
    image = loader(image).float()
    image = Variable(image, requires_grad = True)

image = './plane.jpg'
out = net(Variable(image).cuda())
_,predicted = torch.max(out.data, 1)
print(classes[predicted[0]])
# correct = 0
# total = 0
# for data in testloader:
#     images, labels = data
#     labels = labels.cuda()
    # outputs = net(Variable(images))
    # outputs = net(Variable(images).cuda())
    # _, predicted = torch.max(outputs.data,1)
    # total += labels.size(0)
    # correct += (predicted == labels).sum()
#
# print('Accuracy is %d %%'%(100 * correct / total))
#
# class_correct = list(0. for i in range(10))
# class_total = list(0. for i in range(10))
# for data in testloader:
#     images, labels = data
#     labels = labels.cuda()
#     outputs = net(Variable(images))
    # outputs = net(Variable(images.cuda()))
    # _, predicted = torch.max(outputs.data, 1)
    # c = (predicted == labels).squeeze()
    # for i in range(4):
    #     label = labels[i]
    #     class_correct[label] += c[i]
    #     class_total[label] += 1
#
# for i in range(10):
#     print('accuracy of %s is %d %%' %(classes[i], 100 * class_correct[i] / class_total[i]))
#
# end1 = time.clock()
# end2 = time.time()
#
# print("cpu clock time duration:%s" % (end1 - start1))
# print("time duration:%s" % (end2 - start2))
# on cpu
# cpu clock time duration:694.808074
# time duration:133.895688057

# on gpu
# cpu clock time duration:48.632438
# time duration:54.9926979542
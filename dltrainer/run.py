from __future__ import print_function
from imp import reload
from PIL import Image

import os
import pdb

import numpy as np
import torch
import torch.nn as nn
import torch.cuda as cuda
import torchvision
import torchvision.transforms as transforms
import torchvision.models as models

USE_CUDA = torch.cuda.is_available()

transform_test = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.4914, 0.4822, 0.4465), (0.2023, 0.1994, 0.2010)),
])

classes = ('plane', 'car', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck')

net = models.resnet50(pretrained=True)
net.cuda() if USE_CUDA else None
net.eval()

output = net(input)
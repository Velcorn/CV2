import torch
import math
x = torch.Tensor([math.pi / 2.0])
x.requires_grad_(True)
y = torch.cos(x)
print(y)
y.backward()
print(x.grad)

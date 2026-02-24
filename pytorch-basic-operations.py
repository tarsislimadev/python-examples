import torch

x = torch.tensor([1.0, 2.0, 3.0])

y = torch.tensor([4.0, 5.0, 6.0])

print(x + y)

print(x * y)

print(torch.dot(x, y))

import torch

x = torch.randn(3, requires_grad=True)
y = x+2

print(x)
print(y)
print(y.grad_fn)

z = y*y*3
print(z)
z = z.mean()
print(z) 
#tracks all operations done on the tensor 
z.backward() #accumulates the gradient for x in x.grad
print(x.grad) #prints partial derivate wrt tensor ie dz/dx
#gradient claculations need to be cleared 
#can also use x.detach to let requires_grad be false
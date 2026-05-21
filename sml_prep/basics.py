import torch
import numpy as np
print(torch.__version__)

x = torch.rand(5,3)
print("random 5,3", x) # makes a tensor of random numbers w/5 rows and 3 cols

x = torch.zeros(2,4)
print("zeros 2,4", x) #makes a tensor of zeros w/2 rows and 4 cols

# requires_grad is off by default(grad=gradient)
# requires_grad is used for calculating gradient which is later used in optimization
# x = torch.tensor([5,3], requires_grad=True) #tensor has given value 5 and 3
# print(x) 

x = torch.ones(2,2)
y = torch.rand(2,2)

z = x+y #this is normal element addition
print(x)
print(y)
print(z)
# for inplace addition use y.add_(x) which changes the values tensor y by additing x to it

#slicing
print("all rows first col", z[:, 0])
print("all cols second row", z[1, :])
print("all cols row 1", z[1, 1]) #for the actualy iten just add .item() after the tensor location

#to convert tensor to numpy just declare it as z.numoy()
#when tensor is in cpu the the data is stored in the same memory eg in place addition changes the...
#valule of both the tensor and the numpy

a = np.ones(3)
b = torch.tensor(a)
a += 1
print(a)
print(b)
#if torch.tensor(z)[let z be numpy] is used for np to tensor then it creates the copy does not change it




#general form of linear reg
#f(x) = w * x + b ----- w is weight and b is bias

import torch
#eg: want to evaluate f(x) = 2*x and consider bias = 0
x = torch.tensor([1,2,3,4,5], dtype=torch.float32)
y = torch.tensor([2,4,6,8,10], dtype=torch.float32)
#need a tensor for weight initialised with zero and with requires_grad = True to track the gradient
w = torch.tensor(0.0, dtype=torch.float32, requires_grad=True)

#forward pass that just does the required function
def forward(x):
    return w * x #f(x) = w*x + b but b is 0 here

#loss function to evaluate loss bw predicted and actual value
def loss(y, y_predicted):
    return ((y_predicted-y)**2).mean() #mean square error

x_test = 5.0
print(f'Prediction before training: f({x_test}) = {forward(x_test):.3f}')

learning_rate = 0.01
n_iters = 100

for i in range(n_iters):
    y_pred = forward(x)
    l = loss(y, y_pred)
    l.backward() #this gives dl/dw ie the gradient of loss with respect to weight
    #now the gradient is stored in w.grad which is used to update the w value to get the desired value
    with torch.no_grad(): #to update the weight we need to turn off the gradient tracking
        w -= learning_rate * w.grad #update the weight using gradient descent
    w.grad.zero_() #we need to clear the gradient after each iteration so the next one does not have the values of prev one

print(f'Prediction after training: f({x_test}) = {forward(x_test):.3f}')


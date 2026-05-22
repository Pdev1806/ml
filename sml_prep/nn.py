import torch
import torch.nn as nn

# ==========================================
# 1. CREATE DATASET
# ==========================================

# y = 2x

X = torch.tensor(
    [[1], [2], [3], [4], [5]],
    dtype=torch.float32
)

Y = torch.tensor(
    [[2], [4], [6], [8], [10]],
    dtype=torch.float32
)

# shape = (samples, features)
n_samples, n_features = X.shape

print("samples:", n_samples)
print("features:", n_features)

# ==========================================
# 2. CREATE MODEL CLASS
# ==========================================

# Every PyTorch model usually inherits nn.Module

class LinearRegressionModel(nn.Module):

    # constructor
    def __init__(self, input_dim, output_dim):

        # initialize parent class
        super(LinearRegressionModel, self).__init__()

        # create linear layer
        # internally does:
        # y = wx + b

        self.linear = nn.Linear(
            input_dim,
            output_dim
        )

    # forward pass
    def forward(self, x):

        return self.linear(x)

# ==========================================
# 3. CREATE MODEL OBJECT
# ==========================================

model = LinearRegressionModel(
    input_dim=n_features,
    output_dim=1
)

# ==========================================
# 4. LOSS FUNCTION
# ==========================================

# Mean Squared Error
loss_fn = nn.MSELoss()

# ==========================================
# 5. OPTIMIZER
# ==========================================

optimizer = torch.optim.SGD(
    model.parameters(),
    lr=0.01
)

# ==========================================
# 6. BEFORE TRAINING
# ==========================================

x_test = torch.tensor([[5]], dtype=torch.float32)

prediction = model(x_test)

print("\nBefore training:")
print(prediction)

# ==========================================
# 7. TRAINING LOOP
# ==========================================

epochs = 1000

for epoch in range(epochs):

    # ------------------------------
    # FORWARD PASS
    # ------------------------------

    y_predicted = model(X)

    # ------------------------------
    # LOSS
    # ------------------------------

    loss = loss_fn(Y, y_predicted)

    # ------------------------------
    # BACKWARD PASS
    # ------------------------------

    optimizer.zero_grad()

    loss.backward()

    # ------------------------------
    # UPDATE WEIGHTS
    # ------------------------------

    optimizer.step()

    # ------------------------------
    # PRINT PROGRESS
    # ------------------------------

    if (epoch + 1) % 100 == 0:

        # get weight and bias
        [w, b] = model.parameters()

        print(
            f'epoch {epoch+1}: '
            f'weight = {w[0][0].item():.3f}, '
            f'bias = {b.item():.3f}, '
            f'loss = {loss.item():.8f}'
        )

# ==========================================
# 8. AFTER TRAINING
# ==========================================

print("\nAfter training:")

prediction = model(x_test)

print(prediction)

# ==========================================
# 9. INSPECT PARAMETERS
# ==========================================

print("\nModel parameters:")

for param in model.parameters():
    print(param)
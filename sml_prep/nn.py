import torch
import torch.nn as nn
import torchvision
import torchvision.transforms as transforms

# ==========================================
# 1. DEVICE CONFIGURATION
# ==========================================

# use GPU if available else CPU

device = torch.device(
    'cuda' if torch.cuda.is_available() else 'cpu'
)

print(device)

# ==========================================
# 2. HYPERPARAMETERS
# ==========================================

input_size = 784      # 28x28 image = 784 pixels
hidden_size = 500
num_classes = 10      # digits 0-9

num_epochs = 5
batch_size = 100
learning_rate = 0.001

# ==========================================
# 3. LOAD DATASET
# ==========================================

train_dataset = torchvision.datasets.MNIST(
    root='./data',
    train=True,
    transform=transforms.ToTensor(),
    download=True
)

test_dataset = torchvision.datasets.MNIST(
    root='./data',
    train=False,
    transform=transforms.ToTensor()
)

# ==========================================
# 4. DATALOADERS
# ==========================================

train_loader = torch.utils.data.DataLoader(
    dataset=train_dataset,
    batch_size=batch_size,
    shuffle=True
)

test_loader = torch.utils.data.DataLoader(
    dataset=test_dataset,
    batch_size=batch_size,
    shuffle=False
)

# ==========================================
# 5. CREATE NEURAL NETWORK
# ==========================================

class NeuralNet(nn.Module):

    def __init__(self, input_size, hidden_size, num_classes):

        super(NeuralNet, self).__init__()

        # hidden layer
        self.linear1 = nn.Linear(
            input_size,
            hidden_size
        )

        # activation
        self.relu = nn.ReLU()

        # output layer
        self.linear2 = nn.Linear(
            hidden_size,
            num_classes
        )

    def forward(self, x):

        # flatten image
        x = x.reshape(-1, 28 * 28)

        out = self.linear1(x)

        out = self.relu(out)

        out = self.linear2(out)

        return out

# ==========================================
# 6. INITIALIZE MODEL
# ==========================================

model = NeuralNet(
    input_size,
    hidden_size,
    num_classes
).to(device)

# ==========================================
# 7. LOSS + OPTIMIZER
# ==========================================

criterion = nn.CrossEntropyLoss()

optimizer = torch.optim.Adam(
    model.parameters(),
    lr=learning_rate
)

# ==========================================
# 8. TRAINING LOOP
# ==========================================

total_steps = len(train_loader)

for epoch in range(num_epochs):

    for i, (images, labels) in enumerate(train_loader):

        # move tensors to device
        images = images.to(device)
        labels = labels.to(device)

        # -------------------------
        # FORWARD PASS
        # -------------------------

        outputs = model(images)

        loss = criterion(outputs, labels)

        # -------------------------
        # BACKWARD PASS
        # -------------------------

        optimizer.zero_grad()

        loss.backward()

        optimizer.step()

        # -------------------------
        # PRINT
        # -------------------------

        if (i + 1) % 100 == 0:

            print(
                f'Epoch [{epoch+1}/{num_epochs}], '
                f'Step [{i+1}/{total_steps}], '
                f'Loss: {loss.item():.4f}'
            )

# ==========================================
# 9. TEST MODEL
# ==========================================

with torch.no_grad():

    correct = 0
    total = 0

    for images, labels in test_loader:

        images = images.to(device)
        labels = labels.to(device)

        outputs = model(images)

        _, predicted = torch.max(outputs, 1)

        total += labels.size(0)

        correct += (predicted == labels).sum().item()

    print(
        f'Accuracy: {100 * correct / total:.2f}%'
    )
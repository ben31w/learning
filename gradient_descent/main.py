"""
Demonstration of different gradient descent techniques applied to the same model and dataset.

Gradient descent is an optimization algorithm: it enables ML models to find the optimal parameters (weights, bias).
It involves iteratively updating weights and biases to find the combination that minimizes loss.

https://mypinguai.com/gradient-descent/
"""
import torch
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt
import numpy as np

#################
# HYPERPARAMETERS
#################

# One epoch is reached when a model processes all the training examples once.
# More epochs -> Model trains longer and is more accurate.
EPOCHS = 200


# Set random seeds for reproducibility
torch.manual_seed(42)
np.random.seed(42)

# Generate synthetic data (regression): y = x^3 + noise
# We will train models to fit this data.
N = 200
x = np.linspace(-1, 1, N).reshape(-1, 1)
y = x**3 + 0.1 * np.random.randn(N, 1)
plt.figure(figsize=(8, 6))
plt.scatter(x, y, color='purple')

# Convert numpy arrays to torch tensors
x_tensor = torch.tensor(x, dtype=torch.float32)
y_tensor = torch.tensor(y, dtype=torch.float32)

# Define a simple feedforward neural network model
def get_model():
    model = nn.Sequential(
        nn.Linear(1, 10),
        nn.ReLU(),
        nn.Linear(10, 1)
    )
    return model

# Training function: runs the training loop and records loss history
def train_model(model, optimizer, x, y, epochs, opt_name):
    criterion = nn.MSELoss()
    loss_history = []
    for epoch in range(epochs):
        optimizer.zero_grad()
        outputs = model(x)
        loss = criterion(outputs, y)
        loss.backward()
        optimizer.step()
        loss_history.append(loss.item())

    # Only for plotting purposes: convert the model output (torch tensor weights) to a numpy array
    model_y_tensor = x ** 3 + 0.1 * outputs
    model_y = model_y_tensor.detach().numpy()
    plt.plot(x, model_y, label=opt_name)

    return loss_history

# Prepare a dictionary of optimizers to compare
optimizer_configs = {
    "SGD": lambda model: optim.SGD(model.parameters(), lr=0.01),
    "SGD_momentum": lambda model: optim.SGD(model.parameters(), lr=0.01, momentum=0.9),
    "RMSprop": lambda model: optim.RMSprop(model.parameters(), lr=0.01),
    "Adam": lambda model: optim.Adam(model.parameters(), lr=0.01)
}

# Save an initial state dict so that all models start from the same weights
base_model = get_model()
initial_state = base_model.state_dict()

# Dictionary to store the loss history for each optimizer
results = {}

# Train a new model with each optimizer using the same initialization
for opt_name, opt_func in optimizer_configs.items():
    model = get_model()
    model.load_state_dict(initial_state)  # Ensure identical starting weights
    optimizer = opt_func(model)
    loss_history = train_model(model, optimizer, x_tensor, y_tensor, epochs=EPOCHS, opt_name=opt_name)
    results[opt_name] = loss_history

# Finishing touches on the model output figure
plt.title("Training the same model with different optimization algorithms")
plt.legend()

# Plot the loss curves for each optimizer on a new figure
plt.figure(figsize=(8, 6))
for opt_name, loss_history in results.items():
    plt.plot(loss_history, label=opt_name)
plt.xlabel('Epoch')
plt.ylabel('Mean Squared Error (MSE) Loss')
plt.title('Comparison of Optimization Algorithms')
plt.legend()
plt.grid(True)
plt.show()
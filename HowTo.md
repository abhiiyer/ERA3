# How to Run the MNIST CNN Project

## Prerequisites

- Python 3.x
- PyTorch
- torchvision
- matplotlib
- numpy

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/abhiiyer/ERA3.git
   cd ERA3
   ```

2. Install the required packages:
   ```bash
   pip install torch torchvision matplotlib numpy
   ```

## Training the Model

1. Run the training script:
   ```bash
   python train.py
   ```

   This will train the model and save the loss curve as `static/loss_curve.png`.

## Viewing Training Logs

1. Start the server:
   ```bash
   python server.py
   ```

2. Open your web browser and go to `http://localhost:8000` to view the training logs and loss curve.

## Displaying Model Results

1. Run the utility script to show model predictions on random images:
   ```bash
   python utils.py
   ```

   This will display the model's predictions on 10 random images from the MNIST test set. 
import torch
import torchvision
import torchvision.transforms as transforms
import matplotlib.pyplot as plt
import numpy as np
from model import SimpleCNN

def show_random_results():
    transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5,), (0.5,))])
    testset = torchvision.datasets.MNIST(root='./data', train=False, download=True, transform=transform)
    testloader = torch.utils.data.DataLoader(testset, batch_size=10, shuffle=True)

    dataiter = iter(testloader)
    images, labels = dataiter.next()

    model = SimpleCNN()
    model.load_state_dict(torch.load('mnist_cnn.pth'))
    model.eval()

    outputs = model(images)
    _, predicted = torch.max(outputs, 1)

    fig, axes = plt.subplots(1, 10, figsize=(12, 2))
    for i in range(10):
        ax = axes[i]
        ax.imshow(images[i].numpy().squeeze(), cmap='gray')
        ax.set_title(f'Pred: {predicted[i].item()}')
        ax.axis('off')
    plt.show()

if __name__ == '__main__':
    show_random_results() 
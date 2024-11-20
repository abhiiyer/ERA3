# **Session-5: MNIST Project**

This project is a lightweight convolutional neural network (CNN) built to classify handwritten digits from the MNIST dataset. The model is optimized to have **less than 25,000 parameters** and achieves **95% training accuracy in 1 epoch**.

---

## **Project Overview**

- **Objective**: Build a CNN with:
  - Fewer than 25,000 parameters.
  - At least 95% training accuracy in one epoch.
- **Technologies Used**: Python, PyTorch, GitHub Actions for CI/CD.
- **GitHub Actions Integration**:
  - Validates that the model has fewer than 25,000 parameters.
  - Verifies that training accuracy is at least 95%.

---

## **Model Parameters Calculation**

The model architecture is defined in [`model.py`](./model.py). Below is a breakdown of the parameter count:

| **Layer**            | **Details**                          | **Parameters** |
|----------------------|--------------------------------------|----------------|
| Convolutional Layer 1 | Input Channels: 1, Output Channels: 8, Kernel: 3x3 | (1 × 3 × 3 + 1) × 8 = 80 |
| Convolutional Layer 2 | Input Channels: 8, Output Channels: 16, Kernel: 3x3 | (8 × 3 × 3 + 1) × 16 = 1,168 |
| Convolutional Layer 3 | Input Channels: 16, Output Channels: 16, Kernel: 3x3 | (16 × 3 × 3 + 1) × 16 = 2,320 |
| Fully Connected Layer 1 | Input Features: 144, Output Features: 64 | 144 × 64 + 64 = 9,280 |
| Fully Connected Layer 2 | Input Features: 64, Output Features: 10 | 64 × 10 + 10 = 650 |

**Total Parameters**: **7,098**

---

## **Project Structure**



---

## **GitHub Actions Results**

GitHub Actions automates the following tests:
1. **Parameter Count Check**: Ensures the model has fewer than 25,000 parameters.
2. **Training Accuracy Check**: Validates that the model achieves at least 95% training accuracy in 1 epoch.

Below is a screenshot of the successful test execution:

![GitHub Actions Success Screenshot](./github_actions_success.png)

---

## **How to Run the Project**

### Prerequisites
- Python 3.8 or later
- Libraries: PyTorch, torchvision

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/abhiiyer/ERA3.git
   cd ERA3/Session-5

2. Install dependencies:
   ```bash
pip install torch torchvision

3. Run the tests:
   ```bash
python test_model1.py
   ```
GitHub Actions Workflow
The workflow file, ml-pipeline.yml, automates:

Setting up the Python environment.
Installing dependencies.
Running test_model.py.
Key Workflow Output
The workflow verifies:

Parameter count test passed: Model parameter count test passed: 7098 parameters.
Training accuracy test passed: Training accuracy test passed: 95.02%.
Future Enhancements
Add model evaluation on the MNIST test dataset.
Deploy the model using a lightweight API (e.g., FastAPI).
Extend GitHub Actions to include test dataset accuracy validation.


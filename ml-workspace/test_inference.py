
import numpy as np

from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Load the same dataset
digits = load_digits()
X = digits.data
y = digits.target

# Recreate the same train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Train the same model
model = LogisticRegression(max_iter=2000, solver="lbfgs")
model.fit(X_train, y_train)

# Select one test sample
sample = X_test[0]

# Python prediction
prediction = model.predict([sample])[0]

# Export input for C program
np.savetxt("test_input.txt", sample, fmt="%.9f")

print("Actual digit:", y_test[0])
print("Python prediction:", prediction)
print("Test input exported.")

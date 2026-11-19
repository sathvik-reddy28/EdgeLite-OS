
import numpy as np

from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# 1. Load handwritten digit dataset
digits = load_digits()

X = digits.data
y = digits.target

print("Dataset shape:", X.shape)
print("Target shape:", y.shape)

# 2. Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# 3. Create Logistic Regression model
model = LogisticRegression(
    max_iter=2000,
    solver="lbfgs"
)

# 4. Train the model
model.fit(X_train, y_train)

# 5. Make predictions
y_pred = model.predict(X_test)

# 6. Evaluate model
accuracy = accuracy_score(y_test, y_pred)

print("\nTraining samples:", len(X_train))
print("Testing samples:", len(X_test))
print("Model accuracy:", accuracy * 100, "%")

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# 7. Save model parameters
np.savez(
    "digit_model.npz",
    weights=model.coef_,
    bias=model.intercept_
)

print("\nModel parameters exported successfully.")

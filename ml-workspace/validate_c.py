
import numpy as np
import subprocess
import re

from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Load dataset
digits = load_digits()
X = digits.data
y = digits.target

# Use the same train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Train Python model
model = LogisticRegression(max_iter=2000, solver="lbfgs")
model.fit(X_train, y_train)

python_predictions = model.predict(X_test)

# Run C inference for every test sample
c_predictions = []

for sample in X_test:
    input_data = " ".join(map(str, sample))

    result = subprocess.run(
        ["./digit_inference"],
        input=input_data,
        text=True,
        capture_output=True,
        check=True
    )

    match = re.search(r"Predicted digit:\s*(\d+)", result.stdout)

    if not match:
        raise RuntimeError("Could not read C prediction: " + result.stdout)

    c_predictions.append(int(match.group(1)))

c_predictions = np.array(c_predictions)

# Compare results
matches = np.sum(python_predictions == c_predictions)
total = len(y_test)

print("\n========== C INFERENCE VALIDATION ==========")
print("Total test samples:", total)
print("Matching predictions:", matches)
print("Mismatching predictions:", total - matches)

print("\nPython accuracy:", accuracy_score(y_test, python_predictions) * 100)
print("C accuracy:", accuracy_score(y_test, c_predictions) * 100)

print("\nC vs Python prediction agreement:",
      accuracy_score(python_predictions, c_predictions) * 100, "%")

print("\nC Confusion Matrix:")
print(confusion_matrix(y_test, c_predictions))

print("\nC Classification Report:")
print(classification_report(y_test, c_predictions))

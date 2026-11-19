
import numpy as np

# Load trained model parameters
data = np.load("digit_model.npz")

weights = data["weights"]
bias = data["bias"]

# Export weights
with open("model_weights.h", "w") as f:
    f.write("#ifndef MODEL_WEIGHTS_H\n")
    f.write("#define MODEL_WEIGHTS_H\n\n")
    f.write("static const float weights[10][64] = {\n")

    for row in weights:
        f.write("    {")
        f.write(", ".join(f"{x:.9f}f" for x in row))
        f.write("},\n")

    f.write("};\n\n")
    f.write("#endif\n")

# Export biases
with open("model_bias.h", "w") as f:
    f.write("#ifndef MODEL_BIAS_H\n")
    f.write("#define MODEL_BIAS_H\n\n")
    f.write("static const float bias[10] = {\n")
    f.write(", ".join(f"{x:.9f}f" for x in bias))
    f.write("\n};\n\n")
    f.write("#endif\n")

print("Model parameters exported to C header files.")

# EdgeLite OS
## Lightweight Linux Distribution for ML Inference

## 1. Project Overview

EdgeLite OS is a lightweight Linux distribution designed for
machine learning inference in resource-constrained environments.

It uses Buildroot to generate a customized Linux system for
QEMU x86-64. The system integrates a handwritten digit recognition
application using a Logistic Regression model implemented in C.

## 2. Technologies Used

- Buildroot 2026.08.1
- Linux Kernel 6.18.7
- QEMU x86-64
- BusyBox
- SquashFS
- OverlayFS
- C and Python
- scikit-learn

## 3. Machine Learning Application

- Dataset: scikit-learn Digits dataset
- Samples: 1,797
- Input: 8x8 grayscale images
- Features: 64
- Classes: 10 (digits 0-9)
- Model: Logistic Regression
- Test accuracy: 95.83%

The trained model parameters are exported and used by a
standalone C inference application.

Python and C predictions matched on all 360 test samples.

## 4. System and Security Features

- Read-only SquashFS root filesystem
- Writable OverlayFS mount for /etc
- Temporary runtime filesystems using tmpfs
- Kernel pointer restriction enabled
- Kernel log access restriction enabled
- Address Space Layout Randomization enabled

## 5. Performance Results

- Kernel image: approximately 6.0 MB
- SquashFS root filesystem: approximately 2.8 MB
- EXT2 root filesystem: approximately 20 MB
- Original Buildroot EXT2 baseline: approximately 60 MB
- EXT2 reduction against original baseline: 66.67%
- QEMU RAM: approximately 110 MB
- Average inference latency: approximately 5.347 microseconds
- Python/C prediction agreement: 360/360

The 66.67% reduction is measured against the original
Buildroot EXT2 image, not a mainstream Linux distribution.

Inference timing was measured in QEMU and is not a
real-hardware performance measurement.

## 6. Build and Execution

Target platform: QEMU x86-64.

Refer to BUILD-INSTRUCTIONS.txt for build and execution instructions.

The generated system can be launched using the supplied
QEMU launcher.

## 7. Device Tree

A separate custom device tree was not required for the
QEMU x86-64 PC target.

## 8. Repository Structure

- images/: Kernel, root filesystem and QEMU launcher
- configs/: Buildroot and kernel configurations
- manifests/: Package and licence information
- benchmarks/: Performance and validation results
- scripts/: Build scripts
- source/: Custom package and root filesystem overlay

## 9. Licensing

The digit-inference application is licensed under MIT.
Third-party package licences are documented in
manifests/manifest.csv and manifests/licenses/.

## 10. Limitations

The system was tested using QEMU x86-64 rather than
physical edge hardware. Performance may differ on real devices.

GPU acceleration was outside the scope of this CPU-only implementation.

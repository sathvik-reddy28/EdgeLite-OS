#!/bin/bash
set -e

PROJECT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
BUILDROOT_DIR="$PROJECT_DIR/buildroot-2026.08.1"
CONFIG_FILE="$PROJECT_DIR/configs/edgelite_defconfig"

echo "=================================="
echo "       Building EdgeLite OS"
echo "=================================="

# Remove whitespace-containing PATH entries that Buildroot rejects
export PATH="$(printf '%s' "$PATH" | tr ':' '\n' | grep -Ev '[[:space:]]' | paste -sd ':' -)"

cd "$BUILDROOT_DIR"

# Load the saved EdgeLite configuration
make BR2_DEFCONFIG="$CONFIG_FILE" defconfig

# Build kernel, root filesystem and application
make -j"$(nproc)"

echo ""
echo "=================================="
echo "       Build Completed"
echo "=================================="
echo "Generated images:"
ls -lh output/images/bzImage
ls -lh output/images/rootfs.squashfs
ls -lh output/images/rootfs.ext2

# Ensure the QEMU launcher boots the SquashFS image
if [ -f output/images/start-qemu.sh ]; then
    sed -i 's/rootfs\.ext2/rootfs.squashfs/g' output/images/start-qemu.sh
    sed -i 's/root=\/dev\/vda /root=\/dev\/vda rootfstype=squashfs ro /' output/images/start-qemu.sh
    echo "QEMU launcher configured for SquashFS."
fi

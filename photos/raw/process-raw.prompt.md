---
description: 'Process new photos from photos/raw: convert HEICs to PNG, rename uniformly to photo-XX.png, and move to photos/'
agent: 'agent'
tools: [run_in_terminal]
---

Process all new photos sitting in the `photos/raw/` directory of this workspace.

Steps to follow:

1. List all files in `photos/raw/` (skip `.DS_Store`).
2. Find the current highest `photo-XX.png` number already in `photos/`.
3. For each file in `photos/raw/` (sorted alphabetically):
   - If it is a `.heic` or `.HEIC` file, convert it to PNG using `sips -s format png <src> --out <dst>`.
   - Rename it to `photo-XX.png` where XX continues sequentially from the current max, zero-padded to 2 digits.
   - Move the final `.png` into `photos/`.
   - Delete the original raw file after a successful move.
4. Print a summary of every file renamed and moved.
5. Print the new total photo count in `photos/`.

Do all of this in a single Python script run via the terminal. Use `sips` for HEIC conversion (built into macOS). Do not leave any originals behind in `photos/raw/` after successful processing.

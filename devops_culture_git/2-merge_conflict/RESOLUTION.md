# Merge Conflict Resolution

## Conflicting line
The line in conflict concerned the ‘Version’ lines (version: 1.1.0 – version: 2.0.0).

## Why this line and not the others
Both branches had modified the same line since the common ancestor, whereas ‘replicas’ and ‘feature_dark_mode’ had only been modified on a single branch each, so Git was able to merge them automatically.

## Resolution
Version: 2.0.0, as requested in the instructions, whilst also retaining the values that had already been automatically merged: replicas: 4 and feature_dark_mode: true.
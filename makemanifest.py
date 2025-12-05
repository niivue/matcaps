#!/usr/bin/env python3
import os
import sys
import json

def main():
    if len(sys.argv) != 2:
        print("Usage: python makemanifest.py /path/to/jsons")
        sys.exit(1)

    folder = sys.argv[1]

    if not os.path.isdir(folder):
        print(f"Error: '{folder}' is not a directory.")
        sys.exit(1)

    manifest_path = os.path.join(folder, "manifest.json")

    # List *.json files (excluding manifest.json) and strip extension
    files = [
        os.path.splitext(f)[0]
        for f in os.listdir(folder)
        if f.endswith(".json") and f != "manifest.json"
    ]

    # Sort alphabetically
    files.sort()

    # Write manifest
    with open(manifest_path, "w") as f:
        json.dump(files, f, indent=2)

    print(f"Wrote {manifest_path} with {len(files)} entries.")

if __name__ == "__main__":
    main()

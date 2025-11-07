import os

# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Create the 'examples' subfolder inside the script's directory
examples_dir = os.path.join(script_dir, "examples")
os.makedirs(examples_dir, exist_ok=True)

# Create 70 files: example_1.py to example_70.py
for i in range(1, 71):
    filename = f"example_{i}.py"
    filepath = os.path.join(examples_dir, filename)

    if not os.path.exists(filepath):
        with open(filepath, "w") as f:
            f.write(f"# This is example file number {i}\n")
        print(f"Created: {filename}")
    else:
        print(f"Skipped (already exists): {filename}")

print("Done.")

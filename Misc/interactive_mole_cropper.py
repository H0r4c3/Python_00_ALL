import cv2
import os
from tkinter import Tk, filedialog

# --- Step 1: Select a folder ---
Tk().withdraw()  # hide the main Tk window
folder = filedialog.askdirectory(title="Select Folder Containing Images")

if not folder:
    print("❌ No folder selected. Exiting.")
    exit()

# --- Step 2: Select an image file from the chosen folder ---
filetypes = [("Image files", "*.jpg *.jpeg *.png *.tiff *.bmp")]
Tk().withdraw()
image_path = filedialog.askopenfilename(initialdir=folder, title="Select an image", filetypes=filetypes)

if not image_path:
    print("❌ No image selected. Exiting.")
    exit()

# --- Step 3: Load and crop interactively ---
img = cv2.imread(image_path)
clone = img.copy()
cv2.namedWindow("Select Mole", cv2.WINDOW_NORMAL)
r = cv2.selectROI("Select Mole", img, showCrosshair=True, fromCenter=False)
cv2.destroyWindow("Select Mole")

x, y, w, h = [int(v) for v in r]

# Add a margin around the mole (adjust if needed)
margin = 100
x1 = max(0, x - margin)
y1 = max(0, y - margin)
x2 = min(img.shape[1], x + w + margin)
y2 = min(img.shape[0], y + h + margin)

# Crop and save as PNG near the original file
crop = clone[y1:y2, x1:x2]
base_name = os.path.splitext(os.path.basename(image_path))[0]
output_path = os.path.join(os.path.dirname(image_path), f"{base_name}_cropped.png")

cv2.imwrite(output_path, crop, [cv2.IMWRITE_PNG_COMPRESSION, 0])

print(f"✅ Mole cropped and saved as:\n{output_path}")

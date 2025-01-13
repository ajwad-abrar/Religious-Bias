import os

# Path to the folder containing the images
biased_folder = r"E:\Teaching\Research\Religious Bias\Religious-Bias\images\biased"

# Rename images in the folder
for i, filename in enumerate(os.listdir(biased_folder), start=1):
    old_path = os.path.join(biased_folder, filename)
    
    # Ensure the file is a .png image
    if filename.lower().endswith('.png'):
        # Create the new filename
        new_name = f"img_{i}.png"
        new_path = os.path.join(biased_folder, new_name)
        
        # Rename the file
        os.rename(old_path, new_path)

print(f"Renamed {i} images successfully!")

import os
import random
from PIL import Image, ImageOps


def concat_images(image_paths, size, shape=None):
    # Open images and resize them
    width, height = size
    images = map(Image.open, image_paths)
    images = [ImageOps.fit(image, size, Image.ANTIALIAS) 
              for image in images]
    
    # Create canvas for the final image with total size
    shape = shape if shape else (1, len(images))
    image_size = (width * shape[1], height * shape[0])
    image = Image.new('RGB', image_size)
    
    # Paste images into final image
    for row in range(shape[0]):
        for col in range(shape[1]):
            offset = width * col, height * row
            idx = row * shape[1] + col
            image.paste(images[idx], offset)
    
    return image

# Get list of image paths
folder = 'images'
image_paths = [os.path.join(folder, f) 
               for f in os.listdir(folder) if f.endswith('.jpg')]

image_paths.sort()

# Random selection of images
image_array = random.choices(image_paths, k=9)

# Create and save image grid
image = concat_images(image_paths, (300, 300), (3, 3))
image.save('image.jpg', 'JPEG')
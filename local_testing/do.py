import logging
import shlex
import subprocess
import sys
import platform
import shutil
import google.colab
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from collections import namedtuple
from matplotlib.patches import Rectangle
from matplotlib.collections import PatchCollection


# Define file paths
IMAGE_NAME = "input4.jpeg"
img_path    = Path(f"{IMAGE_NAME}")
bin_path    = "candidate_crops"
model_path  = "fastgaze.vxm"
img_path 	= Path("input.jpeg")

print("\n")
print(f"Image is at: {str(img_path.absolute())}")
print(f"Model is at: {str(model_path)}")
print("\n")


# Show crop part for different aspect ratios
from crop_api import ImageSaliencyModel, is_symmetric, parse_output, reservoir_sampling
model = ImageSaliencyModel(crop_binary_path=bin_path, crop_model_path=model_path)
saliencyData = model.plot_img_crops(img_path)
print(saliencyData)

# Crop images for different aspect ratios, with saliency coordinate as centre point
from fractions import Fraction
from utils import cropImage
#shutil.rmtree('/content/photos')
! mkdir photos
absoluteImagePath = str(img_path.absolute())
aspectRatios = [0.3125, 0.625, 1.0, 1.14, 2]
salientCoordinates = saliencyData['top10_average_coordinates']
print("Aspect Ratios are:")
for ratio in aspectRatios:
  fraction = Fraction(ratio).limit_denominator(10)
  height = fraction.numerator
  width = fraction.denominator
  print(f"Aspect Width: {width} Height: {height}")
  cropImage(absoluteImagePath, (width, height), salientCoordinates, f"photos/{ratio}")










  
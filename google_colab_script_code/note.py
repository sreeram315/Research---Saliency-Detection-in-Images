import logging
import shlex
import subprocess
import sys
from collections import namedtuple
from pathlib import Path
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.collections import PatchCollection
from matplotlib.patches import Rectangle
import platform
import google.colab

logging.basicConfig(level=logging.ERROR)
! pip install pandas scikit-learn scikit-image statsmodels requests dash
! [[ -d final-project-image-crop ]] || git clone https://github.com/sreeram315/final-project-image-crop
sys.path.append("final-project-image-crop/src")

bin_dir     = Path("final-project-image-crop/bin")
bin_path    = "final-project-image-crop/bin/candidate_crops"
model_path  = "final-project-image-crop/bin/fastgaze.vxm"
data_dir    = Path("final-project-image-crop/data")
data_dir.exists()

img_path    = Path("/content/final-project-image-crop/data/input.jpeg")
img         = mpimg.imread(img_path)
img         = mpimg.imread(img_path)

plt.imshow(img)
plt.gca().add_patch(Rectangle((0, 0), 200, 112, linewidth=1, edgecolor="r", facecolor="none"))

print(f"Image is at: {str(img_path.absolute())}")
print(f"Model is at: {str(model_path)}")

command = f"{str(bin_path)} {str(model_path)} '{img_path.absolute()}' show_all_points"
output = subprocess.check_output(command, shell=True)
print(output.splitlines())

from crop_api import ImageSaliencyModel, is_symmetric, parse_output, reservoir_sampling
model = ImageSaliencyModel(crop_binary_path=bin_path, crop_model_path=model_path)
print(img_path)
model.plot_img_crops(img_path)


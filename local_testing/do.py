from pathlib import Path

bin_path    = "candidate_crops"
model_path  = "fastgaze.vxm"
img_path 	= Path("input.jpeg")

# Show crop part for different aspect ratios
from crop_api import ImageSaliencyModel, is_symmetric, parse_output, reservoir_sampling
model = ImageSaliencyModel(crop_binary_path=bin_path, crop_model_path=model_path)
saliencyData = model.plot_img_crops(img_path)




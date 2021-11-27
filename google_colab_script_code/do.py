# delete
import shutil
shutil.rmtree('/content/final-project-image-crop')
! git clone https://github.com/sreeram315/final-project-image-crop

# download
! zip -r photos.zip photos
from google.colab import files
files.download("photos.zip")
def cropImage(imagePath, aspectRatio, salientCoordinates, outputFileName = "output"):
	from PIL import Image
	originalImage = Image.open(imagePath)
	width, height = originalImage.size
	print(width, height)
	finalWidth = (0.75 * width)
	left = max(0, salientCoordinates[0] - (finalWidth/2))
	right = left + finalWidth

	finalHeight = (aspectRatio[1]*finalWidth)/aspectRatio[0]
	top = max(0, salientCoordinates[1] - (finalHeight/2))
	bottom = min(top + finalHeight, height)
	print(top, bottom, left, right)
	croppedImage = originalImage.crop((left, top, right, bottom))
	croppedImage.show()
	croppedImage.save(f"{outputFileName}.jpeg")
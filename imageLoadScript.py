from os import listdir
from PIL import Image as PImage

def loadImages(path):
    # return array of images

    imagesList = listdir(path)
    loadedImages = []
    for image in imagesList:
        img = PImage.open(path + image)
        loadedImages.append(img)

    return loadedImages

path = "/Users/jeffreyzhang/Downloads"

# your images in an array
imgs = loadImages(path)

for img in imgs:
    # you can show every image
    img.show()

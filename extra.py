import pickle
import base64
from io import BytesIO
from PIL import Image

# object
class img(object):
    __array_interface__ = []
    mode = ""

    # The class "constructor" - It's actually an initializer
    def __init__(self, array_interface, mode):
        self.__array_interface__ = array_interface
        self.mode = mode

def make_img(array_interface, mode):
    myimg = img(array_interface, mode)
    return myimg

import indicoio

indicoio.config.api_key = '3244a46ccac6ac4cf7d163a6240b5531'

face = indicoio.facial_localization(r"C:\Users\ldann\Downloads\jeffrey.jpg", crop=True)

face = face[0]

face = face['image']

imgobj = make_img(face, None)

print(imgobj)

pil_img = Image.fromarray(imgobj)
buff = BytesIO()
pil_img.save(buff, format="JPEG")
face64 = base64.b64encode(buff.getvalue()).decode("utf-8")

print(face64)


i = 0
for imgin in r"C:\Users\ldann\Downloads\img_in\jeffrey\*.JPG":
    print(imgin)
    imgout = r"C:\Users\ldann\Downloads\img_out\jeffrey\img" + str(i) + ".jpg"
    saveFaceImage(imgin, imgout, "Jeffrey")
    print(imgout)
    i += 1


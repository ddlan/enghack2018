import scipy.misc
import glob

import indicoio

from indicoio.custom import Collection
indicoio.config.api_key = '3244a46ccac6ac4cf7d163a6240b5531'


collection = Collection("facial_recognition three")

def testFaceImage(urlin, imgout):
    face = indicoio.facial_localization(urlin, sensitivity=0.05, crop=True)
    print(face)
    if len(face) >= 1:
        face = face[0]
        face = face['image']

        scipy.misc.imsave(imgout, face)

        print(collection.predict(imgout))



i = 0
for imgin in glob.iglob(r'C:\Users\ldann\Downloads\img_in\test\*.jpg'):
    print(imgin)
    imgout = r"C:\Users\ldann\Downloads\img_out\test\test" + str(i) + ".jpg"
    testFaceImage(imgin, imgout)
    print(imgout)
    i += 1
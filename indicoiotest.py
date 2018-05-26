import scipy.misc
import glob

import indicoio

from indicoio.custom import Collection
indicoio.config.api_key = '3244a46ccac6ac4cf7d163a6240b5531'

def saveFaceImage(urlin, urlout):
    face = indicoio.facial_localization(urlin, sensitivity=0, crop=True)
    face = face[0]
    face = face['image']

    scipy.misc.imsave(urlout, face)

collection = Collection("facial_recognition two")

i = 0
for image_file in glob.iglob(r'C:\Users\ldann\Downloads\img_in\danny\*.jpg'):
    imgurl = r'C:\Users\ldann\Downloads\img_out\danny\img' + str(i) + '.jpg'
    saveFaceImage(image_file, imgurl)
    collection.add_data([imgurl, "Danny"])
    i += 1

for image_file in glob.iglob(r'C:\Users\ldann\Downloads\img_in\jeffrey\*.jpg'):
    imgurl = r'C:\Users\ldann\Downloads\img_out\jeffrey\img' + str(i) + '.jpg'
    saveFaceImage(image_file, imgurl)
    collection.add_data([imgurl, "Jeffrey"])
    i += 1


collection.train()

collection.wait()

print(collection.predict(r'C:\Users\ldann\Downloads\img_in\jeffrey.jpg'))
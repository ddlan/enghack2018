import scipy.misc
import indicoio
import numpy as np

indicoio.config.api_key = '3244a46ccac6ac4cf7d163a6240b5531'


def saveFaceImage(url, id):
    face = indicoio.facial_localization(r"https://peopledotcom.files.wordpress.com/2018/04/will-ferrell.jpg",
                                    sensitivity=0, crop=True)
    face = face[0]
    face = face['image']

    scipy.misc.imsave(r'C:\Users\ldann\Downloads\outfile.jpg', face)


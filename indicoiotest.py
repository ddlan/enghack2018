import indicoio

from indicoio.custom import Collection
indicoio.config.api_key = '3244a46ccac6ac4cf7d163a6240b5531'

collection = Collection("facial_recognition")

collection.add_data([[indicoio.facial_localization(r"C:\Users\ldann\Desktop\1B\PD-COOP\linkedin.IMG_7805_DxO.jpg", "Danny"],
                     [r"C:\Users\ldann\Desktop\1B\PD-COOP\linkedin.IMG_7809_DxO.jpg", "Danny"],
                     ["https://upload.wikimedia.org/wikipedia/commons/3/38/Will_Ferrell_2013.jpg", "Will"],
                     [r"C:\Users\ldann\Downloads\jeffrey.jpg", "Jeffrey"]])

collection.train()

collection.wait()

print(collection.predict(r'C:\Users\ldann\Desktop\1B\PD-COOP\linkedin.IMG_7818_DxO.jpg'))
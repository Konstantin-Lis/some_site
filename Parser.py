from selenium import webdriver
import cv2

from tensorflow.keras.models import load_model
model = load_model("Cars_and_Roads9857.h5")

from tensorflow.keras import models
from tensorflow.keras import layers
from tensorflow.keras import optimizers
import os
import glob
import shutil
import sys
import numpy as np

def predict_image(img_path):
    # Read the image and resize it
    img = image.load_img(img_path, target_size=(90, 90))
    # Convert it to a Numpy array with target shape.
    x = image.img_to_array(img)
    # Reshape
    x = x.reshape((1,) + x.shape)
    x /= 255.
    result = model.predict([x])[0][0]
    if result > 0.5:
        return 1
    else:
        return 0

driver = webdriver.Chrome("C://Users/USER/PycharmProjects/pythonProject/chromedriver.exe")
driver.get("localhost:8000")

elem = driver.find_elements_by_class_name("link_menu")[1]
driver.get("http://localhost:8000/contacts.html")

images = driver.find_elements_by_tag_name("img")
driver.save_screenshot("screenshot.png")
image = cv2.imread("screenshot.png")

for i in range(9):
    loc = images[i].location
    img = image[loc['y']+46+30*(i//3):loc['y']+46+30*(i//3)+90, loc['x']+2+30*(i%3):loc['x']+2+30*(i%3)+90]
    cv2.imwrite("img_"+str(i)+".jpg", img)
    ans = predict_image("img_"+str(i)+".jpg")
    if ans == 1:
        images[i].click()

#driver.quit()

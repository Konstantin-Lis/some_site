from selenium import webdriver
import cv2

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
driver.quit()

from selenium import webdriver
import cv2
import time
import random

count3 = 0
count4 = 0
#Когда запускать для сбора данных, то поменять i с 10 на большое число
for i in range(10):
    driver = webdriver.Chrome("C://Users/USER/PycharmProjects/pythonProject/chromedriver.exe")
    driver.get("https://www.google.com/recaptcha/api2/demo")

    button = driver.find_element_by_id("recaptcha-demo")
    button.click()

    t = random.randint(3, 6)
    time.sleep(t)
    driver.save_screenshot("screenshot.png")

    driver.quit()

    #Блок обработки скриншота
    image = cv2.imread("screenshot.png")

    img = image[104: 830, 106:606]
    task_block = img[9:151, 9:491]
    pic_block = img[157:641, 8:495]
    line = pic_block[161:162, 0:484]

    is_3_3 = True
    for j in range(480):
        if line[0, i][0] not in range(250, 256):
            is_3_3 = False
            break
        elif line[0, i][1] not in range(250, 256):
            is_3_3 = False
            break
        elif line[0, i][2] not in range(250, 256):
            is_3_3 = False
            break

    if is_3_3:
        cv2.imwrite("3x3/tasks/"+str(count3)+"_task_block.jpg", task_block)

        img_0_0 = pic_block[0:160, 0:159]
        cv2.imwrite("3x3/imags/"+str(count3)+"_img_0_0.jpg", img_0_0)

        img_0_1 = pic_block[163:322, 0:159]
        cv2.imwrite("3x3/imags/"+str(count3)+"_img_0_1.jpg", img_0_1)

        img_0_2 = pic_block[324:484, 0:159]
        cv2.imwrite("3x3/imags/"+str(count3)+"_img_0_2.jpg", img_0_2)

        img_1_0 = pic_block[0:160, 163:322]
        cv2.imwrite("3x3/imags/"+str(count3)+"_img_1_0.jpg", img_1_0)

        img_1_1 = pic_block[163:322, 163:322]
        cv2.imwrite("3x3/imags/"+str(count3)+"_img_1_1.jpg", img_1_1)

        img_1_2 = pic_block[324:484, 163:322]
        cv2.imwrite("3x3/imags/"+str(count3)+"_img_1_2.jpg", img_1_2)

        img_2_0 = pic_block[0:160, 326:485]
        cv2.imwrite("3x3/imags/"+str(count3)+"_img_2_0.jpg", img_2_0)

        img_2_1 = pic_block[163:322, 326:485]
        cv2.imwrite("3x3/imags/"+str(count3)+"_img_2_1.jpg", img_2_1)

        img_2_2 = pic_block[324:484, 326:485]
        cv2.imwrite("3x3/imags/"+str(count3)+"_img_2_2.jpg", img_2_2)

        count3 += 1

    else:
        cv2.imwrite("4x4/tasks/"+str(count4)+"_task_block.jpg", task_block)

        img_0_0 = pic_block[1:121, 0:121]
        cv2.imwrite("4x4/imags/"+str(count4)+"_img_0_0.jpg", img_0_0)

        img_0_1 = pic_block[122:242, 0:121]
        cv2.imwrite("4x4/imags/"+str(count4)+"_img_0_1.jpg", img_0_1)

        img_0_2 = pic_block[243:363, 0:121]
        cv2.imwrite("4x4/imags/"+str(count4)+"_img_0_2.jpg", img_0_2)

        img_0_3 = pic_block[364:484, 0:121]
        cv2.imwrite("4x4/imags/"+str(count4)+"_img_0_3.jpg", img_0_3)

        img_1_0 = pic_block[1:121, 122:243]
        cv2.imwrite("4x4/imags/"+str(count4)+"_img_1_0.jpg", img_1_0)

        img_1_1 = pic_block[122:242, 122:243]
        cv2.imwrite("4x4/imags/"+str(count4)+"_img_1_1.jpg", img_1_1)

        img_1_2 = pic_block[243:363, 122:243]
        cv2.imwrite("4x4/imags/"+str(count4)+"_img_1_2.jpg", img_1_2)

        img_1_3 = pic_block[364:484, 122:243]
        cv2.imwrite("4x4/imags/"+str(count4)+"_img_1_3.jpg", img_1_3)

        img_2_0 = pic_block[1:121, 244:365]
        cv2.imwrite("4x4/imags/"+str(count4)+"_img_2_0.jpg", img_2_0)

        img_2_1 = pic_block[122:242, 244:365]
        cv2.imwrite("4x4/imags/"+str(count4)+"_img_2_1.jpg", img_2_1)

        img_2_2 = pic_block[243:363, 244:365]
        cv2.imwrite("4x4/imags/"+str(count4)+"_img_2_2.jpg", img_2_2)

        img_2_3 = pic_block[364:484, 244:365]
        cv2.imwrite("4x4/imags/"+str(count4)+"_img_2_3.jpg", img_2_3)

        img_3_0 = pic_block[1:121, 366:487]
        cv2.imwrite("4x4/imags/"+str(count4)+"_img_3_0.jpg", img_3_0)

        img_3_1 = pic_block[122:242, 366:487]
        cv2.imwrite("4x4/imags/"+str(count4)+"_img_3_1.jpg", img_3_1)

        img_3_2 = pic_block[243:363, 366:487]
        cv2.imwrite("4x4/imags/"+str(count4)+"_img_3_2.jpg", img_3_2)

        img_3_3 = pic_block[364:484, 366:487]
        cv2.imwrite("4x4/imags/"+str(count4)+"_img_3_3.jpg", img_3_3)

        count4 += 1

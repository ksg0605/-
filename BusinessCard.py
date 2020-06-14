#명함을 제작하는 프로그램입니
import numpy as np
import cv2
from PIL import Image, ImageDraw, ImageFont
import os
   
def bitOperation(hpos, vpos):
    img1 = cv2.imread('data/background.png')
    img2 = cv2.imread('data/t_logo.png')

    rows, cols, channels = img2.shape
    roi = img1[vpos:rows+vpos, hpos:cols+hpos]

    img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)

    img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)

    img2_fg = cv2.bitwise_and(img2, img2, mask=mask)

    dst = cv2.add(img1_bg, img2_fg)
    img1[vpos:rows+vpos, hpos:cols+hpos] = dst

    img1 = cv2.imwrite('data/BusinessCardBackground.png', img1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

bitOperation(770, 10) #로고의 위치 지정

print("명함 제작에 필요한 정보를 입력합니다.")
name = input("이름:")
position = input("직위:")
belong = input("소속:")
phone = input("전화번호:")
mail = input("E-mail:")

businesscard = Image.open('data/BusinessCardBackground.png')
fontsFolder = 'data/FontData'
nameFont = ImageFont.truetype(os.path.join(fontsFolder, 'NanumGothicBold.ttf'), 70)
positionFont = ImageFont.truetype(os.path.join(fontsFolder, 'NanumGothicLight.ttf'), 40)
infoFont = ImageFont.truetype(os.path.join(fontsFolder, 'NanumGothicLight.ttf'), 20)
draw = ImageDraw.Draw(businesscard)
draw.text((40, 120), name, fill='black', font=nameFont)
draw.text((300, 160), position, fill='black', font=positionFont)
draw.text((700, 550), belong, fill='black', font=infoFont)
draw.text((700, 580), "Mobile)"+phone, fill='black', font=infoFont)
draw.text((700, 610), "E-mail)"+mail, fill='black', font=infoFont)


businesscard.save('data/lastresult.png')
businesscard.show()

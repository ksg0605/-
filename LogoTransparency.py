#로고의 배경을 삭제하는 프로그램입니다
from PIL import Image
 
img = Image.open('image/logo.jpg')
img = img.convert("RGBA")
datas = img.getdata()
 
newData = []
cutOff = 255
 
for item in datas:
    if item[0] >= cutOff and item[1] >= cutOff and item[2] >= cutOff:
        newData.append((255, 255, 255, 0))
        
    else:
        newData.append(item)
       
 
img.putdata(newData)
img.save("t_logo.png", "PNG") 

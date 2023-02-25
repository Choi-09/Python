from openpyxl import Workbook
from openpyxl.drawing.image import Image

wb = Workbook()
ws = wb.active

# 이미지 가져오기: 
img = Image("image.png")

# C3 위치에 img.png 이미지를 삽입
ws.add_image(img, "C3")

wb.save("rpa_image.xlsx")
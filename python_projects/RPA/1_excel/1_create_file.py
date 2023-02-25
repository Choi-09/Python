from openpyxl import Workbook

wb = Workbook() # 새 워크북 생성
ws = wb.active # 현재 활성화된 sheet 가져옴 
ws.title = 'RPASheet' # sheet의 이름 변경
wb.save("rpa_test1.xlsx") # 파일 저장 
wb.close() # 파일 닫기

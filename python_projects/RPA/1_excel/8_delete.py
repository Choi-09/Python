from openpyxl import load_workbook

wb = load_workbook("rpa_test5.xlsx")
ws = wb.active

# ws.delete_rows(8) # 8번째 줄에 있는 7번학생 정보가 들어있는 줄 전체 삭제. => 뒤에 있는 데이터가 자동으로 위로 당김 된다.
# ws.delete_rows(8, 3) # 8번째 줄에 있는 7번학생 부터 3명(7, 8, 9번 학생) 줄 전체 삭제 
# wb.save("rpa_test5_delete_rows.xlsx")

#ws.delete_cols(2) # 2번째 col에 있는 영어 컬럼 전체 삭제
# ws.delete_cols(2,2) # 2번째 col에 있는 영어, 수학 컬럼 전체 삭제
# wb.save("rpa_test5_delete_cols.xlsx")
from openpyxl import load_workbook

wb = load_workbook("rpa_test5.xlsx")
ws = wb.active

# row 삽입 
# ws.insert_rows(8) # 8번 row에 빈 row 추가
# ws.insert_rows(8,5) # 8번째 row부터 5줄 추가
# wb.save("rpa_test5_insert_rows.xlsx")

# col 삽입
# ws.insert_cols(2) # B번 열에 빈 col 추가
# ws.insert_cols(2,3) # B번 열부터 3개 col 추가
# wb.save("rpa_test5_insert_cols.xlsx")
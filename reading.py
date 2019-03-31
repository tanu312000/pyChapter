import xlrd
loc=("/home/tanu/programs/pythonFiles/employee.xlsx")
wb=xlrd.open_workbook(loc)
sheet=wb.sheet_by_index(2)
print(sheet.cell_value(1,1))

import xlrd
loc=("/home/tanu/programs/pythonFiles/employee.xlsx")
wb=xlrd.open_workbook(loc)
sheet=wb.sheet_by_index(0)
print((sheet.cell_value(0,0)))
print(sheet.nrows,sheet.ncols)
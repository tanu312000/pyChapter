import xlrd
loc=("/home/tanu/programs/pythonFiles/employee.xlsx")
wb=xlrd.open_workbook(loc)
sheet=wb.sheet_by_index(0)

for i in range(sheet.nrows):
    print()
    for j in range(sheet.ncols):
        print(sheet.cell_value(i,j),end='')
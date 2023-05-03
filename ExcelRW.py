import openpyxl

wb = openpyxl.load_workbook(r'sample_data.xlsx')
sh = wb.active
for i in range(1, 11):
    sh.cell(1,i).value='AA'

data = (
    (11, 48, 50),
    (81, 30, 82),
    (20, 51, 72),
    (21, 14, 60),
    (28, 41, 49),
    (74, 65, 53),
    ("Peter", 'Andrew',45.63)
)

for i in data:
    sh.append(i)

wb.save('sample_data.xlsx')


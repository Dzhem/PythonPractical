import xlrd

wb = xlrd.open_workbook('trekking1.xlsx')
sheet = wb.sheet_by_index(0)

prod_names = sheet.col_values(0, 1)
prod_calories = sheet.col_values(1, 1)

j = 0
while j < len(prod_names):
    i = 0
    while i < len(prod_calories) - 1:
        if prod_calories[i] < prod_calories[i + 1]:
            (prod_calories[i], prod_calories[i + 1]) = (
                prod_calories[i + 1], prod_calories[i])
            (prod_names[i], prod_names[i + 1]) = (
                prod_names[i + 1], prod_names[i])
        i += 1
    j += 1

j = 0
while j < len(prod_names):
    i = 0
    while i < len(prod_calories) - 1:
        if prod_calories[i] == prod_calories[i + 1]:
            if prod_names[i] > prod_names[i + 1]:
                (prod_names[i], prod_names[i + 1]) = (
                    prod_names[i + 1], prod_names[i])
        i += 1
    j += 1

for prod_name in prod_names:
    print(prod_name)

# -*- coding: iso-8859-1 -*-
import xlrd
import xlwt
"""
file = xlrd.open_workbook('Zensurtabelle.xlsx')

sh = file.sheet_by_name('Tabelle1')

for row_number in range(sh.nrows):
    print(sh.row_values(row_number))
print(sh)
"""

class CalcGrades:
    grades = {
        1: [100,96],
        2: [95, 85],
        3: [84, 68],
        4: [67, 50],
        5: [49, 25],
        6: [24, 0]
    }

    def run(self):
        dict_excel = {}
        points = 8

        for inti in range(1):
            points += 2
            dict = {}
            for grade in list(self.grades.keys()):
                percent_up = self.grades[grade][0]
                percent_down = self.grades[grade][1]
                point_up = round(points / 100 * percent_up)
                point_down = round(points / 100 * percent_down)

                if point_up == point_down:
                    point_up = ' '
                dict[grade] = [point_up, point_down]
            dict_excel[points] = dict
        return dict_excel

cla = CalcGrades()
print(cla.run())

"""

wb = xlwt.Workbook()
ws = wb.add_sheet('Zensurentabelle')
row_0 = ['', 100.0, '-', 96.0, 95.0, '-', 85.0, 84.0, '-', 68.0, 67.0, '-', 50.0, 49.0, '-', 25.0, 24.0, '-', 0.0]
row_excel= ws.row(0)
for col in range(19):
    row_excel.write(col, row_0[col])
points = 8
for row in range(1, 30):
    row_excel = ws.row(row)
    points += 2
    row_excel.write(0, points)
    for col in range(1, 19):
        if col == 1:

    row_excel.write(2,'2')
wichtig = ['', 100.0, '-', 96.0, 95.0, '-', 85.0, 84.0, '-', 68.0, 67.0, '-', 50.0, 49.0, '-', 25.0, 24.0, '-', 0.0]

wb.save('Zensurentabelle_gut.xls')
"""""
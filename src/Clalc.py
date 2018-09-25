# -*- coding: iso-8859-1 -*-
import xlsxwriter


class CalcGrades:
    grades = {
        1: [100,96],
        2: [95, 85],
        3: [84, 68],
        4: [67, 50],
        5: [49, 25],
        6: [24, 0]
    }
    lis_grade = [[100, 96],[95, 85],[84, 68],[67, 50],[49, 25],[24, 0]]

    def run(self):
        dic_excel = {}
        for points in range(10, 101, +2):
            grade = 6
            dic_grade = {}
            dynamic_important = None
            for inti_dynamic in range(0, points + 1):
                percent = round(100 / points * inti_dynamic)
                new_grade = self.find_grade(percent=percent)
                if grade != new_grade :

                    if grade == 6:
                        dic_grade[6] = [0, inti_dynamic - 1]
                        dynamic_important = inti_dynamic
                    else:
                        dic_grade[grade] = [dynamic_important, inti_dynamic-1]
                        dynamic_important = inti_dynamic
                        if new_grade == 1:
                            dic_grade[1] = [dynamic_important, points]
                    grade = new_grade

                    grade = new_grade
            dic_excel[points] = dic_grade
        return dic_excel


    def find_grade(self, percent):
        for inti in range(len(self.lis_grade)):
            if self.lis_grade[inti][0] >= percent >= self.lis_grade[inti][1]:
                return inti + 1
class Exporter:

    def export(self, dic_excel):
        wb = xlsxwriter.Workbook()
        ws = wb.add_sheet('Zensurentabelle')
        row_0 = ['', 100.0, '-', 96.0, 95.0, '-', 85.0, 84.0, '-', 68.0, 67.0, '-', 50.0, 49.0, '-', 25.0, 24.0, '-', 0.0]
        row_excel = ws.row(0)
        for col in range(19):
            row_excel.write(col, row_0[col])

        lis_dic = list(dic_excel.keys())
        sorted(lis_dic)
        row = 0
        for points in lis_dic:
            row += 1
            row_excel = ws.row(row)
            dic_points = dic_excel[points]

            row_excel.write(0, points)
            if dic_points[1][0] != dic_points[1][1]:
                row_excel.write(1, dic_points[1][1])
                row_excel.write(2, '-')
                row_excel.write(3, dic_points[1][0])
            else:
                row_excel.write(3, dic_points[1][1])

            if dic_points[2][0] != dic_points[2][1]:
                row_excel.write(4, dic_points[2][1])
                row_excel.write(5, '-')
                row_excel.write(6, dic_points[2][0])
            else:
                row_excel.write(6, dic_points[2][1])

            row_excel.write(7, dic_points[3][1])
            row_excel.write(8, '-')
            row_excel.write(9, dic_points[3][0])

            row_excel.write(10, dic_points[4][1])
            row_excel.write(11, '-')
            row_excel.write(12, dic_points[4][0])

            row_excel.write(13, dic_points[5][1])
            row_excel.write(14, '-')
            row_excel.write(15, dic_points[5][0])

            row_excel.write(16, dic_points[6][1])
            row_excel.write(17, '-')
            row_excel.write(18, dic_points[6][0])


        wb.save('Zensurentabelle_test1.xls')
bla = CalcGrades()
dic = bla.run()

Exporter().export(dic_excel=dic)
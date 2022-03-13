##############
# By zhangtanliu
# 3/6/2022
##############

import xlrd
from mysqlLibs.report import Report
import argparse


class ResultTable(object):

    def __init__(self, report):
        self.report = report

    def update_all(self):
        self.get_title_index()
        self.update_table()

    def get_title_index(self):
        data = xlrd.open_workbook(self.report)
        self.fps_table = data.sheet_by_name("Yours")
        row_values = self.fps_table.row_values(0, start_colx=0, end_colx=None)
        print(row_values)
        self.pre1, self.pre2 = row_values[0:1]
        print(self.pre1, self.pre2)

    def update_table(self):
        nrows = self.fps_table.nrows
        myDB = Report()
        for i in range(1, nrows):
            model, kpi1, kpi2 = self.fps_table.row_values(i, start_colx=0, end_colx=None)
            modelID = myDB.find_model_id(model)

            kpiID = myDB.add_kpi("kpi1")
            myDB.add_result(value=kpi1, modelID=modelID, kpiID=kpiID)

            kpiID = myDB.add_kpi("kpi2")
            myDB.add_result(value=kpi2, modelID=modelID, kpiID=kpiID)


if __name__ == r"__main__":
    parser = argparse.ArgumentParser(description='upload result into DB')
    parser.add_argument("--table", type=str, default='')
    parser=parser.parse_args()
    args = parser.__dict__

    report = args['table']
    result = ResultTable(report)
    result.update_all()
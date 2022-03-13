##############
# By zhangtanliu
# 3/6/2022
##############

import xlrd
from mysqlLibs.report import Report
import argparse


class ModelTable(object):

    def __init__(self):
        self.model_table = xlrd.open_workbook(report).sheet_by_name('model')

    def update_model_table(self):
        nrows = self.model_table.nrows
        myDB = Report()
        for i in range(1, nrows):
            name, f1, f2 = self.model_table.row_values(0, start_colx=0, end_colx=None)
            myDB.add_model(name=name)


if __name__ == r"__main__":
    parser = argparse.ArgumentParser(description='update model into DB')
    parser.add_argument("--model_sheet", type=str, default='')
    parser=parser.parse_args()
    args = parser.__dict__

    report = args['model_sheet']
    result = ModelTable(report)
    result.update_all()

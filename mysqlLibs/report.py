##############
# By zhangtanliu
# 3/6/2022
# ref. liaoxunfeng
# https://www.liaoxuefeng.com/wiki/1016959663602400/1017803857459008
# https://www.cnblogs.com/mrchige/p/6389588.html
# https://www.cnblogs.com/awfj/p/11004185.html
##############

from sqlalchemy import create_engine
from mysqlLibs.Tables import KPI, Result, Model
from sqlalchemy.orm import sessionmaker


class Report(object):

    def __init__(self):

        engine = create_engine('mysql+mysyldb://root:serverIP@port/tablename')

        DBSession = sessionmaker(bind=engine)
        self.db_session = DBSession()

    def find_model_id(self, name):

        model_objects = self.db_session.query(Model).filter(Model.name == name).all()

        if len(model_objects) == 1:
            return model_objects[-1].id

        if len(model_objects) == 0:
            print('Model not found: %s' % name)

        if len(model_objects) > 1:
            model_objects.sort()
            for o in model_objects:
                print('Found model: %s' % o)
            print('Found more than one model.')
            return [model.id for model in model_objects]

        return None

    def delete_model(self, name):

        model_objects = self.db_session.query(Model).filter(Model.name == name).all()

        if len(model_objects) == 1:
            print('Found model: %s, will delete it.' % name)
            self.db_session.delete(model_objects[0])
            self.db_session.commit()

        if len(model_objects) == 0:
            print('Model not found: %s, do nothing.' % name)

        if len(model_objects) > 1:
            print('Found more than one model, do nothing.')

    def add_model(self, name):

        model_objects = self.db_session.query(Model).filter(Model.name == name).all()

        if len(model_objects) == 0:
            print("Model doesn't exist, create new record.")
            self.db_session.add_all([Model(name=name)])
            self.db_session.commit()
            model_objects = self.db_session.query(Model).filter(Model.name == name).all()
        else:
            print("Model exists, won't create new record.")

        return model_objects[-1].id

    def add_kpi(self, name):

        kpi_objects = self.db_session.query(KPI).filter(KPI.name == name).all()

        if len(kpi_objects) == 0:
            print("KPI doesn't exist, create new record.")
            self.db_session.add_all([KPI(name=name)])
            self.db_session.commit()
            kpi_objects = self.db_session.query(KPI).filter(KPI.name == name).all()
        else:
            print("KPI exists, won't create new record.")

        return kpi_objects[-1].id

    def delete_result(self, value, modelID, kpiID):

        result_objects = self.db_session.query(Result).filter(Result.ModelID == modelID, Result.KPIID == kpiID, Result.value == value).all()

        if len(result_objects) == 0:
            print("Not found any result, do nothing.")

        if len(result_objects) == 1:
            print("Found a record, will delete %s." % value)
            self.db_session.delete(result_objects[0])
            self.db_session.commit()

        if len(result_objects) > 1:
            print("Found more than one result: %s, %s, %s" % (modelID, kpiID, value))

    def add_result(self, value, modelID, kpiID):

        result_objects = self.db_session.query(Result).filter(Result.ModelID == modelID, Result.KPIID == kpiID,
                                                              Result.value == value).all()

        if len(result_objects) == 0:
            print("Create new record: %s" % value)
            self.db_session.add_all([Result(ModelID=modelID, KPIID=kpiID, value=value)])
            self.db_session.commit()
            print('Succeed')
        else:
            print('Result has been recorded, do nothing.')

    def update_result(self, value, modelID, kpiID):

        result_objects = self.db_session.query(Result).filter(Result.ModelID == modelID, Result.KPIID == kpiID,
                                                              Result.value == value).all()

        for result in result_objects:
            if result.value == value:
                # do whatever modification you want here of column's name
                # result.KPIID = kpiID
                self.db_session.add(result)
                self.db_session.commit()

    def close_db(self):
        self.db_session.close()


# for debugging
if __name__ == "__main__":
    myDB = Report()
    myDB.add_result(value=123, modelID=111, kpiID=22)
    myDB.close_db()
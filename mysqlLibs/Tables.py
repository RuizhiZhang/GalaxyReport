##############
# By zhangtanliu
# 3/6/2022
# ref. liaoxuefeng
# https://www.liaoxuefeng.com/wiki/1016959663602400/1017803857459008
# https://www.cnblogs.com/mrchige/p/6389588.html
# https://www.cnblogs.com/awfj/p/11004185.html
##############

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey, Column, String, Integer, FLOAT, TIMESTAMP
from sqlalchemy.orm import relationship

Base = declarative_base()


class Model(Base):

    __tablename__ = 'Model'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(90), nullable=False)
    results = relationship('Result')
    sourceModelID = Column(Integer, ForeignKey('SourceModel.id'))


class KPI(Base):

    __tablename__ = 'KPI'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(90), nullable=False)
    results = relationship('Result')


class Result(Base):

    __tablename__ = 'Result'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    value = Column(FLOAT(90), nullable=False)
    timestamp = Column(TIMESTAMP)
    ModelID = Column(Integer, ForeignKey('Model.id'))
    KPIID = Column(Integer, ForeignKey('KPI.id'))

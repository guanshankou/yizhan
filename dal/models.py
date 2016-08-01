from sqlalchemy import create_engine, func, ForeignKey, Column
from sqlalchemy.types import String, Integer, Boolean, Float, Date, BigInteger, DateTime, Time, SMALLINT,REAL
from sqlalchemy.orm import relationship, backref
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.dialects.mysql import TINYINT
from dal.db_configs import YizhanBase, DBSession

#初始化数据库 与数据库建连接
def init_db_data():
	YizhanBase.metadata.create_all()
	return True

class Test(YizhanBase):
	__tablename__="test"
	id=Column(Integer,primary_key=True,autoincrement=True)
	name=Column(String(10))
	
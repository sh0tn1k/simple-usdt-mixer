from sqlalchemy import Column,Integer, String ,Boolean, Date, ForeignKey, Float

from db.base_class import Base

# Модель таблицы «транзакций» в БД
class Transaction(Base):
    id = Column(Integer,primary_key=True,index=True)
    txid = Column(String,unique=True,nullable=False)
    amount = Column(Float,nullable=False)
    date = Column(Date)
    status = Column(String,nullable=False)
    note = Column(String,nullable=True)
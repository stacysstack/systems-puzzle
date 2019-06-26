from database import Base
# mine
# from app import 
from sqlalchemy import Column, Integer, String
from sqlalchemy.types import DateTime

class Items(Base):
    """
    Items table
    """
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    name = Column(String(256))
    quantity = Column(Integer)
    description = Column(String(256))
    date_added = Column(DateTime())

    # def __init__(self,id, name, quantity, description, date_added):
    #     self.id = id
    #     self.name = name
    #     self.quantity = quantity
    #     self.description = description
    #     self.date_added = date_added
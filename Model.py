import sqlalchemy
from sqlalchemy import create_engine
engine = create_engine('postgresql://postgres:111@localhost/lab', echo = True)
from sqlalchemy import MetaData, Table, Column, Integer, String, ForeignKey, Date, Text
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy.orm import sessionmaker

meta = MetaData()

Base = declarative_base()

class Train(Base):
    __tablename__ = 'train'
    train_id = Column(Integer, primary_key=True)
    datetime = Column(Date)
    drivers = relationship("Driver", secondary='traindriver')

class Driver(Base):
    __tablename__ = 'driver'
    driver_id = Column(Integer, primary_key=True)
    name = Column(String)
    trains = relationship("Train", secondary='traindriver')

class TrainDriverAssoc(Base):
    __tablename__ = 'traindriver'
    train_id = Column(Integer, ForeignKey('train.train_id'), primary_key=True)
    driver_id = Column(Integer, ForeignKey('driver.driver_id'), primary_key=True)

class Carriage(Base):
    __tablename__ = 'carriage'
    carriage_id = Column(Integer, primary_key=True)
    train_id = Column(Integer, ForeignKey('train.train_id'))
    carriage_type = Column(String)
    place = relationship("Place", order_by="Place.place_id", back_populates="carriage")

class Place(Base):
    __tablename__ = 'place'
    place_id = Column(Integer, primary_key=True)
    carriage_id = Column(Integer, ForeignKey('carriage.carriage_id'))
    ticket = relationship("Ticket", order_by="Ticket.ticket_id", back_populates="place")
    carriage = relationship("Carriage", back_populates="place")

class Ticket(Base):
    __tablename__ = 'ticket'
    ticket_id = Column(Integer, primary_key=True)
    place_id = Column(Integer, ForeignKey('place.place_id'))
    place = relationship("Place", back_populates="ticket")

Session = sessionmaker(bind=engine)











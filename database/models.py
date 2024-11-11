# coding: utf-8
from sqlalchemy import DECIMAL, DateTime  # API Logic Server GenAI assist
from sqlalchemy import Column, Date, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

########################################################################################################################
# Classes describing database for SqlAlchemy ORM, initially created by schema introspection.
#
# Alter this file per your database maintenance policy
#    See https://apilogicserver.github.io/Docs/Project-Rebuild/#rebuilding
#
# Created:  November 11, 2024 15:23:44
# Database: sqlite:////tmp/tmp.wqPrTGV51A-01JCDX2P0JGDEHWG3B81H95CQD/DogWalkBiz/database/db.sqlite
# Dialect:  sqlite
#
# mypy: ignore-errors
########################################################################################################################
 
from database.system.SAFRSBaseX import SAFRSBaseX
from flask_login import UserMixin
import safrs, flask_sqlalchemy
from safrs import jsonapi_attr
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.sql.sqltypes import NullType
from typing import List

db = SQLAlchemy() 
Base = declarative_base()  # type: flask_sqlalchemy.model.DefaultMeta
metadata = Base.metadata

#NullType = db.String  # datatype fixup
#TIMESTAMP= db.TIMESTAMP

from sqlalchemy.dialects.sqlite import *



class Administration(SAFRSBaseX, Base):
    """
    description: Administration data for the business.
    """
    __tablename__ = 'administration'
    _s_collection_name = 'Administration'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    admin_name = Column(String, nullable=False)
    created_date = Column(DateTime, nullable=False)
    updated_date = Column(DateTime, nullable=False)
    created_by = Column(String, nullable=False)

    # parent relationships (access parent)

    # child relationships (access children)



class Owner(SAFRSBaseX, Base):
    """
    description: Represents a dog owner who requests services.
    """
    __tablename__ = 'owner'
    _s_collection_name = 'Owner'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    address = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    email = Column(String, nullable=False)
    created_date = Column(DateTime, nullable=False)
    updated_date = Column(DateTime, nullable=False)
    created_by = Column(String, nullable=False)

    # parent relationships (access parent)

    # child relationships (access children)
    DogList : Mapped[List["Dog"]] = relationship(back_populates="owner")
    PaymentInformationList : Mapped[List["PaymentInformation"]] = relationship(back_populates="owner")
    WalkRequestList : Mapped[List["WalkRequest"]] = relationship(back_populates="owner")
    PaymentList : Mapped[List["Payment"]] = relationship(back_populates="owner")
    WalkerReviewList : Mapped[List["WalkerReview"]] = relationship(back_populates="owner")



class Walker(SAFRSBaseX, Base):
    """
    description: Represents a dog walker who registers and provides services.
    """
    __tablename__ = 'walker'
    _s_collection_name = 'Walker'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    postal_code = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    email = Column(String, nullable=False)
    max_dogs_per_walk = Column(Integer, nullable=False)
    created_date = Column(DateTime, nullable=False)
    updated_date = Column(DateTime, nullable=False)
    created_by = Column(String, nullable=False)

    # parent relationships (access parent)

    # child relationships (access children)
    WalkerAvailabilityList : Mapped[List["WalkerAvailability"]] = relationship(back_populates="walker")
    WalkerRateList : Mapped[List["WalkerRate"]] = relationship(back_populates="walker")
    WalkScheduleList : Mapped[List["WalkSchedule"]] = relationship(back_populates="walker")
    PaymentList : Mapped[List["Payment"]] = relationship(back_populates="walker")



class Dog(SAFRSBaseX, Base):
    """
    description: Represents a dog belonging to an owner.
    """
    __tablename__ = 'dog'
    _s_collection_name = 'Dog'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    owner_id = Column(ForeignKey('owner.id'), nullable=False)
    name = Column(String, nullable=False)
    breed = Column(String, nullable=False)
    size = Column(String(10), nullable=False)
    notes = Column(String)
    created_date = Column(DateTime, nullable=False)
    updated_date = Column(DateTime, nullable=False)
    created_by = Column(String, nullable=False)

    # parent relationships (access parent)
    owner : Mapped["Owner"] = relationship(back_populates=("DogList"))

    # child relationships (access children)



class PaymentInformation(SAFRSBaseX, Base):
    """
    description: Stores payment information for an owner.
    """
    __tablename__ = 'payment_information'
    _s_collection_name = 'PaymentInformation'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    owner_id = Column(ForeignKey('owner.id'), nullable=False)
    service = Column(String(10), nullable=False)
    created_date = Column(DateTime, nullable=False)
    updated_date = Column(DateTime, nullable=False)
    created_by = Column(String, nullable=False)

    # parent relationships (access parent)
    owner : Mapped["Owner"] = relationship(back_populates=("PaymentInformationList"))

    # child relationships (access children)



class WalkRequest(SAFRSBaseX, Base):
    """
    description: A request made by an owner for a dog walk.
    """
    __tablename__ = 'walk_request'
    _s_collection_name = 'WalkRequest'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    owner_id = Column(ForeignKey('owner.id'), nullable=False)
    date = Column(Date, nullable=False)
    time = Column(String(10), nullable=False)
    duration = Column(String(10), nullable=False)
    created_date = Column(DateTime, nullable=False)
    updated_date = Column(DateTime, nullable=False)
    created_by = Column(String, nullable=False)

    # parent relationships (access parent)
    owner : Mapped["Owner"] = relationship(back_populates=("WalkRequestList"))

    # child relationships (access children)
    WalkScheduleList : Mapped[List["WalkSchedule"]] = relationship(back_populates="walk_request")



class WalkerAvailability(SAFRSBaseX, Base):
    """
    description: Records the days of the week and times a walker is available.
    """
    __tablename__ = 'walker_availability'
    _s_collection_name = 'WalkerAvailability'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    walker_id = Column(ForeignKey('walker.id'), nullable=False)
    day_of_week = Column(String(10), nullable=False)
    time_of_day = Column(String(10), nullable=False)
    created_date = Column(DateTime, nullable=False)
    updated_date = Column(DateTime, nullable=False)
    created_by = Column(String, nullable=False)

    # parent relationships (access parent)
    walker : Mapped["Walker"] = relationship(back_populates=("WalkerAvailabilityList"))

    # child relationships (access children)



class WalkerRate(SAFRSBaseX, Base):
    """
    description: Sets the price for walks based on dog size and duration.
    """
    __tablename__ = 'walker_rate'
    _s_collection_name = 'WalkerRate'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    walker_id = Column(ForeignKey('walker.id'), nullable=False)
    dog_size = Column(String(10), nullable=False)
    duration = Column(String(10), nullable=False)
    price = Column(Integer, nullable=False)
    created_date = Column(DateTime, nullable=False)
    updated_date = Column(DateTime, nullable=False)
    created_by = Column(String, nullable=False)

    # parent relationships (access parent)
    walker : Mapped["Walker"] = relationship(back_populates=("WalkerRateList"))

    # child relationships (access children)



class WalkSchedule(SAFRSBaseX, Base):
    """
    description: Schedules a walk after a walker accepts a request.
    """
    __tablename__ = 'walk_schedule'
    _s_collection_name = 'WalkSchedule'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    walk_request_id = Column(ForeignKey('walk_request.id'), nullable=False)
    walker_id = Column(ForeignKey('walker.id'), nullable=False)
    status = Column(String(10), nullable=False)
    created_date = Column(DateTime, nullable=False)
    updated_date = Column(DateTime, nullable=False)
    created_by = Column(String, nullable=False)

    # parent relationships (access parent)
    walk_request : Mapped["WalkRequest"] = relationship(back_populates=("WalkScheduleList"))
    walker : Mapped["Walker"] = relationship(back_populates=("WalkScheduleList"))

    # child relationships (access children)
    PaymentList : Mapped[List["Payment"]] = relationship(back_populates="walk_schedule")
    WalkMonitoringList : Mapped[List["WalkMonitoring"]] = relationship(back_populates="walk_schedule")
    WalkerReviewList : Mapped[List["WalkerReview"]] = relationship(back_populates="walk_schedule")



class Payment(SAFRSBaseX, Base):
    """
    description: Records payments to walkers after a walk is completed.
    """
    __tablename__ = 'payment'
    _s_collection_name = 'Payment'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    walk_schedule_id = Column(ForeignKey('walk_schedule.id'), nullable=False)
    owner_id = Column(ForeignKey('owner.id'), nullable=False)
    walker_id = Column(ForeignKey('walker.id'), nullable=False)
    amount = Column(Integer, nullable=False)
    payment_method = Column(String(10), nullable=False)
    status = Column(String(10), nullable=False)
    created_date = Column(DateTime, nullable=False)
    updated_date = Column(DateTime, nullable=False)
    created_by = Column(String, nullable=False)

    # parent relationships (access parent)
    owner : Mapped["Owner"] = relationship(back_populates=("PaymentList"))
    walk_schedule : Mapped["WalkSchedule"] = relationship(back_populates=("PaymentList"))
    walker : Mapped["Walker"] = relationship(back_populates=("PaymentList"))

    # child relationships (access children)



class WalkMonitoring(SAFRSBaseX, Base):
    """
    description: Monitors the start and end of a walk.
    """
    __tablename__ = 'walk_monitoring'
    _s_collection_name = 'WalkMonitoring'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    walk_schedule_id = Column(ForeignKey('walk_schedule.id'), nullable=False)
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    created_date = Column(DateTime, nullable=False)
    updated_date = Column(DateTime, nullable=False)
    created_by = Column(String, nullable=False)

    # parent relationships (access parent)
    walk_schedule : Mapped["WalkSchedule"] = relationship(back_populates=("WalkMonitoringList"))

    # child relationships (access children)



class WalkerReview(SAFRSBaseX, Base):
    """
    description: Stores reviews given by owners about walkers.
    """
    __tablename__ = 'walker_review'
    _s_collection_name = 'WalkerReview'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    walk_schedule_id = Column(ForeignKey('walk_schedule.id'), nullable=False)
    owner_id = Column(ForeignKey('owner.id'), nullable=False)
    review_text = Column(String)
    rating = Column(Integer, nullable=False)
    created_date = Column(DateTime, nullable=False)
    updated_date = Column(DateTime, nullable=False)
    created_by = Column(String, nullable=False)

    # parent relationships (access parent)
    owner : Mapped["Owner"] = relationship(back_populates=("WalkerReviewList"))
    walk_schedule : Mapped["WalkSchedule"] = relationship(back_populates=("WalkerReviewList"))

    # child relationships (access children)

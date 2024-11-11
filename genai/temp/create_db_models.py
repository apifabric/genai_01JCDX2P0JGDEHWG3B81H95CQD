# using resolved_model gpt-4o-2024-08-06# created from response, to create create_db_models.sqlite, with test data
#    that is used to create project
# should run without error in manager 
#    if not, check for decimal, indent, or import issues

import decimal
import logging
import sqlalchemy
from sqlalchemy.sql import func 
from logic_bank.logic_bank import Rule
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Date, DateTime, Numeric, Boolean, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from datetime import date   
from datetime import datetime

logging.getLogger('sqlalchemy.engine.Engine').disabled = True  # remove for additional logging

Base = declarative_base()  # from system/genai/create_db_models_inserts/create_db_models_prefix.py


class Walker(Base):
    """
    description: Represents a dog walker who registers and provides services.
    """

    __tablename__ = 'walker'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    postal_code = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    email = Column(String, nullable=False)
    max_dogs_per_walk = Column(Integer, nullable=False)
    created_date = Column(DateTime, default=datetime.now, nullable=False)
    updated_date = Column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)
    created_by = Column(String, nullable=False)


class WalkerAvailability(Base):
    """
    description: Records the days of the week and times a walker is available.
    """

    __tablename__ = 'walker_availability'

    id = Column(Integer, primary_key=True, autoincrement=True)
    walker_id = Column(Integer, ForeignKey('walker.id'), nullable=False)
    day_of_week = Column(String(10), nullable=False)
    time_of_day = Column(String(10), nullable=False)  # morning or afternoon
    created_date = Column(DateTime, default=datetime.now, nullable=False)
    updated_date = Column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)
    created_by = Column(String, nullable=False)


class WalkerRate(Base):
    """
    description: Sets the price for walks based on dog size and duration.
    """

    __tablename__ = 'walker_rate'

    id = Column(Integer, primary_key=True, autoincrement=True)
    walker_id = Column(Integer, ForeignKey('walker.id'), nullable=False)
    dog_size = Column(String(10), nullable=False)  # small, medium, large
    duration = Column(String(10), nullable=False)  # short, medium, long
    price = Column(Integer, nullable=False)
    created_date = Column(DateTime, default=datetime.now, nullable=False)
    updated_date = Column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)
    created_by = Column(String, nullable=False)


class Owner(Base):
    """
    description: Represents a dog owner who requests services.
    """

    __tablename__ = 'owner'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    address = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    email = Column(String, nullable=False)
    created_date = Column(DateTime, default=datetime.now, nullable=False)
    updated_date = Column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)
    created_by = Column(String, nullable=False)


class PaymentInformation(Base):
    """
    description: Stores payment information for an owner.
    """

    __tablename__ = 'payment_information'

    id = Column(Integer, primary_key=True, autoincrement=True)
    owner_id = Column(Integer, ForeignKey('owner.id'), nullable=False)
    service = Column(String(10), nullable=False)  # Stripe, PayPal, Zelle
    created_date = Column(DateTime, default=datetime.now, nullable=False)
    updated_date = Column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)
    created_by = Column(String, nullable=False)


class Dog(Base):
    """
    description: Represents a dog belonging to an owner.
    """

    __tablename__ = 'dog'

    id = Column(Integer, primary_key=True, autoincrement=True)
    owner_id = Column(Integer, ForeignKey('owner.id'), nullable=False)
    name = Column(String, nullable=False)
    breed = Column(String, nullable=False)
    size = Column(String(10), nullable=False)  # small, medium, large
    notes = Column(String)
    created_date = Column(DateTime, default=datetime.now, nullable=False)
    updated_date = Column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)
    created_by = Column(String, nullable=False)


class WalkRequest(Base):
    """
    description: A request made by an owner for a dog walk.
    """

    __tablename__ = 'walk_request'

    id = Column(Integer, primary_key=True, autoincrement=True)
    owner_id = Column(Integer, ForeignKey('owner.id'), nullable=False)
    date = Column(Date, nullable=False)
    time = Column(String(10), nullable=False)
    duration = Column(String(10), nullable=False)  # short, medium, long
    created_date = Column(DateTime, default=datetime.now, nullable=False)
    updated_date = Column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)
    created_by = Column(String, nullable=False)


class WalkSchedule(Base):
    """
    description: Schedules a walk after a walker accepts a request.
    """

    __tablename__ = 'walk_schedule'

    id = Column(Integer, primary_key=True, autoincrement=True)
    walk_request_id = Column(Integer, ForeignKey('walk_request.id'), nullable=False)
    walker_id = Column(Integer, ForeignKey('walker.id'), nullable=False)
    status = Column(String(10), nullable=False)  # pending, confirmed, completed
    created_date = Column(DateTime, default=datetime.now, nullable=False)
    updated_date = Column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)
    created_by = Column(String, nullable=False)


class WalkerReview(Base):
    """
    description: Stores reviews given by owners about walkers.
    """

    __tablename__ = 'walker_review'

    id = Column(Integer, primary_key=True, autoincrement=True)
    walk_schedule_id = Column(Integer, ForeignKey('walk_schedule.id'), nullable=False)
    owner_id = Column(Integer, ForeignKey('owner.id'), nullable=False)
    review_text = Column(String)
    rating = Column(Integer, nullable=False)  # assuming 1 to 5
    created_date = Column(DateTime, default=datetime.now, nullable=False)
    updated_date = Column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)
    created_by = Column(String, nullable=False)


class WalkMonitoring(Base):
    """
    description: Monitors the start and end of a walk.
    """

    __tablename__ = 'walk_monitoring'

    id = Column(Integer, primary_key=True, autoincrement=True)
    walk_schedule_id = Column(Integer, ForeignKey('walk_schedule.id'), nullable=False)
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    created_date = Column(DateTime, default=datetime.now, nullable=False)
    updated_date = Column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)
    created_by = Column(String, nullable=False)


class Payment(Base):
    """
    description: Records payments to walkers after a walk is completed.
    """

    __tablename__ = 'payment'

    id = Column(Integer, primary_key=True, autoincrement=True)
    walk_schedule_id = Column(Integer, ForeignKey('walk_schedule.id'), nullable=False)
    owner_id = Column(Integer, ForeignKey('owner.id'), nullable=False)
    walker_id = Column(Integer, ForeignKey('walker.id'), nullable=False)
    amount = Column(Integer, nullable=False)
    payment_method = Column(String(10), nullable=False)  # Zelle, PayPal, Stripe
    status = Column(String(10), nullable=False)  # pending, completed
    created_date = Column(DateTime, default=datetime.now, nullable=False)
    updated_date = Column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)
    created_by = Column(String, nullable=False)


class Administration(Base):
    """
    description: Administration data for the business.
    """

    __tablename__ = 'administration'

    id = Column(Integer, primary_key=True, autoincrement=True)
    admin_name = Column(String, nullable=False)
    created_date = Column(DateTime, default=datetime.now, nullable=False)
    updated_date = Column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)
    created_by = Column(String, nullable=False)


# ALS/GenAI: Create an SQLite database
engine = create_engine('sqlite:///system/genai/temp/create_db_models.sqlite')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# ALS/GenAI: Prepare for sample data

from datetime import datetime, date

walker1 = Walker(first_name='John', last_name='Doe', postal_code='12345', phone='5551234567', email='john@example.com', max_dogs_per_walk=3, created_by='admin')
walker2 = Walker(first_name='Jane', last_name='Smith', postal_code='23456', phone='5552345678', email='jane@example.com', max_dogs_per_walk=2, created_by='admin')
walker3 = Walker(first_name='Bob', last_name='Brown', postal_code='34567', phone='5553456789', email='bob@example.com', max_dogs_per_walk=5, created_by='admin')
walker4 = Walker(first_name='Alice', last_name='Jones', postal_code='45678', phone='5554567890', email='alice@example.com', max_dogs_per_walk=4, created_by='admin')

walker_availability1 = WalkerAvailability(walker_id=1, day_of_week='Mon', time_of_day='morning', created_by='admin')
walker_availability2 = WalkerAvailability(walker_id=2, day_of_week='Tues', time_of_day='afternoon', created_by='admin')
walker_availability3 = WalkerAvailability(walker_id=3, day_of_week='Wed', time_of_day='morning', created_by='admin')
walker_availability4 = WalkerAvailability(walker_id=4, day_of_week='Thurs', time_of_day='afternoon', created_by='admin')

walker_rate1 = WalkerRate(walker_id=1, dog_size='small', duration='short', price=15, created_by='admin')
walker_rate2 = WalkerRate(walker_id=2, dog_size='medium', duration='medium', price=25, created_by='admin')
walker_rate3 = WalkerRate(walker_id=3, dog_size='large', duration='long', price=35, created_by='admin')
walker_rate4 = WalkerRate(walker_id=4, dog_size='small', duration='medium', price=20, created_by='admin')

owner1 = Owner(name='Michael Green', address='123 Elm St', phone='1231231234', email='michaelg@example.com', created_by='admin')
owner2 = Owner(name='Rachel White', address='234 Oak St', phone='2342342345', email='rachelw@example.com', created_by='admin')
owner3 = Owner(name='Stacy Blue', address='345 Maple St', phone='3453453456', email='stacyb@example.com', created_by='admin')
owner4 = Owner(name='Tom Black', address='456 Pine St', phone='4564564567', email='tom@example.com', created_by='admin')

payment_info1 = PaymentInformation(owner_id=1, service='Stripe', created_by='admin')
payment_info2 = PaymentInformation(owner_id=2, service='PayPal', created_by='admin')
payment_info3 = PaymentInformation(owner_id=3, service='Zelle', created_by='admin')
payment_info4 = PaymentInformation(owner_id=4, service='Stripe', created_by='admin')

dog1 = Dog(owner_id=1, name='Fido', breed='Labrador', size='large', notes='Friendly', created_by='admin')
dog2 = Dog(owner_id=2, name='Rex', breed='Bulldog', size='medium', notes='Likes to chew', created_by='admin')
dog3 = Dog(owner_id=3, name='Bella', breed='Poodle', size='small', notes='Energetic', created_by='admin')
dog4 = Dog(owner_id=4, name='Charlie', breed='Beagle', size='small', notes='Calm', created_by='admin')

walk_request1 = WalkRequest(owner_id=1, date=date(2024, 4, 1), time='morning', duration='short', created_by='admin')
walk_request2 = WalkRequest(owner_id=2, date=date(2024, 4, 2), time='afternoon', duration='medium', created_by='admin')
walk_request3 = WalkRequest(owner_id=3, date=date(2024, 4, 3), time='morning', duration='long', created_by='admin')
walk_request4 = WalkRequest(owner_id=4, date=date(2024, 4, 4), time='afternoon', duration='short', created_by='admin')

walk_schedule1 = WalkSchedule(walk_request_id=1, walker_id=1, status='confirmed', created_by='admin')
walk_schedule2 = WalkSchedule(walk_request_id=2, walker_id=2, status='pending', created_by='admin')
walk_schedule3 = WalkSchedule(walk_request_id=3, walker_id=3, status='completed', created_by='admin')
walk_schedule4 = WalkSchedule(walk_request_id=4, walker_id=4, status='confirmed', created_by='admin')

walker_review1 = WalkerReview(walk_schedule_id=3, owner_id=1, review_text='Great service!', rating=5, created_by='admin')
walker_review2 = WalkerReview(walk_schedule_id=2, owner_id=2, review_text='Too late!', rating=3, created_by='admin')
walker_review3 = WalkerReview(walk_schedule_id=1, owner_id=3, review_text='Good walk', rating=4, created_by='admin')
walker_review4 = WalkerReview(walk_schedule_id=4, owner_id=4, review_text='Not satisfied', rating=2, created_by='admin')

walk_monitoring1 = WalkMonitoring(walk_schedule_id=1, start_time=datetime(2024, 4, 1, 9, 0), end_time=datetime(2024, 4, 1, 10, 0), created_by='admin')
walk_monitoring2 = WalkMonitoring(walk_schedule_id=2, start_time=datetime(2024, 4, 2, 15, 0), end_time=datetime(2024, 4, 2, 16, 0), created_by='admin')
walk_monitoring3 = WalkMonitoring(walk_schedule_id=3, start_time=datetime(2024, 4, 3, 8, 0), end_time=datetime(2024, 4, 3, 10, 0), created_by='admin')
walk_monitoring4 = WalkMonitoring(walk_schedule_id=4, start_time=datetime(2024, 4, 4, 14, 0), end_time=datetime(2024, 4, 4, 15, 0), created_by='admin')

payment1 = Payment(walk_schedule_id=1, owner_id=1, walker_id=1, amount=15, payment_method='Stripe', status='completed', created_by='admin')
payment2 = Payment(walk_schedule_id=2, owner_id=2, walker_id=2, amount=25, payment_method='PayPal', status='pending', created_by='admin')
payment3 = Payment(walk_schedule_id=3, owner_id=3, walker_id=3, amount=35, payment_method='Zelle', status='completed', created_by='admin')
payment4 = Payment(walk_schedule_id=4, owner_id=4, walker_id=4, amount=20, payment_method='Stripe', status='completed', created_by='admin')

administration1 = Administration(admin_name='Admin1', created_by='system')
administration2 = Administration(admin_name='Admin2', created_by='system')
administration3 = Administration(admin_name='Admin3', created_by='system')
administration4 = Administration(admin_name='Admin4', created_by='system')


session.add_all([walker1, walker2, walker3, walker4, walker_availability1, walker_availability2, walker_availability3, walker_availability4, walker_rate1, walker_rate2, walker_rate3, walker_rate4, owner1, owner2, owner3, owner4, payment_info1, payment_info2, payment_info3, payment_info4, dog1, dog2, dog3, dog4, walk_request1, walk_request2, walk_request3, walk_request4, walk_schedule1, walk_schedule2, walk_schedule3, walk_schedule4, walker_review1, walker_review2, walker_review3, walker_review4, walk_monitoring1, walk_monitoring2, walk_monitoring3, walk_monitoring4, payment1, payment2, payment3, payment4, administration1, administration2, administration3, administration4])
session.commit()

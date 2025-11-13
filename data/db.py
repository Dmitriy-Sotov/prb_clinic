from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean, ForeignKey, Numeric, VARCHAR, Date
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base

base = declarative_base()
__factory = None


class Company(base):
    __tablename__ = 'companies'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(VARCHAR(500), nullable=False)



class Police(base):
    __tablename__ = 'polices'

    id = Column(Integer, primary_key=True, autoincrement=True)
    number = Column(VARCHAR(500), nullable=False)
    created_date = Column(Date, nullable=False)
    company_id = Column(Integer, ForeignKey('companies.id'), nullable=False)




class Card(base):
    __tablename__ = 'cards'

    id = Column(Integer, primary_key=True, autoincrement=True)
    number = Column(VARCHAR(500), nullable=False)
    created_date = Column(Date, nullable=False)
    last_visit = Column(Date, nullable=False)
    next_visit = Column(Date, nullable=False)

class Gender(base):
    __tablename__ = 'genders'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(VARCHAR(500), nullable=False)

class Role(base):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(VARCHAR(500), nullable=False)

class Specialization(base):
    __tablename__ = 'specializations'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(VARCHAR(500), nullable=False)

class Medicine(base):
    __tablename__ = 'medicines'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(VARCHAR(500), nullable=False)

class Storage(base):
    __tablename__ = 'storages'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(VARCHAR(500), nullable=False)


class Vendor(base):
    __tablename__ = 'vendors'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(VARCHAR(500), nullable=False)

class Hospitalization(base):
    __tablename__ = 'type_hospitalizations'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(VARCHAR(500), nullable=False)


class Diagnoses(base):
    __tablename__ = 'diagnoses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(VARCHAR(500), nullable=False)


class Patient(base):
    __tablename__ = 'patients'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(VARCHAR(500), nullable=False)
    last_name = Column(VARCHAR(500), nullable=False)
    patronymic = Column(VARCHAR(500), nullable=False)
    number_passport = Column(VARCHAR(500), nullable=False)
    serial_passport = Column(VARCHAR(500), nullable=False)
    birthday = Column(Date, nullable=False)
    address = Column(VARCHAR(500), nullable=False)
    phone = Column(VARCHAR(500), nullable=False)
    email = Column(VARCHAR(500), nullable=False)
    photo = Column(VARCHAR(500), nullable=False)
    qr_code = Column(VARCHAR(500), nullable=False)
    gender_id = Column(Integer, ForeignKey('genders.id'), nullable=False)
    card_id = Column(Integer, ForeignKey('cards.id'), nullable=False)
    police_id = Column(Integer, ForeignKey('polices.id'), nullable=False)

class Staff(base):
    __tablename__ = 'staff'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(VARCHAR(500), nullable=False)
    last_name = Column(VARCHAR(500), nullable=False)
    patronymic = Column(VARCHAR(500), nullable=False)
    specialization_id = Column(Integer, ForeignKey('specializations.id'), nullable=False)
    number_passport = Column(VARCHAR(4), nullable=False)
    serial_passport = Column(VARCHAR(8), nullable=False)
    phone_numbers = Column(VARCHAR(10), nullable=False)
    login = Column(VARCHAR(100), nullable=False)
    password = Column(VARCHAR(100), nullable=False)
    role_id = Column(Integer, ForeignKey('roles.id'), nullable=False)

class Department(base):
    __tablename__ = 'departments'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(VARCHAR(500), nullable=False)



class Event(base):
    __tablename__ = 'type_events'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(VARCHAR(500), nullable=False)

class MedicineHistories(base):
    __tablename__ = 'medicine_histories'
    id = Column(Integer, primary_key=True, autoincrement=True)
    date_receipt = Column(Date, nullable=False)
    expiration_date = Column(Date, nullable=False)
    count = Column(VARCHAR(100), nullable=False)
    optimal_count = Column(VARCHAR(100), nullable=False)
    is_cancelled = Column(VARCHAR(100), nullable=False)
    why_cancelled = Column(VARCHAR(500), nullable=False)
    medicine_id = Column(Integer, ForeignKey('medicines.id'), nullable=False)
    storage_id = Column(Integer, ForeignKey('storages.id'), nullable=False)
    vendor_id = Column(Integer, ForeignKey('vendors.id'), nullable=False)


class History(base):
    __tablename__ = 'histories'
    id = Column(Integer, primary_key=True, autoincrement=True)
    patient_id = Column(Integer, ForeignKey('patients.id'), nullable=False)
    diagnoses_id = Column(Integer, ForeignKey('diagnoses.id'), nullable=False)

class Hospitalizations(base):
    __tablename__ = 'hospitalizations'
    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(Date, nullable=False)
    time = Column(Date, nullable=False)
    is_cancelled = Column(VARCHAR(100), nullable=False)
    why_cancelled = Column(VARCHAR(500), nullable=False)
    patient_id = Column(Integer, ForeignKey('patients.id'), nullable=False)
    diagnoses_id = Column(Integer, ForeignKey('diagnoses.id'), nullable=False)
    type_id = Column(Integer, ForeignKey('departments.id'), nullable=False)
    doctor_id = Column(Integer, ForeignKey('staff.id'), nullable=False)


class Bed(base):
    __tablename__ = 'beds'
    id = Column(Integer, primary_key=True, autoincrement=True)
    bed_number = Column(VARCHAR(500), nullable=False)
    patient_id = Column(Integer, ForeignKey('patients.id'), nullable=False)

class Events(base):
    __tablename__ = 'events'
    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(Date, nullable=False)
    doctors = Column(VARCHAR(500), nullable=False)
    name = Column(VARCHAR(500), nullable=False)
    recommendations = Column(VARCHAR(500), nullable=False)
    anamnez= Column(VARCHAR(500), nullable=False)
    simptoms = Column(VARCHAR(500), nullable=False)
    diagnoses_id = Column(Integer, ForeignKey('diagnoses.id'), nullable=False)
    type_id = Column(Integer, ForeignKey('departmens.id'), nullable=False)
    time = Column(Date, nullable=False)


def init_db():
    eng = create_engine('postgresql+psycopg2://postgres:123@localhost:5432/prb_clinic')

    global __factory
    __factory = sessionmaker(bind=eng)

    base.metadata.create_all(eng)


def connect() -> Session:
    global __factory
    return __factory()

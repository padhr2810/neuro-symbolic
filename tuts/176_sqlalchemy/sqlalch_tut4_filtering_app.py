

from sqlalch_tut4_filtering_models import Patient, engine
from sqlalchemy import and_, not_, or_
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

# If there is data in the database, dont add more data
if session.query(Patient).count() < 1:
    session.add(Patient(patient_name="Iron Man", patient_age=23))
    session.add(Patient(patient_name="Coding Man", patient_age=56))
    session.add(Patient(patient_name="Banana Man", patient_age=78))
    session.add(Patient(patient_name="Zeq", patient_age=99))

    session.commit()

# query all users
users_all = session.query(Patient).all()
print('All Patients:', len(users_all))


# ========================================================================================
print("\nFILTER (AGE >= 25)")
# query all users with age greater than or equal to 25
users_filtered = session.query(Patient).filter(Patient.patient_age >= 25).all()
print('Filtered Patients:', len(users_filtered))

# ========================================================================================
print("\nFILTER BY (AGE == 30)")
# query all patients with age is equal to 30
users = session.query(Patient).filter_by(patient_age=30).all()

for user in users:
    print(f"Patient age: {user.patient_age}")

# ========================================================================================
print("\nWHERE (AGE >= 30)")
# query all users with age is greater than or equal to 30
users = session.query(Patient).where(Patient.patient_age >= 30).all()

for user in users:
    print(f"Patient age: {user.patient_age}")

# ========================================================================================
print("\nOR (AGE >= 30 OR NAME == 'IRON MAN'")
# query all users with age is greater than or equal to 30 or name is 'Iron Man'
users = session.query(Patient).where(or_(Patient.patient_age >= 30, Patient.patient_name == "Iron Man")).all()
print(f"Patients: {len(users)}")

users = session.query(Patient).where((Patient.patient_age >= 30) | ( Patient.patient_name == "Iron Man")).all()
print(f"Patients: {len(users)}")

# ========================================================================================
print("\nAND (AGE >= 30 AND NAME == 'IRON MAN'")
# query all users with age is greater than or equal to 30 AND name is 'Iron Man'
users = session.query(Patient).where(and_ (Patient.patient_age >= 30, Patient.patient_name == "Iron Man")).all()

print(f"Patients: {len(users)}")

# ========================================================================================
print("\nNOT")
# query all users where the name is not 'Iron Man'
users = session.query(Patient).where(not_(Patient.patient_name == "Iron Man")).all()

print(f"Patients: {len(users)}")

# ========================================================================================
print("\nCOMBINE OPTIONS (I.E. COMBINE 'OR' / 'NOT' / 'AND' )")
users = (
    session.query(Patient).filter(
        or_(
            not_(Patient.patient_name == "Iron Man"),
            and_(
                Patient.patient_age > 35,
                Patient.patient_age < 60)
            )
    )
)

for user in users.all():
    print(f'{user.patient_age} - {user.patient_name}')



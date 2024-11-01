
# IMPORT 'func' TO ACCESS 'func.count' --- e.g. count the number of patients in a particular group.

from sqlalch_tut5_grouping_models import Patient, engine
from sqlalchemy import and_, func, not_, or_
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

# If there is data in the database, dont add more data
if session.query(Patient).count() < 1:
    session.add(Patient(patient_name="Iron Man", patient_age=23))
    session.add(Patient(patient_name="Mickey Mouse", patient_age=23))
    session.add(Patient(patient_name="Coding Man", patient_age=33))
    session.add(Patient(patient_name="Banana Man", patient_age=78))
    session.add(Patient(patient_name="Zeq", patient_age=99))
    session.add(Patient(patient_name="Bubba", patient_age=99))
    session.commit()


print(" ========================================================================================")
print("\nGROUP BY (AGE,)")
users_group_by_age = (
    session.query(Patient.patient_age).group_by(Patient.patient_age).all()
)
print(users_group_by_age)

print(" \n\n========================================================================================")
print("\nGROUP BY ADDITIONAL CRITERIA (AGE, COUNT)")
# count the number of users by age
users_count_by_age = session.query(Patient.patient_age, func.count(Patient.patient_id)).group_by(Patient.patient_age).all()
print(users_count_by_age)

print(" \n\n========================================================================================")
print("\nCHAINING METHODS - I.E. COMBINE 2 FILTERS (AGE>24) AND (AGE<50)")
users = (
    session.query(Patient).filter(Patient.patient_age > 24).filter(Patient.patient_age < 50).all()
)

print(f"\nMETHOD 1:")
for user in users:
    print(f"{user.patient_age = }")

print(f"\nMETHOD 2:")
# or like this
users_tuple = (
    session.query(Patient.patient_age, func.count(Patient.patient_id))
    .filter(Patient.patient_age > 24)
    .order_by(Patient.patient_age)
    .filter(Patient.patient_age < 50)
    .group_by(Patient.patient_age)
    .all()
)
for age, count in users_tuple :
    print(f"Age: {age} - Patients: {count}")


print(" \n\n========================================================================================")
print("\nDELAY .all() ... don't need to call .all() immediately, can apply more filters conditionally. And later call '.all()' to get the conditionally chained result")
print(" \n.all() = Return the results represented by this Query as a list... This results in an execution of the underlying SQL statement.")
only_iron_man = True
group_by_age = True

users = session.query(Patient)
if only_iron_man:
    users = users.filter(Patient.patient_name == "Iron Man")
if group_by_age:
    users = users.group_by(Patient.patient_age)
users = users.all()
for user in users:
    print(f"\nPatient age: {user.patient_age}, name: {user.patient_name}")
    
    

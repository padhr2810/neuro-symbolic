

from sqlalch_tut2_crud_models import Patient, engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

# ===================================================================================
# CREATE

# If there is data in the database, dont add more data
if session.query(Patient).count() < 1:
    # Create one new Patient
    patient = Patient(patient_name='John Doe 1', patient_age=30)
    session.add(patient)
    session.commit()

    # Create multiple Users
    user_1 = Patient(patient_name='John Doe 2', patient_age=30)
    user_2 = Patient(patient_name='Andrew Pip', patient_age=25)
    user_3 = Patient(patient_name='Iron Man', patient_age=57)
    user_4 = Patient(patient_name='Richard Rodriguez', patient_age=25)

    session.add(user_1)
    session.add(user_2)
    session.add_all([user_3, user_4])
    session.commit()

# ===================================================================================
# READ
# query all users
users = session.query(Patient).all()
print(users)

# Get the first User info
user = users[0]
print(user)
print(user.patient_id)
print(user.patient_name)
print(user.patient_age)

# "one_or_none()" - return None if no matching item in db; or return instance of class Product if exactly one matching item; or raise exception if multiple matching items in db.
user = session.query(Patient).filter_by(patient_id=1).one_or_none()
print(user)

# Loop over each User
for user in users:
    print(f"Patient id: {user.patient_id}, name: {user.patient_name}, age: {user.patient_age}")

# Get first user from the data (return None if no results)
user_first = session.query(Patient).first()
print('First Patient: ', user_first)


# ===================================================================================
# UPDATE
# update a user's name
user = users[0]
user.patient_name = 'Jane Doe'
session.commit()

# ===================================================================================
# DELETE
# delete a user record
user = users[0]
session.delete(user)
session.commit()



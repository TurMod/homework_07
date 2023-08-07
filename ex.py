from faker import Faker
from connect_db import session
from sqlalchemy import func
from models import Student

fake_data = Faker()

first_name, last_name = fake_data.name(word=2).split(' ')

print(first_name, last_name)
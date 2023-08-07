from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://postgres:turbomy123@localhost:5432/homework_07_db')
Session = sessionmaker(bind=engine)
session = Session()

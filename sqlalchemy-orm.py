username, password, database, host, port = "psql1", "pwd1", "psql1", "localhost", 5432

# docker run -d --name psql1 -e POSTGRES_USER=psql1 -e POSTGRES_PASSWORD=pwd1 -e POSTGRES_DB=psql1 -p 5432:5432 postgres

# #

# python -m pip install sqlalchemy psycopg2

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Database connection
engine = create_engine(f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}")
Base = declarative_base()

# Define a model
class User(Base):
  __tablename__ = "users"
  id = Column(Integer, primary_key=True)
  name = Column(String)

# Create tables
Base.metadata.create_all(engine)

# Session
Session = sessionmaker(bind=engine)
session = Session()

# Add a user
new_user = User(name="Bob")
session.add(new_user)
session.commit()

# Query users
for user in session.query(User).all():
  print("id and name")
  print(user.id, user.name)

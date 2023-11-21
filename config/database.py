import os
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

sqlite_db_name: str = "database.sqlite"
base_dir = os.path.dirname(os.path.realpath(__file__))

databse_url: str = f"sqlite:///{os.path.join(base_dir, sqlite_db_name)}"
engine: str = create_engine(databse_url, echo=True)
sesion = sessionmaker(bind=engine)
Base = declarative_base()
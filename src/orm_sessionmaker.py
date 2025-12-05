from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import(database_exists,create_database)
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os 

from models import Base
load_dotenv()
class SessionMakerForORM:
    def get_engine(self):
        user =os.environ['MYSQL_USER_NAME']
        password=os.environ['MYSQL_PASSWORD']
        host=os.environ['MYSQL_HOST']
        port=os.environ['MYSQL_PORT']
        database=os.environ['MYSQL_DB_NAME']
#conn_Str meanss connection str
        conn_str=f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}'

        if not database_exists(conn_str):
            create_database(conn_str)
        _engine=create_engine(conn_str)
        Base.metadata.create_all(_engine)
        return _engine
    
    def get_session(self):
        _engine=self.get_engine()
        _session=sessionmaker(bind=_engine)
        return _session

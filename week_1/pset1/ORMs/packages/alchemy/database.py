from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Session

# configure SQLALCHEMY_DATABASE_URL

engine = create_engine("sqlite://../packages.db", echo=True, connect_args={"check_same_thread": False})

# the factory. It's configured to be bound to your Engine and creates a transactional Session when called
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# SQLAlchemyORM 2.0+ versions
class Base(DeclarativeBase):
    pass
 
# create sessions
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

from sqlalchemy import Column, Integer, String
from app.db.session import Base

class Institution(Base):
    __tablename__ = "institutions"
    id = Column(Integer, primary_key=True, index=True)
    cik = Column(String, unique=True, nullable=False, index=True)  # SEC CIK
    name = Column(String, nullable=False, index=True)
    address = Column(String)
    city = Column(String)
    state = Column(String)
    zipcode = Column(String) 
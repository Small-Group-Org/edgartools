from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.db.session import Base

class Filing13F(Base):
    __tablename__ = "13f_filings"
    accession_number = Column(String, primary_key=True, index=True)
    institution_id = Column(Integer, ForeignKey("institutions.id"), nullable=False, index=True)
    filing_date = Column(Date, nullable=False, index=True)
    period_of_report = Column(Date, nullable=False, index=True)
    file_url = Column(String, nullable=False)
    primary_document = Column(String)
    total_value_usd = Column(Float)
    holdings_count = Column(Integer, default=0)
    manager_name = Column(String)
    signer = Column(String)
    # Relationship to holdings
    holdings = relationship("Filing13FHolding", back_populates="filing", cascade="all, delete-orphan")

class Filing13FHolding(Base):
    __tablename__ = "13f_holdings"
    filing_id = Column(String, ForeignKey("13f_filings.accession_number"), primary_key=True)
    cusip = Column(String, primary_key=True)
    class_of_security = Column(String, primary_key=True)
    issuer = Column(String, nullable=False)
    value = Column(Float)  # Value in thousands USD
    shares_prn_amount = Column(Float)
    type = Column(String)  # Shares or Principal
    put_call = Column(String)
    investment_discretion = Column(String)
    sole_voting = Column(Integer)
    shared_voting = Column(Integer)
    non_voting = Column(Integer)
    ticker = Column(String, index=True)
    # Relationship to filing
    filing = relationship("Filing13F", back_populates="holdings") 
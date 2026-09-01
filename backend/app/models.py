from sqlalchemy import Column, Integer, String, Text

from .database import Base


class ScanResult(Base):
    __tablename__ = "scan_results"

    id = Column(Integer, primary_key=True, index=True)
    target = Column(String(255), nullable=False, index=True)
    finding = Column(Text, nullable=False)
